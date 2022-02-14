from PIL import Image
from numpy import asarray
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
def dac(g,k):
    quantize= g * (k + 0.5)
    quantize = np.array(quantize, dtype=np.int)
    print(quantize.max(),quantize.min())
    Image.fromarray(quantize*255).save('quant'+str(g)+'.png')
def bit(orig,delta):
    p = orig / delta
    k = np.round(p, 0)
    int_array =np.array(k, dtype=np.int)
    if int_array.max()==1:
        dac(128,int_array)
    if int_array.max()==3:
        dac(64, int_array)
    if int_array.max()==7:
        dac(32, int_array)
    if int_array.max()==15:
        dac(16, int_array)
    if int_array.max()==31:
        dac(8, int_array)
    if int_array.max()==63:
        dac(4, int_array)
    if int_array.max()==127:
        dac(2, int_array)
    plt.imshow(k, cmap='gray')
    plt.imsave('bit'+str(int(k.max())+1)+'.jpg', k,cmap='gray')
image = Image.open('tesla.jpg').convert('L')
orig = np.asarray(image)
for NoBits in range(1,9):
    L=(2**NoBits)-1
    delta=orig.max()/L
    bit(orig,delta)