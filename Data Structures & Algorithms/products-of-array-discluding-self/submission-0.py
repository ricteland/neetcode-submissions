import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []

        for i in range(0, len(nums)):

            others = nums.copy()
            others.pop(i)

            out.append(math.prod(others))

        return out