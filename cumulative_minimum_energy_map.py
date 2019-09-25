import numpy as np
from scipy.ndimage import minimum_filter1d 


def cumulative_minimum_energy_map(energyImage,seamDirection):
    if seamDirection == 'VERTICAL':
        cumulativeMinimumEnergyMap = np.copy(energyImage)  
    elif seamDirection == 'HORIZONTAL':
        cumulativeMinimumEnergyMap = np.transpose(np.copy(energyImage))
        energyImage = np.transpose(energyImage)
    m,n = cumulativeMinimumEnergyMap.shape
    for row in range(1,m):
        prev_row = cumulativeMinimumEnergyMap[row-1]
        cumulativeMinimumEnergyMap[row] = energyImage[row] + minimum_filter1d(prev_row,3)
    if seamDirection =='HORIZONTAL':
        cumulativeMinimumEnergyMap = np.transpose(cumulativeMinimumEnergyMap)
    return cumulativeMinimumEnergyMap