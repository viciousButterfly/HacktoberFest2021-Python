import cv2
import os

try:
    if not os.path.exists("dataNew"):
        os.makedirs("dataNew")
except OSError:
    print("Error: Creating directory of data")

currentFrame = 0

while True:
    name = "./data/frame" + str(currentFrame) + ".jpg"
    newName = "./dataNew/frame" + str(currentFrame) + ".jpg"
    pic = cv2.imread(name, 0)
    print("Creating..." + newName)
    cv2.imwrite(newName, pic)
    currentFrame += 1
cv2.waitKey(0)
cv2.destroyAllWindows()
