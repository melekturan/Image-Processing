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
def lowcontrast(x,x1,x2,y1,y2,name):
     new_list=[]
     lowimage=(((x-x1)/(x2-x1))*(y2-y1))+y1
     highimage = np.array(lowimage,dtype=np.int)
     print(highimage)
     for c in highimage:
        for c1 in c:
            new_list.append(c1)
     histogram_ciz(new_list)
     Image.fromarray(highimage*255).save(name + '.png')
Control_list=[]
image = Image.open('lowcont.jpg').convert('L')
imagearray= np.asarray(image)
Image.fromarray(imagearray).save('lowcont' + '.png')
for k in imagearray:
     for l in k:
        Control_list.append(l)
array_list=np.asarray(Control_list)
histogram_ciz(array_list)
lowcontrast(imagearray,imagearray.min(),imagearray.max(),0,255,'highcont')