import random
import json

import extrusion_of_json
import appending_questions

import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

"""
CVZONE fonctionne comme ca:
colorR pour couleure intérieure
colorT pour couleure texte
colorB pour coleure bordure

"""

questions = appending_questions.get_questions()

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8)

while True:
    resolved = False
    while resolved == False:
        try:
            nb = random.randint(0,3000)
            print(nb)
            question = questions[nb]
            resolved=True
        except IndexError:
            pass

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    img, bbox = cvzone.putTextRect(img, "fuck", [50, 100], 1, 2, colorR=(26, 188,156), colorT=(255,255,255),offset=30, border=5)

    imgs = cv2.resize(img, (1920,1080))
    cv2.imshow("Game by Skyrix_ and justekaka", imgs)
    cv2.waitKey(1)