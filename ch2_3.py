import sys
import cv2
import numpy as np


cap = cv2.VideoCapture("sea.mp4")

if not cap.isOpened():
    sys.exit("불러오기 실패")

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임 흭득에 실패해 루프를 나갑니다.")
        break
    frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
    cv2.imshow("Video display", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    elif cv2.waitKey(1) == ord("c"):
        frames.append(frame)
        # print(frames)
        print("저장됨!")
cap.release()
cv2.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))

    cv2.imshow("collected images", imgs)
    cv2.waitKey()
    cv2.destroyAllWindows()