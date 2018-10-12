from PIL import Image
import cv2
import os
import numpy as np
#global refPt, cropping
refPt = []
cropping = False
def user_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)
def img_crop(str):
  image=cv2.imread(str)
  clone = image.copy()
  #cv2.imshow("image",image)
  print("Press r to reset crop and s to save the crop")
  cv2.namedWindow("image")
  cv2.setMouseCallback("image", user_crop)
  while True:
	 # display the image and wait for a keypress
	  cv2.imshow("image", image)
	  key = cv2.waitKey(1) & 0xFF

	   # if the 'r' key is pressed, reset the cropping regio
	  if key == ord("r"):
		  image = clone.copy()

        # if the 's' key is pressed, break from the loop
	  if key == ord("s"):
			if len(refPt) ==2:
				roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        		cv2.imshow("ROI",roi)
        		cv2.imwrite('test00.png',roi)
        		imk=Image.open('test00.png')
        		imk.load()
        		imk.show()
			des=raw_input("Do you want to save y-yes n-no")
			if des=="y":
				#Saved in the same relative location else discarded
				imk.save(str)
				print("Saved")
			else:
				print("change discarded")
			os.remove('test00.png')

			break
