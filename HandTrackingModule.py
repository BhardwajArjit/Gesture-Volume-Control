import cv2
import time
import mediapipe as mp

class HandDetector:
    def __init__(self, mode=False, maxHands=2, modelConfidence=1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelConfidence = modelConfidence
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelConfidence,
                                        self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for handLand in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLand, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        PosList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                height, width, c = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                PosList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)

        return PosList


def main():
    prevTime = 0
    currentTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        PosList = detector.findPosition(img)

        if len(PosList) != 0:
            print(PosList[4])

        currentTime = time.time()
        fps = 1 / (currentTime - prevTime)
        pTime = currentTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Webcam", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()