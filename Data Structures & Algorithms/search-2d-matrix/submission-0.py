class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tolist = []

        for row in matrix:
            tolist.extend(row)

        return target in tolist