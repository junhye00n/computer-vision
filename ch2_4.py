import sys
import cv2


img = cv2.imread("girl_laughing.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")
cv2.rectangle(img, (800, 40), (1000, 200), (0, 0, 255), 2)
cv2.putText(img, "laugh", (800, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imshow("Display", img)
cv2.waitKey()
cv2.destroyAllWindows() 