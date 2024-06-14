import cv2 
from matplotlib import pyplot as plt

# Reading the image 
# img = cv2.imread("/home/bgoshtasbi/Desktop/ML Project/proj1_classification/raw-data/image_6.jpg")
img = cv2.imread('raw-data/image_6.jpg')


# Converting image to grayscale 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Loading the required xml classifier files 
# stop_cascade = cv2.CascadeClassifier('/path_to_your_xml_file/stop_data.xml')

face_cascade = cv2.CascadeClassifier('/src/Haarcascade_frontalface_default.xml') 
stop_cascade = cv2.CascadeClassifier('/src/stop_data.xml')

# Applying face detection method on the grayscale image 
faces_rect = face_cascade.detectMultiScale(gray_img, 1.1, 9,) 

# Detecting stop signs
stop_signs = stop_cascade.detectMultiScale(gray_img, minSize =(20, 20))

# Draw rectangles around detected faces and stop signs 
for (x, y, w, h) in faces_rect: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 

for (x, y, width, height) in stop_signs:
    cv2.rectangle(img, (x, y), (x + height, y + width), (0, 255, 0), 5)
    
# Display image
cv2.imshow('Detected Faces and Stop Signs', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()