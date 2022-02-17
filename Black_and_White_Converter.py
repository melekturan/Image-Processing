from PIL import Image
from numpy import asarray
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
def histogram_ciz(graph):
     fig, ax = plt.subplots(1, 1)
     ax.hist(graph, bins=[i for i in range(0, 256)])
     ax.set_title("histogram of result")
     ax.set_xticks([i for i in range(0, 256, 16)])
     plt.show()
def th(Threshold_list,name):
     an_array = np.where(Threshold_list>127,255, Threshold_list)
     an_array = np.where(an_array < 127, 0, an_array)
     ciz=np.array(an_array)
     Image.fromarray(ciz).save(name+ '.png')
def ortalama(imarray_list,liste,name):
     toplam=liste.sum()
     list_len=len(liste)
     ort=toplam/list_len
     print(ort)
     an_array = np.where(imarray_list > int(ort), 255, imarray_list)
     an_array = np.where(an_array < int(ort), 0, an_array)
     ciz = np.array(an_array)
     Image.fromarray(ciz).save(name + '.png')
def median(imarray_list1,name):
     medyan=np.median(imarray_list1)
     an_array1 = np.where(imarray_list1 > int(medyan), 255, imarray_list1)
     an_array1 = np.where(an_array1 < int(medyan), 0, an_array1)
     ciz = np.array(an_array1)
     Image.fromarray(ciz).save(name + '.png')
Control_list=[]
Control_list2=[]
matrix=[]
image = Image.open('aydinlik.jpg').convert('L')
image2 = Image.open('karanlık.jpg').convert('L')
aydinlik = np.asarray(image)
karanlik= np.asarray(image2)
for k in aydinlik:
     for l in k:
         Control_list.append(l)
for j in karanlik:
     for z in j:
         Control_list2.append(z)
aydinlik_list=np.asarray(Control_list)
karanlik_list=np.asarray(Control_list2)
histogram_ciz(aydinlik_list)
histogram_ciz(karanlik_list)
th(karanlik,'th_karanlik')
th(aydinlik,'th_aydinlik')
ortalama(karanlik,karanlik_list,'ort_karanlik')
ortalama(aydinlik,aydinlik_list,'ort_aydinlik')
median(karanlik,'median_karanlik')
median(aydinlik,'median_aydinlik')