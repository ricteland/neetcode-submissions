import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n= len(nums)
        result = [1]*n

        before = 1

        for i in range(n):

            result[i]= before
            before *= nums[i]


        after = 1
        for i in range(n-1, -1, -1):
            result[i] *= after
            after *= nums[i]

        return result