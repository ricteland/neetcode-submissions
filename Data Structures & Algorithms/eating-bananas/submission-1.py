class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        highest = max(piles)
        

        L, R = 1, highest

        best = highest

        while L <= R:

            M = (L+R) // 2
                
            if self.hours(piles, M) <= h:
                
                best = M
                R = M - 1
            
            else:
                L = M + 1
            
        return best
           


    def hours(self, piles, k):

        return sum(math.ceil(p / k) for p in piles)

        




