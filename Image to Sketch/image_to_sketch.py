import numpy as np
import cv2
import imageio
from scipy.ndimage import gaussian_filter
img = 'images/demo.jpg'

# def greyscale(rgb):
#     image = cv2.imread(img)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def greyscale(rgb):
    return np.dot(rgb[...,:3],[0.3,0.6,0.1])

def dodge(front,back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

i = imageio.imread(img)

g = greyscale(i)

s = 255-g

b = gaussian_filter(s,sigma=10)

r = dodge(b,g)

cv2.imwrite('images/sketch.png',r)