# xX_SignedArchive_Xx

## File format

The signed archive file format is made of a header section followed by a data section. Here is how they are made :

**Header:**
- Magic number (5 bytes) : `01 5A 53 69 67`
- \x02 : `02`
- Signature of the data (300 bytes, 0-padded, big endian)
- \x03 : `03`
- Size of data section (4 bytes, 0-padded, big endian)
- \x04 : `04`

And then put the data section.

## Signature algorithm

- Compute the checksum of the data section
- Encrypt the checksum using the private key

## Verification algorithm

- Compute the checksum of the data section
- Decrypt the signature using the public key
- Compare the computed checksum with the decrypted signature