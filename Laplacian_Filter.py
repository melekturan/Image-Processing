
from PIL import Image
from numpy import asarray
import numpy as np
import  math
import cv2

def save_func(m_image,name):
    Image.fromarray(m_image).save(name + '.png')


def sonuc(k,l,toplam,newimage):
    newimage[k][l]=int(toplam)


def filtre(i,j,image_,new_image,filter_matrix):
    toplam=0
    for f in range(0,3):
        for f1 in range(0,3):

            toplam=toplam+image_[i+f][j+f1]*filter_matrix[f][f1]

    sonuc(i,j,toplam,new_image)

def image_coloumn_row(zero_add_image,newimage,filter_matrix):
    for i in range(0, 512):
        for j in range(0, 512):
            filtre(i, j, zero_add_image, newimage,filter_matrix)


imagelist=[]
image = Image.open('lunapark.jpg').convert('L')
imagearray= np.asarray(image)

newimage=np.zeros([512,512])
newimage1=np.zeros([512,512])
newimage2=np.zeros([512,512])


Laplace=np.asarray([[0,1,0],[1,-4,1],[0,1,0]])

matrix__90=np.asarray([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
matrix__45=np.asarray([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])


zero_add_image = np.pad(imagearray, ((1, 1), (1, 1)), 'constant')

image_coloumn_row(zero_add_image,newimage,Laplace)
image_coloumn_row(zero_add_image,newimage1,matrix__90)
image_coloumn_row(zero_add_image,newimage2,matrix__45)

an_array = np.where(newimage < 0, 0, newimage)
Laplace_ = np.asarray(an_array, dtype=np.uint8)

an_array1 = np.where(newimage1 < 0, 0, newimage1)
an_array1 = np.where(an_array1 > 255, 255, an_array1)
print(an_array1)
__90 = np.asarray(an_array1, dtype=np.uint8)


an_array2 = np.where(newimage2 < 0, 0, newimage2)
an_array2 = np.where(an_array2 > 255, 255, an_array2)
__45 = np.asarray(an_array2, dtype=np.uint8)


save_func(Laplace_,'laplace')
save_func(__45,'keskinlestirme_45')
save_func(__90,'keskinlestirme_90')
save_func(img,'dene')
#
#
