import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('stopper.jpg') #lets use some other images
img=cv.resize(img,(500,500))
cv.imshow("image",img)

#method 1
hist=cv.calcHist([img],[0],None,[256],[0,256])#to calculate the histogram
plt.plot(hist)

#method 2
b,g,r=cv.split(img) #to split the image in bgr channel
plt.hist(b.ravel(),256,(0,256)) #it gives the intensity distribution of blue color in image
plt.hist(g.ravel(),256,(0,256)) # for green color
plt.hist(r.ravel(),256,(0,256)) #for red color

#method 3
color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256]) #so this was another method
    
plt.show()
#so this shows the change in the color intensity

cv.waitKey(0)
cv.destroyAllWindows()
