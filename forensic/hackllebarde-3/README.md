## Hackllebarde Ransomware (3/4)

### Crackage du ZIP

Un dump de clé USB nous est fourni. En utilisant ```binwalk```, ```foremost```, Autopsy ou autre, on en extrait 4 images de chats et une archive ZIP chiffrée.
On peut la cracker avec ```hashcat```, ou encore ```john``` :

```bash
$ zip2john archive.zip > archive.hash && john archive.hash --wordlist=rockyou.txt
```

On trouve alors le mot de passe ```agentkitty```, qui nous permet d'extraire un fichier keepass du zip.

### Crackage du KeePass

En premier lieu, il serait tentant de simplement réitérer le processus, en remplaçant ```zip2john``` par ```keepass2john```. Cependant, ça ne donne rien de concluant. Il faut en effet penser au fait qu'un KeePass peut être chiffré à l'aide d'un mot de passe accompagné d'un fichier, appelé KeyFile.
On essaye alors de générer 4 hashs, avec les 4 images trouvées dans l'image de la clé :

```bash
$ keepass2john -k img1.jpg stockage.kdbx | sed 's/^[^:]*://' > hash1 && keepass2john -k img2.jpg stockage.kdbx | sed 's/^[^:]*://' > hash2 && keepass2john -k img3.jpg stockage.kdbx | sed 's/^[^:]*://' > hash3 && keepass2john -k img4.jpg stockage.kdbx | sed 's/^[^:]*://' > hash4
```

On peut ensuite essayer de lancer john avec rockyou, mais ça ne fonctionne pas. On essaye alors :

```bash
$ echo agentkitty > wordlist ; john hash* --wordlist=wordlist --rules
``` 

On trouve alors comme mot de passe ```Agentkitty```.

### Retrouver le flag

Une fois dans l'archive, on lance une grande recherche sur l'ensemble des champs, et on finit par retrouver le flag dans les anciens mots de passes d'un des utilisateurs.
Le flag est 404CTF{D3l3t1nG_4nD_P4sSw0Rds_n0T_3N0UgH}.