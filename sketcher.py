#Descriptioon:This program converts an image to a pencil sketch

#pip install opencv-python
#import the library
#to import opencv-python in pycharm, go to file->settins->project-python project(select the file)->project interpreter->click on + button at bottom left->search and install
import cv2

#Get the image location and image file name
img_location = 'D:/project/'
filename = 'image1.jpeg'

#read in the image
img = cv2.imread(img_location+filename)

#convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_gray_image = 255 - gray_image



#blur the img by guassian function
blurred_img=cv2.GaussianBlur(inverted_gray_image,(21,21),0)

#Invert the blurred image
inverted_blurred_img = 255 - blurred_img

#create the pencil sketch image
pencil_sketch_IMG = cv2.divide(gray_image,inverted_blurred_img,scale=256.0)

#show the image
cv2.imshow('Original Image',img)
#cv2.imshow('New Image',gray_scale)
#cv2.imshow('New Image',inverted_gray_scale)
#cv2.imshow('New Image',inverted_blurred_img)
cv2.imshow('New Image',pencil_sketch_IMG)
cv2.waitKey(0)
