import cv2
import numpy as np
import os
from functions import select_name_byid

def open_camera():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #recognizer.setThreshold(100)
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 1280) # set video widht
    cam.set(4, 720) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
        img = cv2.flip(img, 1) #Flip vertically

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print(id)
            if (confidence > 60):
                info = select_name_byid(id)
                confidence = "  {0}%".format(round(confidence))
            else:
                info = "unknown"
                confidence = "  {0}%".format(round(confidence))
            
            cv2.putText(img, str(info), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

            
        k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        cv2.imshow('camera',img)

    cam.release()
    cv2.destroyAllWindows()

    #Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")

open_camera()
