import numpy as np

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    m, n = cumulativeEnergyMap.shape
    resultVector = np.zeros((n,), dtype=np.uint32)
    resultVector[-1] = np.argmin(cumulativeEnergyMap[:,-1])
    for col in range(n-2, -1, -1):
        previousRow = resultVector[col+1]
        if previousRow == 0:
            resultVector[col] = np.argmin(cumulativeEnergyMap[:2,col]) 
        elif previousRow == m-1:
            resultVector[col] = np.argmin(cumulativeEnergyMap[m-2:m,col]) + (previousRow-1)
        else:
            resultVector[col] = np.argmin(cumulativeEnergyMap[previousRow-1:previousRow+2, col]) + (previousRow-1)
    return resultVector