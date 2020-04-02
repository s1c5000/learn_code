import PIL.Image as pilimg
import numpy as np
 
# Read image
im = pilimg.open( 'C:/Users/LEEMINJUN/python_study/TensorFlow_Machine_Learning/8.png' )
 
# Display image
#im.show()
 
# Fetch image pixel data to numpy array
#pix = np.array(im)
pix = np.array(im, ndmin=1)
#pix.reshape(1,784)
print(pix.size)
print(pix.shape)
print(3136/4)
print(12*9)
print(pix)