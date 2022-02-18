
from PIL import Image
from numpy import asarray
import numpy as np
import  math

def save_func(m_image,name):
    Image.fromarray(m_image).save(name + '.png')

def gradient(Gx,Gy):
    print(Gx)
    print(Gx**2)
    gradient_image=(Gx**2+Gy**2)**0.5
    print(gradient_image)
    gradient_image_ = np.asarray(gradient_image, dtype=np.uint8)
    save_func(gradient_image_, 'gradient_image')


def sonuc(k,l,toplam,newimage):
    newimage[k][l]=int(toplam)


def filtre(i,j,image_,new_image,filter_matrix):
    toplam=0
    for f in range(0,3):
        for f1 in range(0,3):

            toplam=toplam+image_[i+f][j+f1]*filter_matrix[f][f1]

    sonuc(i,j,toplam,new_image)

def image_coloumn_row(zero_add_image,newimage,filter_matrix):
    for i in range(0, 749):
        for j in range(0, 749):
            filtre(i, j, zero_add_image, newimage,filter_matrix)


imagelist=[]
image = Image.open('satranç.png').convert('L')
imagearray= np.asarray(image)

newimage=np.zeros([749,749])
newimage1=np.zeros([749,749])


Gx_filter_matrix=np.asarray([[0,0,0],[-1,0,1],[0,0,0]])
Gy_filter_matrix=np.asarray([[0,-1,0],[0,0,0],[0,1,0]])



zero_add_image = np.pad(imagearray, ((1, 1), (1, 1)), 'constant')


image_coloumn_row(zero_add_image,newimage,Gx_filter_matrix)
image_coloumn_row(zero_add_image,newimage1,Gy_filter_matrix)


Gx = np.asarray(newimage, dtype=np.uint8)
Gy = np.asarray(newimage1, dtype=np.uint8)

save_func(Gx,'gx')
save_func(Gy,'gy')
gradient(newimage, newimage1)







