## Un simple oracle (2/2)

### Description

Le principe est le même que pour [le premier oracle](/crypto/oracle-1), mais sans la valeur du module : 

```
Il y a eu quelques petits problèmes lors de ma précédente itération, mais tout a été résolu!
Je peux à nouveau montrer mon secret sans craintes:
23096045053715175422659633380210449468300237206135873744927146717570074416155977532687747127703467575387094042812272907316437282809020442636842229007258830753759682724920822693689924764445218680208868883336474578104145600471564351411172735569632058719674954491077094921753318868364084739146102355971779522079448172618230051018150966838973382626883919977287109511853982502661705974647096111335753221186939125044658347717792615899756279282151835154215631917313346657294865496134514664965984220483854152056079003858513704677621523328519881326439170586757888009285506257399152555686891668152324966538174063971424838089030
Par mesure de sécurité, je ne peux malheureusement plus tout partager ici:
e = 65537

Ceci étant dit, passons à ce que vous vouliez me dire!
```

#### Exploit

Sachant que pour résoudre [le premier oracle](/crypto/oracle-1), on ne s'était pas servi du module, on peut simplement reprendre le même script :

```python
from pwn import *

conn = remote('challenge.404ctf.fr',30594)
conn.recvline()
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