class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.lookup = {}
        for row,i in enumerate(self.matrix):
            for col1,j in enumerate(i):
                rowSum = 0
                for col2,k in enumerate(i[col1:]):
                    rowSum += k
                    self.lookup[str(row)+'#'+str(col1)+'#'+str(col1+col2)] = rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionSum = 0    
        for i in range(row1, row2+1):
            regionSum += self.lookup[str(i)+'#'+str(col1)+'#'+str(col2)]
        return regionSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)