## Par câble

### Description

On récupère une série de tensions (valant -1 ou 1) captées dans un câble. L'objectif est donc de les déchiffrer.
Il existe [différentes manières](https://fr.wikipedia.org/wiki/Codage_en_ligne) de coder des données, à nous de retrouver la bonne.

### Solution

Ici, le code utilisé est le [Non Return to Zero Inverted](https://fr.wikipedia.org/wiki/Non_Return_to_Zero_Inverted). Reste à l'implémenter avec un script python, et c'est gagné (en une ligne pour rigoler) :
```python
data = open('Cable.txt','r').read().split(' ')

print(''.join([bytes([int(byte,2)]).decode() for byte in [''.join([str(int(data[i] != data[i+1])) for i in range(len(data) - 1)])[i:i+8] for i in range(0, len(''.join([str(int(data[i] != data[i+1])) for i in range(len(data) - 1)])), 8)]]))
```
On obtient le flag : 404CTF{N0n3_R3tUrn_Z3r0_InV3rtEd_f0r3v3r}.