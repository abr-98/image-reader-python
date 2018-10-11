from PIL import Image
import imutils
import cv2
import os

ch="1"
def img_rotate(str):
  while ch != "3":
      img=Image.open(str)
      img0=cv2.imread(str)
      #img.show()
      im=img.copy()

      print("-----------------------OPTIONS-----------------------")
      print("1.Right angle")
      print("2.180 rotate")
      print("3.exit")
      ch=raw_input("Enter your choice: ")

      if ch=="1":
          #rotating image by 90
        img = imutils.rotate_bound(img0, 90)
        cv2.imwrite('test00.png',img)
        imk=Image.open('test00.png')
        imk.load()
        imk.show()

        des=raw_input("Do you want to save y-yes n-no ")

        if des=="y":
            #Saved in the same relative location else discarded
            imk.save(str)
            print("Saved")
        else:
            print("change discarded")
        os.remove('test00.png')


      elif ch=="2":
       #rotating image by 90
       im = im.rotate(180)
       im.show()
       des=raw_input("Do you want to save y-yes n-no ")

       if des=="y":
          #Saved in the same relative location else discarded
          img.save(str)
          print("Saved ")
       else:
          print("change discarded")
