# Importing OpenCV package 
import cv2 
from matplotlib import pyplot as plt

  
# Reading the image 
img = cv2.imread("/home/bgoshtasbi/Desktop/ML Project/proj1_classification/image_5.jpg")
  
# Converting image to grayscale 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   
  
# Loading the required haar-cascade xml classifier file 
haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml') 
  
# Applying the face detection method on the grayscale image 
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 

#STOP
stop_data = cv2.CascadeClassifier('stop_data.xml')

found = stop_data.detectMultiScale(img_gray, 
                                minSize =(20, 20))

  
# Iterating through rectangles of detected faces 
for (x, y, w, h) in faces_rect: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 

amount_found = len(found)
   
if amount_found != 0:
       
    # There may be more than one
    # sign in the image
    for (x, y, width, height) in found:
           
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(img_rgb, (x, y), 
                      (x + height, y + width), 
                      (0, 255, 0), 5)

# Creates the environment of 
# the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
  
cv2.imshow('Detected faces', img) 
  
cv2.waitKey(0) 