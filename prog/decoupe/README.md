## Découpé

### Description

On se retrouve avec un grand nombres d'images, toutes carrées, chacune consituées uniquement de pixels blancs et noirs.
On remarque qu'on a 576 images, soit 24^2 images. Au vu du titre et de cette donnéés, on peut imaginer qu'il faille reconstituer une image carrée de 24 sous-images par 24 sous-images.

### Script

On recolle les images dans l'ordre, de gauche à droite et de haut en bas :

```python
import numpy as np
import PIL
from PIL import Image


lines = []
line = []
for i in range(1,577):
    line.append(f'{i}.png')
    if i%24 == 0:
        lines.append(line)
        line = []
im_list = []
for line in lines:
    imgs = [Image.open(i) for i in line]
    imgs_comb = np.hstack((np.asarray(i) for i in imgs))
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(f'{lines.index(line)}_vert.png')   
    im_list.append(f'{lines.index(line)}_vert.png') 

imgs = [Image.open(i) for i in im_list]
imgs_comb = np.vstack((np.asarray(i) for i in imgs))
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('recole.jpg')
```

Cela nous donne un QRCode, dont la valeur est le flag : 404CTF{M4n1PuL4T10N_d'1M4g3S_F4c1L3_n0N?}.

