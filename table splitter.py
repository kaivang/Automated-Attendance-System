import os
import cv2
import numpy as np
import os

#part1
#img = cv2.imread('test.png',0)
img = cv2.imread('test.png',0)
thresh,img_bin = cv2.threshold(img, 130, 255,cv2.THRESH_BINARY)
img_bin = 255-img_bin 
cv2.imwrite("Image_bin.jpeg",img_bin)
#cv2.imshow('image',img_bin)

#part2
kernel_length = np.array(img).shape[1]//80
# A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
verticle = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
# A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
hori = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
# A kernel of (3 X 3) ones.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

#part3
#Morphological operation to detect vertical lines from an image
img_temp1 = cv2.erode(img_bin, verticle, iterations=3)
verticle_lines_img = cv2.dilate(img_temp1, verticle, iterations=3)
cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
# Morphological operation to detect horizontal lines from an image
img_temp2 = cv2.erode(img_bin, hori, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori, iterations=3)
cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

#cv2.imshow('image',img_temp1)
#cv2.imshow('image',img_temp2)


#part4
# Weighting parameters, this will decide the quantity of an image to be added to make a new image.
alpha = 0.5
beta = 1.0 - alpha

# This function helps to add two image with specific weight parameter to get a third image as summation of two image.
img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)

##The function erodes the source image using the specified structuring element 
img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)

thresh, img_final_bin = cv2.threshold(img_final_bin, 255, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imwrite("img_final_bin.jpg",img_final_bin)
#cv2.imshow("finale image",img_final_bin)

##from PIL import Image  
##
##im = Image.open("img_final_bin.jpg")  
##im.show() 
#cv2.imshow("img_final_bin.jpg",img_final_bin)

#part5

im2=img_final_bin
contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

path = 'C:/Users/Kaivan/test/testing'
idx = 0
for c in contours:
    # Returns the location and width,height for every contour
    x, y, w, h = cv2.boundingRect(c)
## h > 10    
    if (w > 140 and h < 350 ) and w > 2.5*h:
        idx += 1
        new_img = img[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(path,str(idx) + '.jpg'), new_img)
print("total no of rows in the table:",idx)








