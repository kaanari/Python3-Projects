import cv2
import numpy as np
import time
from PIL import Image
import pytesseract
import picamera
#pytesseract.pytesseract.tesseract_cmd: 'C:\Program Files (x86)\Tesseract-OCR\\tesseract' #Plase read the Pytesseract Documentation for this line.

def isParkSign(img):
    parksign_cascade = cv2.CascadeClassifier('parksign_cascade.xml')

    sign = parksign_cascade.detectMultiScale(img, 1.4, 5)  # 1.3-1.4 arasinda gidiyor degerler
    if np.any(sign):
        return 1
    else:
        return 0


def isLeftSign(img):
    sign = cv2.CascadeClassifier('leftsign_cascade.xml')
    sign = sign.detectMultiScale(img, 1.2, 3)
    if sign != ():
        return 1
    else:
        return 0


def isRightSign(img):
    sign=cv2.CascadeClassifier('rightsign_cascade.xml')
    sign = sign.detectMultiScale(img, 1.3, 3)
    if sign != ():
        return 1
    else:
        return 0


def isStraightSign(img):
    sign=cv2.CascadeClassifier('straightsign_cascade.xml')
    sign = sign.detectMultiScale(img, 1.2, 5)
    if sign != ():
        return 1
    else:
        return 0
"""
def leftORright(img):
    gray = cv2.cvtColor(samples, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(gray, (x, y), r, (0, 0, 0), -1)
            ret, mask = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask)
            img = cv2.bitwise_and(img, img, mask=mask)
            img = img[int(y - r + r * 0.5):int(y + r - r * 0.5), int(x - r + r * 0.4):int(x + r - r * 0.4)]
    gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    y0, x0 = img.shape[:2]
    gray2 = np.float32(gray2)
    dst = cv2.cornerHarris(gray2, 2, 1, 0.11)
    dst = cv2.dilate(dst, None)
    img[dst > 0.01 * dst.max()] = [0, 255, 0]
    coord = np.where(np.all(img == (0, 255, 0), axis=-1))
    a = []
    a.append(coord[1])
    b = np.array(coord[1]).mean()
    if b>(x0/2):
        return 1
    else:
        return 0 # Sol ok
"""
def ParkNumber(img):
    gray = cv2.cvtColor(samples, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("graycircle.jpg",gray)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(gray, (x, y), r, (0, 0, 0), -1)
            ret, mask = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY)
            cv2.imwrite("mask1.jpg",mask)
            mask=cv2.bitwise_not(mask)
            cv2.imwrite("mask2.jpg",mask)
            img = cv2.bitwise_and(img, img, mask=mask)
            img = img[int(y - r):int(y + r), int(x - r):int(x + r)]
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
    for i in range(0,20):
        filtered = img
        y, x = filtered.shape[:2]
        cv2.rectangle(filtered, (0, 0), (y, x), (255, 255, 255), int(x * (0.28+i*0.01)))
        cv2.imwrite(str(i)+".jpg",filtered)
        filtered = Image.fromarray(filtered)
        text = pytesseract.image_to_string(filtered, lang='eng', config="-c tessedit_char_whitelist=123AB -psm 6")
        if (text == ("B3") or text == ("A1") or text == ("A2") or text == ("A3") or text == ("B1") or text == ("B2")):
            print("step"+str(i))
            print(text)
            return text
    return 0

def whichSign():
    camera = picamera.PiCamera() # I used it for Raspberry Pi. You can use any camera which you want.
    time.sleep(0.1)
    camera.capture('image.jpg')
    samples = cv2.imread("image.jpg")
    park,straight,right,left=isParkSign(samples),isStraightSign(samples),isRightSign(samples),isLeftSign(samples)
    print(park,straight,right,left)
    if park==1:
        return 0
    if straight==1:
        return 1
    if right==1:
        return 2
    if left==1:
        return 3
    if park==0 and straight==0 and right==0 and left==0:
        return 4
   # if right==1 and left==1:
       # leftORright(samples)
   # if(park==0 and straight==0 and right==0 and left==0):
       # leftORright(samples)
