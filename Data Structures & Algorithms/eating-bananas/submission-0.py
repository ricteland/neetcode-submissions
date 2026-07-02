class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        highest = max(piles)
        

        L, R = 1, highest

        best = highest   # maximum possible k
        while L <= R:
            M = (L + R) // 2
            if self.hours(piles, M) <= h:
                best = M          # record candidate speed
                R = M - 1         # try to find a smaller speed
            else:
                L = M + 1         # need to eat faster
        return best


    def hours(self, piles, k):

        return sum(math.ceil(p / k) for p in piles)

        




