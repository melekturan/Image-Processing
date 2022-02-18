from PIL import Image
from numpy import asarray
import numpy as np
import math
def result(save_image,error2,error,k,std_sapma): #Cevap 5.2
     mae=error.sum()/(512*512)
     mse = error2.sum() / (512 * 512)
     psnr = 10 * math.log10((255 ** 2) / mse)
     print(psnr,mae)
     Image.fromarray(save_image).save(str(k) + 'adet' + str(std_sapma) + '.png')
def gurultu(varyans,size,X): #Cevap 5.1
     std_sapma = int(varyans ** 0.5)
     print(std_sapma)
     for k in [1,5, 10, 50, 100]:
         Y = 0
     for i in range(k):
         N = std_sapma * np.random.randn(size[0], size[1])
         Y = Y + (X + N)
     save_image = np.asarray(Y / k, dtype=np.uint8)
     error=abs(X-(Y/k))
     error2=(X-(Y/k))**2
     result(save_image,error2,error,k,std_sapma)
image = Image.open('lunapark.jpg').convert('L')
X= np.asarray(image)
print(X)
Image.fromarray(X).save('orginal'+ '.png')
size=X.shape
gurultu(100,size,X)
gurultu(400,size,X)