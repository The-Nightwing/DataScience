import cv2
import numpy as np

cap = cv2.VideoCapture("Jamie_Before.jpg")
eyes_class = cv2.CascadeClassifier("frontalEyes35x16.xml")  # xml with eyes proportions
nose_class = cv2.CascadeClassifier("Nose18x15.xml")  # xml with nose proportions
while True:
    retval, img = cap.read()
    if retval:
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        eyes = eyes_class.detectMultiScale(img)
        nose = nose_class.detectMultiScale(img)

        x1, y1, w1, h1 = eyes[0]


        glass = cv2.imread("glasses.png")
        glass = cv2.resize(glass, (w1, h1))

        for i in range(glass.shape[0]):
            for j in range(glass.shape[1]):
                if glass[i, j, 3] > 0:
                    img[y1 + i, x1 + j, :] = glass[i, j, :-1]

        #cut_nose = img[y2:y2 + w2, x2:x2 + h2]

        cv2.imshow("Glasses", img)

        # cv2.imshow("photo",img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
