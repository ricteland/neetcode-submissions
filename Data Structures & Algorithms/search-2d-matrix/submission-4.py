class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            print(self.search(row,target), target)
            if self.search(row,target):
                return True

        return False

    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums)-1
        
        while L <= R:

            M = (L+R)//2
            
            if target > nums[M]:
                L = M+1

            elif target < nums[M]:
                R = M-1

            else:
                return True

        return False
