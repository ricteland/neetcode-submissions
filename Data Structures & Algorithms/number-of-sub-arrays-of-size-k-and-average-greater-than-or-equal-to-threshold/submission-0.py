class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:


        count = 0
        cursum = sum(arr[:k-1])

        L = 0

        for R in range(k-1, len(arr)):
            
            cursum += arr[R]

            if R-L+1 > k:
                
                cursum -= arr[L]
                L += 1
            
            if (cursum/k) >= threshold:

                count += 1

            


        return count