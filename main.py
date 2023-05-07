import json
from random import randint as rdint

import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

import appending_questions

"""
CVZONE fonctionne comme ca:
colorR pour couleure intérieure
colorT pour couleure texte
colorB pour coleure bordure

"""

questions,reponses = appending_questions.get_questions()

i=0
question=[]
reponse=[]
while i<4:
    try:
        nb=rdint(0,3000)
        print(nb)
        question.append(questions[nb])
        reponse.append(reponses[nb])
        i+=1
    except IndexError:
        pass
print(question,reponse)

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    img, bbox0 = cvzone.putTextRect(img, question[0], [100, 100], 2, 2, offset=50, border=5)
    img, bbox1 = cvzone.putTextRect(img, reponse[0][0], [150, 350], 2, 2, offset=50, border=5)
    img, bbox2 = cvzone.putTextRect(img, reponse[0][1], [700, 350], 2, 2, offset=50, border=5)
    img, bbox3 = cvzone.putTextRect(img, reponse[0][2], [150, 500], 2, 2, offset=50, border=5)
    img, bbox4 = cvzone.putTextRect(img, reponse[0][3], [700, 500], 2, 2, offset=50, border=5)


    imgs = cv2.resize(img, (1920,1080))
    cv2.imshow("Game by Skyrix_ and justekaka", imgs) #change to imgs to change resolution
    cv2.waitKey(1)