import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

import numpy as np
import pandas as pd
import datetime
import time
from functions import *


video_capture = cv2.VideoCapture(0)

video_capture.set(3, 1280) # set video widht
video_capture.set(4, 720) # set video height

window = Tk()
window.geometry("1280x720")
window.configure(bg="green")


frameCam = Frame(window, width = 720, height = 520, bg = "black", bd=5)
frameCam.pack()
frameCam.place(x = 40, y = 40)
label_widget = Label(frameCam, bg="green", width = 700, height = 500)

#------------------------------------------------------------#
              #КИСМИ НИШОН ДОДАНИ ВЕБ-КАМЕРА
#------------------------------------------------------------#

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


familyaValue = ""
imyaValue = ""
otchestvoValue = ""
idValue = ""
doljnostValue = ""

key = False
sampleNum = 0

def keyTrue():
    global key
    global familyaValue
    global imyaValue
    global otchestvoValue
    global idValue
    global doljnostValue

    familyaValue = textFamilya.get()
    imyaValue = textImya.get()
    otchestvoValue = textOtchestvo.get()
    doljnostValue = textDoljnost.get()
    idValue = textParol.get()
    
    prId = proverkaID(idValue)
    print(prId)

    if (prId == False):
        insert_data(idValue, familyaValue, imyaValue, otchestvoValue, doljnostValue)
        key = True

    
def update_camera():

    global imyaValue
    global idValue

    global sampleNum
    global key
    
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1) #Flip vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Тасвири хат дар руйи одам
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Ичрои суратгири агар key == True бошад
    if (key == True):
        sampleNum = sampleNum + 1
        print(sampleNum)
        cv2.imwrite("trainimage_path/" + imyaValue + "_" + idValue + "_" + str(sampleNum) + ".jpg", gray[y : y + h, x : x + w],)
        if sampleNum > 50:
            key = False
            sampleNum = 0
            from face_training import faceRecognizer
            faceRecognizer()
            
           
    # Табаддулоти расм бо OpenCV ба формате, ки tkinter нишон дода метавонад
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    photo_image = ImageTk.PhotoImage(image=image)
    
    # Обновить кардани расм дар Label
    label_widget.configure(image=photo_image)

    label_widget.image = photo_image

    label_widget.pack(anchor = "nw")
    
    # Запуски фунскияи update_camera баъди хар як 10 миллисекунд

    label_widget.after(10, update_camera)

        
#------------------------------------------------------------#
           #КИСМИ ПУР КАРДАНИ МАЪЛУМОИ ШАХСИЯТ
#------------------------------------------------------------#
    

lFamilya = tk.Label(
        window,
        text="ФАМИЛИЯ",
        bg="green",
        fg="navy",
        font=("times new roman", 30),
)
lFamilya.place(x=820, y=15)


        
textFamilya = tk.Entry(
    window,
    text="",
    font=("times new roman", 30),
    width=25,
    bd=5,
    bg="white",
    fg="black",
)
textFamilya.place(x=780, y=80)


lImya = tk.Label(
        window,
        text="НОМ",
        bg="green",
        fg="navy",
        font=("times new roman", 30),
)
lImya.place(x=820, y=140)


textImya = tk.Entry(
    window,
    text="",
    font=("times new roman", 30),
    width=25,
    bd=5,
    bg="white",
    fg="black",
)
textImya.place(x=780, y=200)


lOtchestvo = tk.Label(
        window,
        text="НАСАБ",
        bg="green",
        fg="navy",
        font=("times new roman", 30),
)
lOtchestvo.place(x=820, y=260)

textOtchestvo = tk.Entry(
    window,
    text="",
    font=("times new roman", 30),
    width=25,
    bd=5,
    bg="white",
    fg="black",
)
textOtchestvo.place(x=780, y=320)


ldoljnost = tk.Label(
        window,
        text="Вазифа",
        bg="green",
        fg="navy",
        font=("times new roman", 30),
)
ldoljnost.place(x=820, y=380)

textDoljnost = tk.Entry(
    window, 
    text="",
    font=("times new roman", 30),
    width=25,
    bd=5,
    bg="white",
    fg="black",
)
textDoljnost.place(x=780, y=440)


lparol = tk.Label(
        window,
        text="РАКАМИ ШАХСИ",
        bg="green",
        fg="navy",
        font=("times new roman", 30),
)
lparol.place(x=820, y=500)

textParol = tk.Entry(
    window, 
    text="",
    font=("times new roman", 30),
    width=25,
    bd=5,
    bg="white",
    fg="black",
)
textParol.place(x=780, y=560)

    
#------------------------------------------------------------#
      #КИСМИ КНОПКАХОИ МУАЙЯН ВА ВОРИДКУНИИ РУЙ ДАР SQL
#------------------------------------------------------------#

btnScayn = tk.Button(
    window,
    text="Омухтани руй",
    command=update_camera,
    bd=5,
    font=("times new roman", 16),
    width=30,
    height=2,
    bg="black",
    fg="yellow",
)
btnScayn.place(x=40, y=600)


btnImport = tk.Button(
    window,
    text="Ворид кардани руй",
    command=keyTrue,
    bd=5,
    font=("times new roman", 16),
    width=30,
    height=2,
    bg="black",
    fg="yellow",
)
btnImport.place(x=450, y=600)


btnImport = tk.Button(
    window,
    text="Ворид кардани руй",
    command=keyTrue,
    bd=5,
    font=("times new roman", 16),
    width=30,
    height=2,
    bg="black",
    fg="yellow",
)
btnImport.place(x=450, y=600)




window.mainloop()
