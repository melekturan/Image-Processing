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
def gama(imagearray,L,x,name):
     new_list=[]
     gama_image=(((imagearray/(L-1)))**x)*255
     ciz = np.array(gama_image,dtype=np.int)
     for c in ciz:
        for c1 in c:
             new_list.append(c1)
     histogram_ciz(new_list)
     Image.fromarray(ciz*255).save(name + '.png')
Control_list=[]
image = Image.open('renk.jpg').convert('L')
imagearray= np.asarray(image)
Image.fromarray(imagearray).save('org_gs' + '.png')
for k in imagearray:
     for l in k:
         Control_list.append(l)
L=256
array_list=np.asarray(Control_list)
histogram_ciz(array_list)
gama(imagearray,L,0.5,'acık')
gama(imagearray,L,2.0,'koyu')
