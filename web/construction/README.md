## En construction

### Description

On se retrouve sur un site explicitement dit en construction, avec une page d'accueil, une page admin sans grand intérêt et a priori une page 1, et une page 2.
On peut assez rapidement remarquer qu'il est possible d'obtenir la page N, avec N un entier relatif.

### Exploit

Après avoir cherché des chemins cachés, des moyens de faire du Directory Traversal et autre, on en revient à nos fondamentaux et on regarde plus précisément les réponses des requêtes pour les pages N. On voit alors que le code de réponse varie, ce qui est assez étrange. Peut-être que le flag se cache là ? Un script python pour vérifier ça donne :
```python
import requests

url = "https://en-construction.404ctf.fr/page/%s"

retour = ""

for i in range(3,334):
    r = requests.get(url % i)
    retour += str(r.status_code)[1:]
print(retour)
```

En le [décodant](https://www.dcode.fr/code-ascii) correctement, on retrouve le flag : 404CTF{Dr0l3_D3_m0Y3N_d3_f41r3_P4sS3r_d3S_d0nN33s_n0N?}.