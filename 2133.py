import numpy as np
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        npmatrix = np.array(matrix)
        n = len(matrix)
        return all(len(set(npmatrix[i]))==n and len(set(npmatrix[::,i]))==n for i in range(n))
            
