from pytesseract import *
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import matplotlib
#reading the image
str=raw_input("Enter the image ")
img0=cv2.imread(str)

#Creating a copy of the original
img=img0.copy()

#converting to grayscale
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
img2 = cv2.threshold(img1, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
img2 = cv2.bitwise_not(img2)
#iff there is inclination of the text then rectifying it
coords = np.column_stack(np.where(img2 > 0))

#measuring angle
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle

#rotating image to vertical position
(h, w) = img0.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
img3 = cv2.warpAffine(img2, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('test001.png',img3)
#end of opencv operations

#starting PIL operations
im=Image.open('test001.png')

#MedianFilter eliminates noise
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(3)
im = im.convert('1')
im.save('test001.png')

#image to text
text = pytesseract.image_to_string(Image.open('test001.png'))
print(text)
