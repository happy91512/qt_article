#model.py
import cv2
import numpy as np

def get_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def get_HSV(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img

if __name__ == "__main__":
    img = cv2.imread("frogg.jpg")
    #img = get_gray(img)
    cv2.imshow("123", get_HSV(img))
    cv2.waitKey(0)