from pytesseract import *
import sys
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import os
#from scipy import imread, imsave, imresize
import numpy as np
import webbrowser
import matplotlib

#checking whether image is coloured or grayscale
def is_grey_scale(img_path):
    im = Image.open(img_path).convert('RGB')
    w,h = im.size
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            if r != g != b: return False
    return True


#reading the image
str=raw_input("Enter the image ")
img0=cv2.imread(str)

#maximize if not deskewed
print("do you want to deskew the image *recommended for tilted images")
ch1=raw_input("y-yes,n-no?")
if ch1== 'n':
	img0 = cv2.resize(img0, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#initiating PIL
img00=Image.open(str)

if not is_grey_scale(str):
	img00.show()
	print("The image contains cooured  images if you convert it you may not get full accuracy")
	ch=raw_input("Do you want  to continue? y-yes n-no")
	if ch=='n':
		sys.exit()
#Creating a copy of the original
img=img0.copy()

#converting to grayscale
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
img2 = cv2.threshold(img1, 127, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
img2 = cv2.bitwise_not(img2)

#iff there is inclination of the text then rectifying it
coords = np.column_stack(np.where(img2 > 0))
angle = cv2.minAreaRect(coords)[-1]

#measuring angle
if angle < -45:
	angle2 = -(90 + angle)
else:
	angle2 = -angle

#rotating image to vertical position
(h, w) = img0.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle2, 1.0)
img3 = cv2.warpAffine(img2, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.imwrite('test000.png',img3)
#end of opencv operations

#starting PIL operations
im=Image.open('test000.png')
im.load()
if angle == 0:
	new_size = tuple(2*x for x in im.size)
	im = im.resize(new_size, Image.ANTIALIAS)

#MedianFilter eliminates noise
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(3)
im = im.convert('1')
im.save('test000.png')

#image to text
text = pytesseract.image_to_string(Image.open('test000.png'),lang='eng')
if text== "":
	print("this is a logo like")
#if text is an image or logo it will print the input as image
	img00.show()
os.remove('test000.png')
print(text)
#saving file to a text file
text_file = open("Output.txt", "w")
text_file.write("%s" % text)
text_file.close()

#to launch file in an editor
webbrowser.open("Output.txt")
