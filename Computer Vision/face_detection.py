import cv2,pandas
from datetime import datetime

frame_first=None
timing=[]
status_list=[None,None]
face_capture=cv2.VideoCapture(0)

my_data=pandas.DataFrame(columns=["Enter Time","Exit Time"])

while True:
    check,frame=face_capture.read()
    img_status=0
    gray_scale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_scale_img=cv2.GaussianBlur(gray_scale_img,(21,21),0)

    if frame_first is None:
        frame_first=gray_scale_img
        continue

    blured_frame=cv2.absdiff(frame_first,gray_scale_img)
    
    #Threshold Frame
    threshold_frame=cv2.threshold(blured_frame,40,255,cv2.THRESH_BINARY)[1]
    #Clear frame
    threshold_frame=cv2.dilate(threshold_frame,None,iterations=3)

    #Countour
    (contour,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cntr in contour:
        if cv2.contourArea(cntr)<10000:
            continue
        img_status=1
        (x,y,w,h)=cv2.boundingRect(cntr)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    status_list.append(img_status)
    status_list=status_list[-2:]
    
    if status_list[-1]==1 and status_list[-2]==0:
        timing.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        timing.append(datetime.now())

    cv2.imshow('Normal Frame',frame) #Normal Image

    press_key=cv2.waitKey(1)
    if press_key==ord('q'):
        if img_status==1:
            timing.append(datetime.now())
        break

face_capture.release()
cv2.destroyAllWindows()
