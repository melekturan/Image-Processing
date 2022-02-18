from PIL import Image
import numpy as np
import cmath
import threading
from matplotlib import pyplot as plt
def Shift(newimage_ifft_shift, x, y, baz1mat, baz2mat, newimage_power,Bir_bolu_MN):
     ifft_shift=(np.multiply(newimage_power,(np.multiply(baz1mat**x,
    baz2mat**y))))*Bir_bolu_MN
     toplam_ifft_shift=np.sum(ifft_shift)
     newimage_ifft_shift[x][y]=abs(toplam_ifft_shift)
def ifft2(newimage_ifft, x, y, baz1mat, baz2mat, imagearray,Bir_bolu_MN):
     ifft=(np.multiply(imagearray,(np.multiply(baz1mat**x, baz2mat**y))))*Bir_bolu_MN
     toplam_shift=np.sum(ifft)
     newimage_ifft[x][y]=abs(toplam_shift)
image = Image.open('orginal.png').convert('L')
imagearray= np.asarray(image)
newimage_power=np.zeros([512,512])
for x in range(0,512):
     for y in range(0,512):
         newimage_power[x][y]=imagearray[x][y]*((-1)**(x+y))
baz1mat= np.zeros((512,512),dtype=np.complex_)
baz2mat= np.zeros((512,512),dtype=np.complex_)
kombination=[]
newimage_ifft=np.zeros([512,512])
newimage_ifft_shift=np.zeros([512,512])
for u in range(0, 512):
     for v in range(0, 512):
         baz1 = cmath.exp((complex(0, 1) * 2 * cmath.pi * u) / 512)
         baz2 = cmath.exp((complex(0, 1) * 2 * cmath.pi * v) / 512)
         baz1mat[u][v]=baz1
         baz2mat[u][v]=baz2
         kombination.append([u,v])
Bir_bolu_MN = 1 / (512 * 512)
for sayac in kombination:
     x=sayac[0]
     y=sayac[1]
     a = threading.Thread(target=ifft2, args=(newimage_ifft, x, y, baz1mat, baz2mat,
    imagearray,Bir_bolu_MN),daemon=True)
     b = threading.Thread(target=Shift, args=(newimage_ifft_shift, x, y,baz1mat, baz2mat,
    newimage_power,Bir_bolu_MN),daemon=True)
     a.start()
     b.start()
print(newimage_ifft)
print(newimage_ifft_shift)
ifft= 20*np.log(np.abs(newimage_ifft))
ifft_shift= 20*np.log(np.abs(newimage_ifft_shift))
plt.subplot(131),plt.imshow(image, cmap = 'gray')
plt.title('image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(ifft, cmap = 'gray')
plt.title('ifft'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(ifft_shift, cmap = 'gray')
plt.title('ifft_shift'), plt.xticks([]), plt.yticks([])
plt.show()