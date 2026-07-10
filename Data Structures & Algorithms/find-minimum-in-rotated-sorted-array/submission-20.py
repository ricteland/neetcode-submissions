class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l != r:

            m = (l+r) // 2
            
            if l == m or r == m:

                return min(nums[r], nums[l])
            
            if nums[l] < nums[r]:

                if nums[m] < nums[l]:

                    l = m

                else:
                    r = m

            elif nums[r] < nums[l]:

                if nums[m] < nums[r]:

                    r = m
                    
                else:
                    l = m

        return min(nums)