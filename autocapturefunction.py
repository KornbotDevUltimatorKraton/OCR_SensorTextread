import numpy as np 
from nanpy import(ArduinoApi,SerialManager) # Serial Manager function for hardware control software 
# opencv for the capture function into the .jpg 
import datetime 
import os # operating system control read 
import cv2
import time
from ocrtextout import ocr_msg
WorkDay = []
today = datetime.date.today() 
WorkDay.append(today)

cam = cv2.VideoCapture(1)

cv2.namedWindow("OCR capture text read")

img_counter = 0

Ultrasonics = 0

try: 
    connection = SerialManager() 
    Hardwarecontrol = ArduinoApi(connection=connection)
except: 
     print("Hardware unit error please check")

def capture_pictures(): 
      cv2.imshow('img1',frame) # display the image was capture 
      cv2.imwrite('img1'+ str(WorkDay[0]) + '.jpg',frame)
while True:
    ret, frame = cam.read()
    cv2.imshow("ocr seccondcamera", frame)
    Ultrasonics = Hardwarecontrol.analogRead(2) # Reading the analogvalue from the sensor that deteted the opject 
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 ==27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        '''
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        '''
        capture_pictures()
    
    if Ultrasonics >= 600: 
         capture_pictures()
         time.sleep(0.1) 
         os.system("python ocrtextout.py") # Running the ultra
         print(ocr_msg)
cam.release()

cv2.destroyAllWindows()
