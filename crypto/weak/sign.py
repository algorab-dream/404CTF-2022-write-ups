import sys

from secret import private_key

# Script for signing and verifying signed archives

def checksum(data: bytes) -> int:
    # Sum the integer value of each byte and multiply the result by the length
    chksum = sum(data) * len(data)

    return chksum


def compute_signature(data: bytes, private_key: int, mod: int) -> int:
    # Compute the checksum
    chksum = checksum(data)
    # Sign it
    signature = pow(chksum, private_key, mod)

    return signature


def check_signature(data: bytes, signature: int, mod: int) -> bool:
    # In our case, public key exponent is always 65537
    to_check = pow(signature, 65537, mod)

    # Compute the actual checksum
    chksum = checksum(data)

    return chksum == to_check


def sign(in_file: str, out_file: str, private_key: int, mod: int) -> None:
    with open(in_file, "rb") as f:
        data = f.read()
    
    signature = compute_signature(data, private_key, mod)
    signature_bytes = signature.to_bytes(300, "big")

    size_bytes = len(data).to_bytes(4, "big")

    out_bytes = b"\x01ZSig\x02" + signature_bytes + b"\x03" + size_bytes + b"\x04" + data

    with open(out_file, "wb+") as f:
        f.write(out_bytes)


def verify(in_file: str, mod: int):
    with open(in_file, "rb") as f:
        magic = f.read(5)
        if magic != b"\x01ZSig":
            return False
        
        f.read(1)
        signature = int.from_bytes(f.read(300), "big")

        f.read(1)
        size = int.from_bytes(f.read(4), "big")

        f.read(1)
        data = f.read()

        if len(data) != size:
            return False
        
        if check_signature(data, signature, mod):
            return data
        else:
            return False


def print_usage():
    print("Usage:", file=sys.stderr)
    print("\t" + sys.argv[0] + " sign <input_file> <output_file>", file=sys.stderr)
    print("or", file=sys.stderr)
    print("\t" + sys.argv[0] + " run <input_file>", file=sys.stderr)
    exit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage()

    mode = sys.argv[1]
    if mode not in ["sign", "run"]:
        print_usage()

    mod = 221027607696016055330225199730004315633371808272167570987738708218816159833989480355901373361425282092914736310694029777936753927631812865622326955729592220642870561983138852634957728096291312307092550755716648880511833062740232861937708219741536005110883882372419034097193889630562360199603238619292770230484188772936262259410362789470181350351169944338502734560511300850685040238166004812599312697863279097878240430563714732124632651690886061257136157390268372745145428925223780181129620285589838270820282051669863964181353006744093479768868790988029676360187172005933366198639891820146811651748962622102323334597

    if mode == "sign" and len(sys.argv) == 4:
        sign(sys.argv[2], sys.argv[3], private_key, mod)
    elif mode == "run" and len(sys.argv) == 3:
        data = verify(sys.argv[2], mod)
        if data:
            exec(data.decode())
        else:
            print("Wrong signature!", file=sys.stderr)
    else:
        print_usage()