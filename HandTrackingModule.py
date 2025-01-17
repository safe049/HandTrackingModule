import cv2
import mediapipe as mp
import math
import numpy as np

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.3, trackCon=0.3):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        if not isinstance(img, np.ndarray):
            raise ValueError("Input image must be a numpy array.")
        
        # 如果没有检测到手或者 handNo 超出范围，返回空列表
        if self.results.multi_hand_landmarks is None or handNo >= len(self.results.multi_hand_landmarks):
            print("No hand found at the specified handNo or handNo out of range.")
            return []

        lmList = []
        h, w, c = img.shape  # 只需要计算一次图像的形状
        myHand = self.results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
            if draw:
                cv2.putText(img, str(id), (cx + 10, cy + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        
        return lmList


    def fingerStatus(self, lmList):
        if not isinstance(lmList, list) or not lmList:
            raise ValueError("Input lmList must be a non-empty list.")

        fingerList = []
        originx, originy = lmList[0][1], lmList[0][2]  # 只需要提取一次原点坐标
        keypoint_list = [[2, 4], [6, 8], [10, 12], [14, 16], [18, 20]]
        for point in keypoint_list:
            x1, y1 = lmList[point[0]][1], lmList[point[0]][2]
            x2, y2 = lmList[point[1]][1], lmList[point[1]][2]
            fingerList.append(math.hypot(x2 - originx, y2 - originy) > math.hypot(x1 - originx, y1 - originy))

        return fingerList
