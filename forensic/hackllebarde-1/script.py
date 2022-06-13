import os

flags = os.popen('tshark -r ransomware1.pcapng -Y "ip.src == 172.17.0.1" -T fields -e tcp.flags.str').read().split('\n')
bitstr = ""

for flag in flags:
    flag = list(flag)[-8:]
    for char in flag:
        if char != '·':
            bitstr += '1'
        else:
            bitstr += '0'

bytes_str = int(bitstr, 2).to_bytes((len(bitstr) + 7) // 8, byteorder='big')

open('haccklebarde.pdf','wb').write(bytes_str)