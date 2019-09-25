import cv2
import numpy as np
from energy_image import energy_image
from reduceHeight import reduceHeight

im = cv2.imread('inputSeamCarvingPrague.jpg')
energyImage = energy_image(im)
[reducedColorImage, reducedEnergyImage] = reduceHeight(im, energyImage)
for iterator in range(1,100):
    [reducedColorImage, reducedEnergyImage] =  reduceHeight(reducedColorImage, reducedEnergyImage)
cv2.imwrite('outputReduceHeightPrague.png', reducedColorImage)


im = cv2.imread('inputSeamCarvingMall.jpg')
energyImage = energy_image(im)
[reducedColorImage, reducedEnergyImage] = reduceHeight(im, energyImage)
for iterator in range(1,100):
    [reducedColorImage, reducedEnergyImage] =  reduceHeight(reducedColorImage, reducedEnergyImage)
cv2.imwrite('outputReduceHeightMall.png', reducedColorImage)



