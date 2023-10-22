import sys
import cv2


img = cv2.imread("girl_laughing.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

def draw(event, x, y, flages, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
    cv2.imshow("drawing", img)


cv2.namedWindow("drawing")
cv2.imshow("drawing", img)
cv2.setMouseCallback("drawing", draw)
while True:
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break