import numpy as np
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from energy_image import energy_image

def reduceWidth(im, energyImage):
    m, n = im.shape[: 2]
    
    cumulativeMinimumEnergyMap = cumulative_minimum_energy_map(energyImage,'VERTICAL')
    verticalSeam = find_optimal_vertical_seam(cumulativeMinimumEnergyMap)
    
    reducedColorImage = np.zeros((m,n-1,3),dtype = np.uint8)
    reducedEnergyImage = np.zeros((m,n-1),dtype = np.float64)

    for rows in range(m):
        imageCopy = im[rows,:,:]
        mask = np.ones(n,dtype = bool)
        mask[verticalSeam[rows]] = False
        reducedColorImage[rows,:,:] = imageCopy[mask]
        
    reducedEnergyImage = energy_image(reducedColorImage)
        
    return [reducedColorImage,reducedEnergyImage]