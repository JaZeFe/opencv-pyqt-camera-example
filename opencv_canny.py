import cv2
import numpy as np

def CannyThreshold(lowThreshold, gray, img):
    ratio = 3
    kernel_size = 3

    detected_edges = cv2.GaussianBlur(gray, (3,3), 0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges) # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

def main():    
    cam = cv2.VideoCapture(0)
    lowThreshold = 0
    max_lowThreshold = 100

    while True:
        retval, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('canny demo')
    
        cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
    
        CannyThreshold(0, gray, img) # initialization
        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
