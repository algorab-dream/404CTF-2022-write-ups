## Weak Signature

### Description

L'objectif ici est de faire exécuter un code par le serveur en le signant correctement. L'algorithme de signature ainsi qu'un exemple de script signé nous est donné en exemple.

Dans l'algorithme de signature, ces deux fonctions sont le coeur de la signature :

```python
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
```

On remarque immédiatement un défaut majeur de cet algorithme, qui va constituer la base de l'exploit : la signature ne dépend pas des données, mais simplement que leur longueur et de leur somme.

La documentation de l'algorithme de signature nous donne également le format de celle-ci :

```
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
```

### Exploit

Puisqu'on n'a pas la clé privée, pourquoi chercher à forger une signature, alors que l'on peut réutiliser celle qui nous est donnée ?

Cela se fait en 3 étapes. 

#### Coder la payload

On fait simple :
```python
payload = b"a=open('flag.txt','r').read()\n\nprint(a)#"
```
Le ```#``` va nous servir ici à rajouter des données ensuite pour obtenir des données qui correspondent à la signature.

#### Trouver la taille finale de la payload

On sait que le checksum correspond à la taille des données multipliée par leur poids, donc on doit déjà avoir le même nombres d'octets dans notre payload et dans l'exemple fourni. L'exemple fait 122 octets, et notre payload en fait pour le moment 40, donc il nous reste (122-40) caractères à ajouter.

#### Trouver les caractères à ajouter

En lisant la signature, on voit que la checksum vaut ```1235738```. En divisant par la taille (122), on a donc la somme nécessaire de nos données. Ici, ```10129```.
La somme actuelle de notre payload étant 3124, le nombre à ajouter restant est ```7005```.
En divisant cette valeur par le nombre de caractères qu'il nous reste à ajouter, on trouve ```7005//(122-40) = 85 ; 7005%(122-40) = 35```.
En reportant ces valeurs à leur code ASCII, on aboutit à la payload suivante :
```python
payload = b"a=open('flag.txt','r').read()\n\nprint(a)#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUx"
```
On reconstruit alors un fichier signé dont on envoie la base64 au serveur, et on obtient le flag : 404CTF{Th1s_Ch3cksum_W4s_Tr4sh}.

