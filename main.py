import cv2
from PIL import Image

img_cat = "cat.jpeg"
cascade_cat = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
img = cv2.imread(img_cat)
cat_face = cascade_cat.detectMultiScale(img)

cat = Image.open(img_cat)
glasses = Image.open('glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, w, h) in cat_face:
    glasses=glasses.resize((w,int(h/3)))
    cat.paste(glasses,(x,int(y+h/4)),glasses)
cat.save("kit.png")
img = cv2.imread("kit.png")
cv2.imshow("cat", img)
cv2.waitKey()
