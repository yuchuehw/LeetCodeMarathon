class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*i for i in range(1,101)]
        tower[0][0] = poured
        for i, row in enumerate(tower[:-1]):
            for j in range(len(row)):
                if row[j] > 1:
                    over = row[j]-1
                    tower[i+1][j] += over/2
                    tower[i+1][j+1] += over/2
                    row[j] = 1
                if i==query_row and j==query_glass:
                    return tower[query_row][query_glass]
        return 0
        
