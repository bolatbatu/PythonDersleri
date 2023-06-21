import cv2 as cv  

img = cv.imread("30.2.opencv.png")

cv.imshow("python",img)

b,g,r = cv.split(img)

print(r)

cv.imshow("r",r)
cv.imshow("b",b)
cv.imshow("g",g)


if cv.waitKey(0) & 0XFF == ord("q"):
    cv.destroyAllWindows()
