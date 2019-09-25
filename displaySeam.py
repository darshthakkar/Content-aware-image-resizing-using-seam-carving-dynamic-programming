import numpy as np
import cv2

def displaySeam(im, seam, type):
    carved = np.copy(im)
    if type == "HORIZONTAL":
        for col in range(len(seam)):
            carved[seam[col],col] = [0,0,255]
    elif type == "VERTICAL":
        for row in range(len(seam)):
            carved[row,seam[row]] = [0,0,255]
    cv2.imshow("Carved_Image",carved)
    cv2.waitKey(0)