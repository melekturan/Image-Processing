from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def histogram_ciz(graph):
     plt.bar([p for p in range(0, 256)], graph, color='blue')
     plt.show()
def hist_esitleme(histogram_array,last_image2,name):
     histogram_cizim = []
     histogram_listt2=[]
     degerler = (histogram_array / np.sum(histogram_array))
     for j in range(0, 256):
         a = np.sum(degerler[0:j])
         histogram_cizim.append(int(a * 255)) # yeni değerler
     for p in range(0,750):
         for p1 in range(0,750):
             last_image2[p,p1]=histogram_cizim[last_image2[p,p1]]
     Image.fromarray(last_image2).save(name + '1.png')
     for k in range(0, 256):
        histogram_listt2.append(np.count_nonzero(last_image2 == k))
     histogram_array2 = np.asarray(histogram_listt2) # resme ait histogram degerleri
     histogram_ciz(histogram_array2)
def low(imagearray,name):
     histogram_listt3=[]
     low_cont=(imagearray/6)+125
     last_image3 = np.array(low_cont,dtype=np.uint8)
     for k in range(0, 256):
        histogram_listt3.append(np.count_nonzero(last_image3 == k))
     histogram_array3=np.asarray(histogram_listt3) #resme ait histogram degerleri
     histogram_ciz(histogram_array3)
     Image.fromarray(last_image3).save(name + '.png')
     hist_esitleme(histogram_array3,last_image3,name)
def gama(imagearray,L,x,name):
     histogram_listt=[]
     gama_image=(((imagearray/(L-1)))**x)*255
     last_image = np.array(gama_image,dtype=np.uint8)
     for k in range(0, 256):
         histogram_listt.append(np.count_nonzero(last_image == k))
         histogram_array=np.asarray(histogram_listt) #resme ait histogram degerleri
         histogram_ciz(histogram_array)
         Image.fromarray(last_image).save(name + '.png')
         hist_esitleme(histogram_array,last_image,name)
hist_list=[]
Control_list=[]
image = Image.open('kalemler.jpg').convert('L')
imagearray= np.asarray(image)
Image.fromarray(imagearray).save('org_gs' + '.png')
for k in imagearray:
     for l in k:
        Control_list.append(l)
L=256
array_list=np.asarray(Control_list)
for k in range(0,256):
    hist_list.append(np.count_nonzero(array_list == k))
histogram_ciz(hist_list)
gama(imagearray,L,0.2,'acık')
gama(imagearray,L,3.0,'koyu')
low(imagearray,'low')