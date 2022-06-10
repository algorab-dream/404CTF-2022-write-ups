## Du Gâteau

### Description

On arrive sur un site implémentant un système d'authentification sans base de donnée. D'après le site, ce système pourrait présenter quelques bugs. A nous de les chercher, donc.
Une fois connecté, on remarque l'apparition d'un cookie dont le contenu est le base64 de la chaîne de caractères suivante :
```username=username;password=sha512(password)```
L'username est donc stocké en clair, tandis que le mot de passe est hashé dans le cookie.
On a également une page de changement de mot de passe, dont l'url est déterminée par le nom d'utilisateur choisi, et où le hash est stocké en clair dans la page.
Pour accéder à la page d'admin, il nous suffit d'avoir le hash du mot de passe de l'admin, puisqu'on peut choisir son username et son password à loisir en modifiant le cookie.
On peut donc essayer de changer son username en admin, et d'aller dans la page de changement de mot de passe. Seulement ça ne fonctionne pas, on dirait que le site ne veut pas nous laisser jouer avec les logs de l'admin aussi facilement.

### Exploit

Il faut donc réfléchir, en imaginant comment le système aurait pu être mal codé. Après de nombreux essais (LFI, Directory Traversal, XSS etc), on finit par essayer de jouer avec le cookie.
En essayant de ne pas mettre de mot de passe, pas d'username, et autre sournoiseries, on finit par trouver un moyen d'accéder à la page de changement de mot de passe admin. Le cookie ressemble alors à ça :
```
username=foo;username=admin;password=e05af1399f4f4beb7934c9f12ba5a9c88f7ee1e8ef3fe7a167be4b979c515d24102ad90d3a0754d48fc5930f6369a3087e686e9732ef3460e6439a95089b4800
```
Cela nous permet d'arriver à la page de modification du mot de passe admin, où l'on peut récupérer son hash : ```66651013935b4c2c31d9baba8fa5d37b809b10da453f293ec8f9a7fbb2ab2e2c1d69dc8d80969508028b5ec14e9d1de585929a4c0d534996744b495c325e3f3d```, et ainsi reconstituer un cookie :
```
username=admin;password=66651013935b4c2c31d9baba8fa5d37b809b10da453f293ec8f9a7fbb2ab2e2c1d69dc8d80969508028b5ec14e9d1de585929a4c0d534996744b495c325e3f3d
```
On obtient ainsi la chaîne ```dXNlcm5hbWU9YWRtaW47cGFzc3dvcmQ9NjY2NTEwMTM5MzViNGMyYzMxZDliYWJhOGZhNWQzN2I4MDliMTBkYTQ1M2YyOTNlYzhmOWE3ZmJiMmFiMmUyYzFkNjlkYzhkODA5Njk1MDgwMjhiNWVjMTRlOWQxZGU1ODU5MjlhNGMwZDUzNDk5Njc0NGI0OTVjMzI1ZTNmM2Q=``` pour le cookie.
En accédant à la page ```/admin``` avec ce cookie, encore un problème, le cookie _exact_ de l'admin a été révoqué. Aucun soucis, car on connaît bien sa [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648), donc le cookie devient par exemple : ```dXNlcm5hbWU9YWRtaW47cGFzc3dvcmQ9NjY2NTEwMTM5MzViNGMyYzMxZDliYWJhOGZhNWQzN2I4MDliMTBkYTQ1M2YyOTNlYzhmOWE3ZmJiMmFiMmUyYzFkNjlkYzhkODA5Njk1MDgwMjhiNWVjMTRlOWQxZGU1ODU5MjlhNGMwZDUzNDk5Njc0NGI0OTVjMzI1ZTNmM2R=```

On obtient alors le flag : 404CTF{m3f13Z_V0Us_D3s_MdP_D4nS_L3s_c00k13s!}.

