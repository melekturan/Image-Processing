
from PIL import Image
from numpy import asarray
import numpy as np

def varyans(filtersize,zero_add_image,newimage,newimage_var):
    for a in range(0, 512):
        for b in range(0, 512):
            toplam2 = 0
            for v in range(0, filtersize):
                for v1 in range(0, filtersize):
                    toplam2=toplam2+((zero_add_image[a + v][b + v1]-newimage[a,b])**2)

            newimage_var[a][b]=int(toplam2/(filtersize**2-1))
    var_im = np.asarray(newimage_var, dtype=np.uint8)
    Image.fromarray(var_im).save(str(filtersize) + 'var.png')

def save_func(m_image,name):
    Image.fromarray(m_image).save(name + '.png')


def mean_image(k,l,toplam1,newimage,filtersize):
    newimage[k][l]=int(toplam1/filtersize**2)

def filtre(k,l,image_,new_image,filtersize):
    toplam1=0
    for f in range(0,filtersize):
        for f1 in range(0,filtersize):
            toplam1=toplam1+image_[k+f][l+f1]

    mean_image(k,l,toplam1,new_image,filtersize)

def image_coloumn_row(zero_add_image,newimage,filtersize):
    for i in range(0, 512):
        for j in range(0, 512):
            filtre(i, j, zero_add_image, newimage,filtersize)



image = Image.open('resim1.jpg').convert('L')
imagearray= np.asarray(image)
print(imagearray)
Image.fromarray(imagearray).save('orginal'+ '.png')


newimage=np.zeros([512,512])#0'dan oluşan 512*512 matris daha sonra değerleri güncellenecek
newimage_var=np.zeros([512,512])#0'dan oluşan 512*512 matris daha sonra değerleri güncellenecek

for filtersize in [3,9,15]:
    padd=int((filtersize-1)/2)# kaç sıra 0 ekleneceğini hesaplama
    zero_add_image = np.pad(imagearray, ((padd, padd), (padd, padd)), 'constant')  # matris etrafına 0 ekleme
    image_coloumn_row(zero_add_image,newimage,filtersize)
    m_image = np.asarray(newimage, dtype=np.uint8)
    save_func(m_image,'filter'+str(filtersize))#bulanıklaştırılmış görsellerin kaydedilmesi

    varyans(filtersize,zero_add_image,newimage,newimage_var)

