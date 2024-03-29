import cv2
import numpy as np
from PIL import Image
import os

    # function to get the images and label data
def getImagesAndLabels():
    path = 'trainimage_path/'
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples =[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split("_")[1])
            
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
        
    return faceSamples, ids

def faceRecognizer():
    # Path for face image database
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    print ("\n[INFO] ИНТИЗОР ШАВЕД ...")
    faces,ids = getImagesAndLabels()
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} ЧЕХРАИ ИНСОН ОМУХТА ШУД".format(len(np.unique(ids))))



