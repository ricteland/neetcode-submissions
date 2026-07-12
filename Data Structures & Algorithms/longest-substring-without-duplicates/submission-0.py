class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = set()
        
        bestcount = 0

        L = 0

        for R in range(len(s)):

            while s[R] in hashmap:

                hashmap.remove(s[L])
                L += 1

            bestcount = max(bestcount, R-L+1)
            

            hashmap.add(s[R])

        return bestcount