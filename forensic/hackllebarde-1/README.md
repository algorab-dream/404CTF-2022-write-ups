## Hackllebarde ransomware (1/4)

### Description

On nous fournit une capture réseau, dans laquelle un grand nombre de paquets TCP sans données sont échangés.
En observant un peu la structure de ces paquets, on peut remarquer que les flags TCP varient sans cesse, et sans grande logique. Peut-être est-ce un moyen de faire passer des données ?

### Solution 

On récupère chaque groupe de flags que l'on interprète comme un octet :

```python
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
```
On récupère ensuite le flag : 404CTF{L3s_fL4gS_TCP_Pr1S_3n_fL4G}.