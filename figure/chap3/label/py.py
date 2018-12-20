import cv2
import os
files=os.listdir('./')
print(files)
for file in files:
	img=cv2.imread(file)
	img=cv2.resize(img,(800,600))
	cv2.imwrite(file,img)