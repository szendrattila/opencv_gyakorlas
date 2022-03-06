import cv2 as cv
#kep olvasas
######################################################
"""
print("Package Imported")

img = cv.imread("kepek/songkang.jpg")

cv.imshow("UwU", img)

cv.waitKey(0)
"""
##################################################
#video olvasas
"""
def resclaeframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture("kepek/moon.mp4")

while True:
    isTrue, frame = cap.read()
    frame_resized = resclaeframe(frame, scale=.2)
    cv.imshow("gif", frame)
    cv.imshow("meretezett", frame_resized)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
"""
############################################################
#szurkites
"""

img = cv.imread("kepek/songkang.jpg")
cv.imshow("Uwu", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("szurke", gray)
cv.waitKey(0)
"""
###################################################
#homalyositas
"""
img = cv.imread("kepek/songkang.jpg")
cv.imshow("Uwu", img)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("homalyozott", blur)
"""

#######################################################
#szelkereso
"""
img = cv.imread("kepek/songkang.jpg")
cv.imshow("Uwu", img)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("homalyozott", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("szelek", canny)
cv.waitKey(0)
"""
########################################################
#meretezes
img = cv.imread("kepek/songkang.jpg")
cv.imshow("Uwu", img)
meretezett = cv.resize(img, (500,500))
cv.imshow("meretezett", meretezett)
cv.waitKey(0)