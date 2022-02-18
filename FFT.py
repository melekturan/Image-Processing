from PIL import Image
import numpy as np
import cmath
import threading
from matplotlib import pyplot as plt
def Shift(newimage_shift, x, y, baz1mat, baz2mat, newimage_power):
     fft_shift=np.multiply(newimage_power,(np.multiply(baz1mat**x, baz2mat**y)))
     toplam_ifft=np.sum(fft_shift)
     newimage_shift[x][y]=abs(toplam_ifft)
def fft2(newimage, x, y, baz1mat, baz2mat, imagearray):
     fft=np.multiply(imagearray,(np.multiply(baz1mat**x, baz2mat**y)))
     toplam=np.sum(fft)
     newimage[x][y]=abs(toplam)
image = Image.open('orginal.png').convert('L')
imagearray= np.asarray(image)
newimage_power=np.zeros([512,512])
for x in range(0,512):
     for y in range(0,512):
        newimage_power[x][y]=imagearray[x][y]*((-1)**(x+y))
baz1mat= np.zeros((512,512),dtype=np.complex_)
baz2mat= np.zeros((512,512),dtype=np.complex_)
kombination=[]
fft_image=np.zeros([512,512])
fft_image_shift=np.zeros([512,512])
for u in range(0, 512):
     for v in range(0, 512):
         baz1 = cmath.exp((complex(0, 1) * 2 * cmath.pi * u) / -512)
         baz2 = cmath.exp((complex(0, 1) * 2 * cmath.pi * v) / -512)
         baz1mat[u][v]=baz1
         baz2mat[u][v]=baz2
         kombination.append([u,v])
for sayac in kombination[0:100]:
     x=sayac[0]
     y=sayac[1]
     a = threading.Thread(target=fft2, args=(fft_image, x, y, baz1mat, baz2mat,
    imagearray),daemon=True)
     b = threading.Thread(target=Shift, args=(fft_image_shift, x, y,baz2mat, baz2mat,
    newimage_power),daemon=True)
     a.start()
     b.start()
print(fft_image)
print(fft_image_shift)
fft = 20*np.log(np.abs(fft_image))
fft_shift = 20*np.log(np.abs(fft_image_shift))
plt.subplot(131),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(fft, cmap = 'gray')
plt.title('fft'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(fft_shift, cmap = 'gray')
plt.title('fft_shift'), plt.xticks([]), plt.yticks([])
plt.show()
