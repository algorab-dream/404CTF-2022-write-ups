## GoGOLFPlex

### Description

On se retrouve face à un script python qui nous met au défi de trouver un moyen de finir un parcours de golf en moins de 10^25 coups.
La partie intéressante du script se situe ici :
```python
a = input('En combien de coups essayez-vous de faire le parcours?\n').strip()

try:

    if a[0] in '-+0':
        print('Opération interdite! Je ne vais pas me faire avoir comme ça! Je ne suis pas un débutant!')
        exit()
    nb = int(f'{a:<051}')
        print(f'vous réussissez à finir le parcours en {nb} coups')
        if nb <= 10**25:
            with open('flag.txt', 'r') as f:
                print(f.readline())
            exit()
```
Impossible ici de mettre des espaces pour meubler, ou de mettre un 0, un - ou un + au début. De plus, la ligne ``nb = int(f'{a:<051}')`` vient rajouter des 0 à notre nombre jusqu'à ce la chaîne de caractères fasse 51 caractères de long.

### Exploit

En se renseignant sur le type ``int``, on découvre que ``1_0`` est un ``int`` en python qui vaut 10. Dès lors, on a notre caractère 'vide' et on peut donner au programme ``1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0``.
On obtient alors le flag : 404CTF{Und3r5c0r35_1n_1nt3g3r5??}.
