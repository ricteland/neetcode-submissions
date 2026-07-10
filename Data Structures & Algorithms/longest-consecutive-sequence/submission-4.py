class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)

        longest = 0

        if not nums:
            return 0

        for i in numset:
            if i - 1 not in numset:
                curr = i
                l = 1

                while curr + 1 in numset:
                    curr += 1
                    l += 1

                longest = max(longest, l)

        return longest    