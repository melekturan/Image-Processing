from PIL import Image
from numpy import asarray
import numpy as np
def bitduzlemi(image,bol,name):
     image1 = (image / bol)
     image1 = np.asarray(image1, dtype=np.uint8)
     print(image1.max())
     ciz2 = image1 % 2
     an_array = np.where(ciz2 == 0, 0, ciz2)
     an_array = np.where(an_array == 1, 255, an_array)
     Image.fromarray(an_array).save(name + '.png')
image = Image.open('manzara.jpg').convert('L')
imagearray= np.asarray(image)
Image.fromarray(imagearray).save('orginal'+ '.png')
bitduzlemi(imagearray,2,'1bit')
bitduzlemi(imagearray,4,'2bit')
bitduzlemi(imagearray,8,'3bit')
bitduzlemi(imagearray,16,'4bit')
bitduzlemi(imagearray,32,'5bit')
bitduzlemi(imagearray,64,'6bit')
bitduzlemi(imagearray,128,'7bit')