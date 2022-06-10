from pwn import *

conn = remote('challenge.404ctf.fr',32128)
conn.recvline()
cipher = int(conn.recvline().decode())

conn.recvline()
e = int(conn.recvline().decode().split(' ')[2])
conn.recvline()
conn.recvline()
conn.recvline()

cc = str(cipher*(2**e)).encode()
conn.sendline(cc)

conn.recvline()

tmodn = int(conn.recvline().decode())//2

tmodn_byte = tmodn.to_bytes((tmodn.bit_length() + 7) // 8, 'big')

print(tmodn_byte)
