import numpy as np
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from energy_image import energy_image

def reduceHeight(im, energyImage):
    m, n = im.shape[: 2]
    
    cumulativeMinimumEnergyMap = cumulative_minimum_energy_map(energyImage,'HORIZONTAL')
    horizontal_seam = find_optimal_horizontal_seam(cumulativeMinimumEnergyMap)
    
    reducedColorImage = np.zeros((m-1,n,3),dtype = np.uint8)
    reducedEnergyImage = np.zeros((m-1,n),dtype = np.float64)

    for col in range(n):
        imageCopy = im[:,col,:]
        mask = np.ones(m,dtype = bool)
        mask[horizontal_seam[col]] = False
        reducedColorImage[:,col,:] = imageCopy[mask]
    
    reducedEnergyImage = energy_image(reducedColorImage)
        
    return [reducedColorImage,reducedEnergyImage]