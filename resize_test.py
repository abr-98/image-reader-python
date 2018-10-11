from PIL import Image
import cv2
import os


im=cv2.imread("test_img.jpg")
print("original Dimensions: ",im.shape)
print("Enter the new size")
h=raw_input("hieght:")
h_int=int(h)
w=raw_input("width:")
w_int=int(w)
dim=(w_int,h_int)

img = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('test00.png',img)
imk=Image.open('test00.png')
imk.load()
imk.show()

des=raw_input("Do you want to save y-yes n-no ")

if des=="y":
    #Saved in the same relative location else discarded
    imk.save("test_img.jpg")
    print("Saved")
else:
    print("change discarded")
    os.remove('test00.png')
