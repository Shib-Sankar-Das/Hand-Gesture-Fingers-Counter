import cv2
import time
import os
import HandTrackingModule as htm

def overlayPNG(img, overlay, x, y):
    b, g, r, a = cv2.split(overlay)
    overlay_rgb = cv2.merge((b, g, r))
    mask = cv2.merge((a, a, a))

    h, w, _ = overlay_rgb.shape
    roi = img[y:y+h, x:x+w]

    img_bg = cv2.bitwise_and(roi, cv2.bitwise_not(mask))
    overlay_fg = cv2.bitwise_and(overlay_rgb, mask)

    combined = cv2.add(img_bg, overlay_fg)
    img[y:y+h, x:x+w] = combined

    return img

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "count"
myList = os.listdir(folderPath)
print(myList)

overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}', cv2.IMREAD_UNCHANGED)  # Load with alpha channel
    image = cv2.resize(image, (154, 256))  # Resize the image to match the desired shape
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    #img = cv2.flip(img, 1)

    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        fingers = []

        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)

        totalFingers = fingers.count(1)

        overlay = overlayList[totalFingers]
        img = overlayPNG(img, overlay, 20, 20)

        #cv2.rectangle(img, (20, 20), (174, 276), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (40, 400), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (470, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)