class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = -math.inf

        cursum = 0

        for n in nums:

            cursum = max(cursum, 0)
            cursum += n
            maxsum = max(cursum, maxsum)

        return maxsum
        