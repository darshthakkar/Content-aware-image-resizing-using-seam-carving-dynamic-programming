import numpy as np
import cv2 
from skimage import color
from scipy import ndimage

def energy_image(im):
    gray_image = color.rgb2gray(im)
    gray_image = gray_image.astype(np.double)
    
    gx = ndimage.sobel(gray_image, axis=0)
    gy = ndimage.sobel(gray_image, axis=1)
    
    energyImage = np.absolute(gx) + np.absolute(gy)
    
    return energyImage