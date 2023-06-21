import cv2 as cv  

img = cv.imread("python.jpeg")

cv.imshow("python",img)

h,g,r = cv.split(img)

print(r)