class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        colors = [0, 1, 2]

        for i in nums:
            buckets[i] += 1

        
        idx = 0
        
        for i in colors:
            for j in range(buckets[i]):
                nums[idx] = i
                idx += 1


        