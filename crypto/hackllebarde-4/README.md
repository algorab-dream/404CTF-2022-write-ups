## Hackllebarde Ransomware (4/4)

### Description

Nous sommes face à un document chiffré, avec le code source ayant permis de le chiffrer. 
Dans ce code, un élément est assez important, à savoir l'utilisation de la fonction ```rand()```, ainsi que cette de ```ìnitstate()```.
Ainsi, connaître la seed permet de retrouver la clé, et donc de déchiffrer le fichier !

### Exploit

Pas besoin d'être davantage intelligent, il s'agit maintenant de bruteforcer la seed.
Après un premier essai avec python, en faisant tourner le programme ```ransomware``` dans son ensemble et en regardant le header du fichier obtenu en sortie afin de vérifier s'il s'agit d'un PDF, on se rend vite compte que cette méthode est trop lente.
On passe donc en C, où l'on recopie presque le code du ransomware :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
    int seed = 0;
    char array[8];
 	initstate(seed, array, 27);

    char pdf[4] = {0x25, 0x50, 0x44, 0x46}; /*Magic Bytes PDF*/
    char crypt[4] = {0x69, 0x12, 0xd1, 0x32}; /*4 premiers octets du fichier chiffré*/

    int key;
    char temp[4];
    char* keychar;

    while((memcmp(&temp,&pdf,4))) {
        seed++;
        initstate(seed, array, 27);
        key = rand();
        keychar = (char*)&key;
        memcpy(&temp,crypt,4);
        for(int i=0; i<4; i++) {
			temp[i] ^= keychar[i];
		}
    }
    printf("seed found = %d\n",seed);
}
```

On retrouve assez rapidement la seed, qui vaut ```270701183```, et ainsi on peut simplement déchiffrer le PDF et obtenir le flag : 404CTF{W0w_p4s_Tr3S_r4nD0m_T0ut_c4}.

