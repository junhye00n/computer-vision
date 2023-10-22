import sys
import cv2


img = cv2.imread("soccer.jpg")  # imread 는 불러옴
# print(type(img))
# print(img)
print(img.shape)
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv2.imshow("Image Display", img)    # imshow 는 나타냄
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image Display", gray_img)  

# cv2.imwrite("soccer_gray.jpg", gray_img)    # imwrite 는 저장

resized_img = cv2.resize(gray_img, dsize=(0, 0), fx=0.5, fy=0.5)
cv2.imshow("Resized image", resized_img)

cv2.waitKey()   # 보여주기 위해서 대기하는 코드
cv2.destroyAllWindows()