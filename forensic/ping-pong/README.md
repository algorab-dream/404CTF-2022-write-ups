## Ping-pong

### Description

L'objectif est de retrouver des données exfiltrées via un échange ICMP.
En regardant les trames, on trouve effectivement des données qui sont des suites de caractères.
Néanmoins, après avoir tenté des les déchiffrer de multiples façons, il est clair que ce n'est pas la piste à suivre.

### Solution

En observant tous les champs des trames, on voit que la taille des données semble suspecte.
Une petite vérification avec tshark, en déchiffrant la taille des données comme des caractères ASCII :
```
n=`tshark -r ping.pcapng -Y "ip.src == 10.1.0.10" -T fields -e data.len`;awk 'BEGIN{FS=" "}{printf "%c\n",$0}' <<<$n | tr -d '\n'
```
On récupère alors le flag : 404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}.