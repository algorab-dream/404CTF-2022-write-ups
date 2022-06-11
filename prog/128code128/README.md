## 128code128

### Description

On intéragit avec un serveur nous envoyant des images en base64, dont on doit tirer un mot de passe. Après avoir décodé la première image, on se retrouve face à un code barre. Le titre du challenge nous oriente directement vers le [code 128](https://fr.wikipedia.org/wiki/Code_128). A partir de là, il faut implémenter le déchiffrage et renvoyer le code obtenu pour chaque image.

### Solution

```python
import base64
from pwn import *
from PIL import Image
import numpy as np

alphabet = {'10011011100':'-', '10011101100':'0', '10011100110':'1', '11001110010':'2', '11001011100':'3', '11001001110':'4', '11011100100':'5',
'11001110100':'6', '11101101110':'7', '11101001100':'8', '11100101100':'9', '10100011000':'A', '10001011000':'B', '10001000110':'C', '10110001000':'D',
'10001101000':'E', '10001100010':'F', '11010001000':'G', '11000101000':'H', '11000100010':'I', '10110111000':'J', '10110001110':'K', '10001101110':'L',
'10111011000':'M', '10111000110':'N', '10001110110':'O', '11101110110':'P', '11010001110':'Q', '11000101110':'R', '11011101000':'S', '11011100010':'T',
'11011101110':'U', '11101011000':'V', '11101000110':'W', '11100010110':'X', '11101101000':'Y', '11101100010':'Z', '10100110000':'_', '10010110000':'a',
'10010000110':'b', '10000101100':'c', '10000100110':'d', '10110010000':'e', '10110000100':'f', '10011010000':'g', '10011000010':'h', '10000110100':'i',
'10000110010':'j', '11000010010':'k', '11001010000':'l', '11110111010':'m', '11000010100':'n', '10001111010':'o', '10100111100':'p', '10010111100':'q',
'10010011110':'r', '10111100100':'s', '10011110100':'t', '10011110010':'u', '11110100100':'v', '11110010100':'w', '11110010010':'x', '11011011110':'y', 
'11011110110':'z', '11110110110':'{', '10100011110':'}'}

conn = remote('challenge.404ctf.fr',30566)

def get_image():
    conn.recvline()
    image64=(conn.recvline())
    with open("128code128.png","wb") as f:
        f.write(base64.b64decode(image64))

def process_image():
    image = Image.open('128code128.png')
    image_array = np.asarray(image)
    line = image_array[0]
    bitstr = ""
    for pix in line:
        bitstr += str(((pix[0]//255)+1)%2)
    final_str = ""
    for i in range(0,len(bitstr)//11):
        try:
            final_str += alphabet[bitstr[i*11:(i+1)*11]]
        except:
            final_str += '*'
    conn.sendline(final_str.encode())

for i in range(128):
    get_image()
    process_image()
    conn.recvline()
conn.recvline()
print(conn.recvline())
```
On obtient le flag : 404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}.