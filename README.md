# Hand Tracking Module

Hand Tracking Module[HTM] is a python module using cv2 and mediapipe to track hand and finger

![LOGO](https://imgr2.lookpic.cn/2025/01/17/2025-01-17_19-51-5826b0cd28ffc26ac0.png)

# Feature
- Precisely detect hand and fingers
- Spread fingers into a list with status of True and False
- Follow the OOP
- Easy to use

# Example Project
[ChromeDino-HandControl](https://github.com/safe049/ChromeDino-HandControl)

A project that make you be able to play Chrome Dino game only with your hand

# Included Class and Function
1. Class:
  - HandDetector

2. Function:
  [All included in HandDetector Class]
  - __init__:
    
    Define variables
    
  - findHands:

    find Hands in the in the image

    return img
    
  - findPosition

    Find exact position of hands,and draw bone on it

    If not found or out of range,return a empty list

    return lmList

  - fingerStatus

    Catch the status of finger,is it closed or open?

    return fingerList

    [Will raise Value Error if lmList is empty]

# Usage

1. Install following package:
- opencv-python
- mediapipe
- numpy

```bash
pip install opencv-python mediapipe numpy
```
2. Import it into your project

# Used Project

- OpenCV [https://opencv.org/](https://opencv.org/)
- MediaPipe [https://github.com/google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)
- numpy [https://numpy.org/](https://numpy.org/)

# License

This Project follows the Apache 2.0 License
