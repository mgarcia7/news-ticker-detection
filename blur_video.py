import numpy as np
import cv2
from matplotlib import pyplot as plt

video_name = '/Dramas/tv/Heard it Through the Grapevine (720p)/Heard.it.Through.the.Grapevine.E07.150316.HDTV.H264.720p-LIMO.avi'
cap = cv2.VideoCapture(video_name)


frame_seconds_normal = 2500;
frame_seconds_new = 2200;

def grab_frame(ms):
    cap.set(cv2.CAP_PROP_POS_MSEC,ms)
    ret,frame = cap.read()
    return frame

def main():
    frame = grab_frame(frame_seconds_new*1000)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # contrast enhancement    
    res = cv2.equalizeHist(gray)
    #res = np.hstack((gray,equ))
    #cv2.imshow('frame',res)

    # edge detection
    laplacian = cv2.Laplacian(res,cv2.CV_64F)
    sobelx = cv2.Sobel(res,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(res,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow('frame',sobelx)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
