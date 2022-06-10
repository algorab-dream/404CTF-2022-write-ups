## La fonte des hashs

### Description

On récupère un code générant un hash, dont l'algorithme est dit "frileux" par l'énoncé.
On peut assez rapidement penser à un algorithme avec un faible entropie, autrement dit dont la sortie est fortement influencée par l'entrée.
On nous donne donne le hash du flag : ```18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205```, ainsi que le code permettant de hasher ce que l'on veut.

Dès lors, afin de tester l'hypothèse d'un hash "frileux", on peut essayer de hasher deux textes proches :
```bash
$ python3 ./hash.py 1234 && python3 ./hash.py 1235
c77b04f2186f967c636363636363636363636363636363636363636363636363
c77b046b96c5187c636363636363636363636363636363636363636363636363
```

On peut voir que les deux outputs sont très proches.
Un autre essai pour être sûr :
```bash
$ python3 ./hash.py 404CTF
18f2048f7d4d537da07c63636363636363636363636363636363636363636363
```

La début du hash correspond au début du hash du flag, plus de doute !

#### Exploit

A partir de là, on peut reconstruire le flag caractère par caractère en comparant les hashs obtenus;

```python
import os
import time
import sys

def distance(a,b):
    a = list(a)
    b = list(b)
    distance = len(a)
    for i in range(len(a)):
        if a[i] != b[i]:
            return distance
        distance -= 1
    return distance

def clean_dict(flag_dict):
    dict_return = {}
    max_length = len(list(flag_dict.keys())[-1])
    for flag in list(flag_dict.keys()):
        if len(flag) >= max_length:
            dict_return[flag] = flag_dict[flag]
    return dict_return

alphabet = list('azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890}')
hash_target = open('hash.txt','r').read()
flag_dict = {'404CTF{':os.popen('python3 ./hash.py 404CTF{').read()}

found = False
while True:
    for flag in list(flag_dict.keys()):
        flag_dict_ = {}
        for k in range(len(alphabet)):
            flag_ = flag + alphabet[k]
            print('Testing input : %s' % flag_,end='\r')
            hash_ = os.popen('python3 ./hash.py %s' % flag_).read()
            for i in range(len(hash_target)):
                if (list(hash_[:i]) == list(hash_target[:i])) and (list(hash_[:i]) != list(list(flag_dict.values())[-1][:i])):
                    flag_dict_[flag_] = hash_
                    break
        if flag_dict_:
            min_dist = distance(list(flag_dict_.values())[0],hash_target)
            for i in range(len(flag_dict_)):
                if distance(list(flag_dict_.values())[i],hash_target) <= min_dist:
                    min_dist = distance(list(flag_dict_.values())[i],hash_target)
                    flag_dict[list(flag_dict_.keys())[i]] = list(flag_dict_.values())[i]
                    if list(list(flag_dict_.values())[i])[-1] == '}':
                        print('Found : %s !' % list(flag_dict_.values())[i])
                        sys.exit(0)
    flag_dict = clean_dict(flag_dict)
```

On obtient le flag : 404CTF{yJ7dhDm35pLoJcbQkUygIJ}.
        