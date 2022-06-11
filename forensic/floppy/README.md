## Floppy

### Description

On nous fournit une image disque à déchiffrer. 
Voyons un peu plus en détail ce dont il s'agit : 
```
$ file floppy.img
floppy.img: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "MSDOS5.0", root entries 224, sectors 2880 (volumes <=32 MB), sectors/FAT 9, sectors/track 18, reserved 0x1, serial number 0x1eeb92d8, unlabeled, FAT (12 bit), followed by FAT

$ binwalk floppy.img
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
17408         0x4400          JPEG image data, JFIF standard 1.01
88576         0x15A00         JPEG image data, JFIF standard 1.01
138240        0x21C00         JPEG image data, JFIF standard 1.01
150528        0x24C00         JPEG image data, JFIF standard 1.01
219136        0x35800         JPEG image data, JFIF standard 1.01

$ strings -n 10 floppy.img
NO NAME    FAT12   3
BOOTMGR
Retirez le disque
Err. disque
Pressez une touche pour red
IMG_0001JPG
IMG_0002JPG
MG_0003JPG
IMG_0004JPG
IMG_0005JPG
RASH-~1
$4.763.22:ASF:=N>22HbINVX]^]8EfmeZlS[]Y
*Y;2;YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
C!YVm(huE%
4&3V8eS2Mk
Hr%&)35g'u>22c
5)9i%&mHqh
gdGXroU 1P-LWe
N,l=b#jyn*K<
$4.763.22:ASF:=N>22HbINVX]^]8EfmeZlS[]Y
*Y;2;YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
4x6*B4e`oD
FHO,2YO0Tiq
$4.763.22:ASF:=N>22HbINVX]^]8EfmeZlS[]Y
*Y;2;YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
!1 AQ0@aq`
$4.763.22:ASF:=N>22HbINVX]^]8EfmeZlS[]Y
*Y;2;YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
45eq\SI>#&TfJ
xt24i"}$(e
}E;y1b\V2*
CNEBv`T5\N
8Bj!rPopTv.
tR~BYbT,_3j
'vry}*r(IK
.
..
MG_0003JPG
[Trash Info]
Path=IMG_0003.jpg
DeletionDate=2022-05-07T05:02:38
[Trash Info]
Path=.Trash-1000
DeletionDate=2022-05-07T05:02:58
```
Il s'agit donc d'une image disque MS/DOS, qui semble contenir 4 images. De plus, l'image ``IMG_0003.jpg`` semble avoir été supprimée.

### Récupération des images

En utilisant l'outil ``foremost``, on peut récupérer les 4 images :
```
$ foremost floppy.img

$ ls output
audit.txt  jpg

$ ls output/jpg
00000034.jpg  00000173.jpg  00000270.jpg  00000294.jpg  00000428.jpg
```
On retrouve le flag dans l'une des images : 404CTF{@v3z_v0vz_z0rt1_135_p0ub3ll35}.
