# python3 scripy.py imagename.jpg
# This script will create a transparent stamp. Note: In input image contains a stamp with blue color, over a white background.

import cv2 as cv
import numpy as np
import sys

img_name=sys.argv[1]
img=cv.imread(img_name)
val=205
tmp_pix=[255,255,255,1]
tmp_img=[]
for j in range(img.shape[0]):
    tmp_col=[]
    for i in range(img.shape[1]):
        if img[j][i][0]<val and img[j][i][1]<130 and img[j][i][2]<120:
            tmp_val=[img[j][i][0],img[j][i][1],img[j][i][2],255]
        else:
            tmp_val=tmp_pix
        tmp_col.append(tmp_val)
    tmp_img.append(tmp_col)
cv.imwrite("result.png",np.array(tmp_img))
