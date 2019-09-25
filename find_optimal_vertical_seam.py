import numpy as np

def find_optimal_vertical_seam(cumulativeEnergyMap):
    m, n = cumulativeEnergyMap.shape
    resultVector = np.zeros((m,), dtype=np.uint32)
    resultVector[-1] = np.argmin(cumulativeEnergyMap[-1])
    for row in range(m-2, -1, -1):
        previousColumn = resultVector[row +1]
        if previousColumn == 0:
            resultVector[row] = np.argmin(cumulativeEnergyMap[row,:2])
        elif previousColumn == n-1:
            resultVector[row] = np.argmin(cumulativeEnergyMap[row,n-2:n]) + (previousColumn-1)
        else:
            resultVector[row] = np.argmin(cumulativeEnergyMap[row, previousColumn-1:previousColumn+2]) + (previousColumn-1)
    return resultVector