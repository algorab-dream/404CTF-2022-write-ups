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