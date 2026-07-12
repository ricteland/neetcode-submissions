class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minlen = math.inf

        L = 0
        cursum = 0

        for R in range(len(nums)):

            cursum += nums[R]
            
            while cursum >= target:

                minlen = min(R-L+1, minlen)
                cursum -= nums[L]
                L+= 1

        return 0 if minlen == math.inf else minlen