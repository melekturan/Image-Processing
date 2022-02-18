import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from PIL import Image
img = cv2.imread('orginal.png',0)
G_zero=np.zeros([512,512])
fftshift=np.fft.fftshift(np.fft.fft2(img))
H=np.zeros([512,512])
M=512
N=512
Do_list=[0.05*(M/2),0.1*(M/2),0.2*(M/2),0.5*(M/2),0.9*(M/2)]
sayac=150
for Do in Do_list:
     sayac = sayac + 1
     for u in range(0,512):
         for v in range(0,512):
             islem=(u-(M/2))**2+(v-(N/2))**2
             D_uv=math.sqrt(islem)
             H[u][v]=1/(1+((D_uv/Do)**4))
     print(H)
     G=H*fftshift
     g=np.fft.ifft2(G)
     g=abs(g)
     for a in range(0,512):
         for b in range(0,512):
              G_zero[a][b] = g[a][b] * ((-1) ** (a + b))
     g=abs(G_zero)
     plt.subplot(sayac), plt.imshow(g, cmap='gray')
     plt.title(str(Do)), plt.xticks([]), plt.yticks([])
plt.show()
