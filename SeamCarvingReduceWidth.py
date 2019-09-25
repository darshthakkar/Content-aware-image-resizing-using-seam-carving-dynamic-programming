import cv2
import numpy as np
from energy_image import energy_image
from reduceWidth import reduceWidth

im = cv2.imread('inputSeamCarvingPrague.jpg')
energyImage = energy_image(im)
[reducedColorImage, reducedEnergyImage] = reduceWidth(im, energyImage)
for iterator in range(1,100):
    [reducedColorImage, reducedEnergyImage] =  reduceWidth(reducedColorImage, reducedEnergyImage)
cv2.imwrite('outputReduceWidthPrague.png', reducedColorImage)

im = cv2.imread('inputSeamCarvingMall.jpg')
energyImage = energy_image(im)
[reducedColorImage, reducedEnergyImage] = reduceWidth(im, energyImage)
for iterator in range(1,100):
    [reducedColorImage, reducedEnergyImage] =  reduceWidth(reducedColorImage, reducedEnergyImage)
cv2.imwrite('outputReduceWidthMall.png', reducedColorImage)