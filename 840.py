import numpy as np

NUMS = set(range(1, 10))


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        npgrid = np.array(grid)
        height, width = npgrid.shape
        counter = 0
        for i in range(height):
            for j in range(width):
                subgrid = npgrid[i : i + 3, j : j + 3]
                if (
                    subgrid.shape == (3, 3)
                    and set(subgrid.flatten()) == NUMS
                    and sum(subgrid[0])
                    == sum(subgrid[1])
                    == sum(subgrid[2])
                    == sum(subgrid[::, 0])
                    == sum(subgrid[::, 1])
                    == sum(subgrid[::, 1])
                    == sum(subgrid.diagonal())
                    == sum(subgrid[::-1, ::-1].diagonal())
                ):
                    counter += 1
        return counter
