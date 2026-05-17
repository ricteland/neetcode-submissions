class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            d = target-nums[i]

            if d in nums:
                j = nums.index(d)
                if i != j:
                    return sorted([i,j])