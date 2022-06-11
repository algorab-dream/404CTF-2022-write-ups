## Un agent compromis (3/3)

### Description

Après avoir reconstitué les fichiers, il faut retrouver le flag. Nous avons à notre disposition 3 fichiers, le flag étant contenu dans le PDF. 
En ouvrant le PDF, on ne voit qu'une page blanche. On en déduit donc qu'il faut réparer le fichier, pour pouvoir accéder à son contenu.

### Solution

Il faut mettre les mains dans le cambouis.
En ouvrant le PDF, on remarque quelques étrangetés :
```
10 0 obj
<</F1 911 0 obj
<</Font 10 0 R
/ProcSet[/PDF/Text]
>>
endobj
```
```
xref
0 14
0000000000 65535 f
0000008983 00000 n
0000000019 00000 n
0000000252 00000 n
0000009152 00000 n
0000000272 00000 n
0000008026 00000 n
0000008047 00000 n
0000008237 00000 n
0000008640 00000 n
0000008896 928 00000 n
0000009251 00000 n
0000009348 00000 n
trailer
```
Deux choses interpellent ici. L'objet 10 n'est pas terminé, et l'objet 11 commence en plein milieu de celui-ci. De plus, une ``928`` s'est glissé dans le ``xref``, que l'on doit retirer. Les deux parties deffectueuses corrigées donnent :
```
10 0 obj
<</F1 9 0 R
>>
endobj

11 0 obj
<</Font 10 0 R
/ProcSet[/PDF/Text]
>>
endobj
```
```
xref
0 14
0000000000 65535 f
0000008983 00000 n
0000000019 00000 n
0000000252 00000 n
0000009152 00000 n
0000000272 00000 n
0000008026 00000 n
0000008047 00000 n
0000008237 00000 n
0000008640 00000 n
0000008896 00000 n
0000009251 00000 n
0000009348 00000 n
trailer
```
En rouvrant le PDF, on obtient alors le flag : 404CTF{DNS_3xf1ltr4t10n_hallebarde}.