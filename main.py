import json
from random import randint as rdint

from time import sleep as slp

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

questionNum=0
compteur=0

questions,propositions,reponses = appending_questions.get_questions()

i=0
question=[]
proposition=[]
reponse=[]
while i<400:
    try:
        nb=rdint(0,3000)
        print(nb)
        question.append(questions[nb])
        proposition.append(propositions[nb])
        reponse.append(reponses[nb])
        i+=1
    except IndexError:
        pass
print(question,proposition,reponse)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

while True:
    score=0
    
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)


    img, bbox0 = cvzone.putTextRect(img, question[questionNum], [100, 100], 1.5, 2, offset=50, border=5)
    img, bbox1 = cvzone.putTextRect(img, proposition[questionNum][0], [150, 350], 2, 2, offset=50, border=5)
    img, bbox2 = cvzone.putTextRect(img, proposition[questionNum][1], [700, 350], 2, 2, offset=50, border=5)
    img, bbox3 = cvzone.putTextRect(img, proposition[questionNum][2], [150, 500], 2, 2, offset=50, border=5)
    img, bbox4 = cvzone.putTextRect(img, proposition[questionNum][3], [700, 500], 2, 2, offset=50, border=5)
    img, bbox5 = cvzone.putTextRect(img, str(compteur), [10, 500])


    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]
        length, info = detector.findDistance(lmList[8], lmList[12])
        print(lmList[8])
        if length < 25:
            print(rdint(0,4673)," : vous avez cliqué!!!!!!!!! :D 🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣")

            for x, bbox in enumerate([bbox1, bbox2, bbox3, bbox4]):
                x1, y1, x2, y2 = bbox
                if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                    #self.userAns = x + 1
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                    compteur+=1
                    slp(0.4)
                    questionNum+=1



    imgs = cv2.resize(img, (1920,1080))
    cv2.imshow("Game by Skyrix_ and justekoro", imgs) #change to imgs to change resolution
    cv2.waitKey(1)
