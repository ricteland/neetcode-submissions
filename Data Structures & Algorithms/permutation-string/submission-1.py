class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        counts = Counter(s1)
        rolling = Counter(s2[:k-1])
        L = 0


        for R in range(k-1, len(s2)):
            
            rolling[s2[R]] += 1

            if R-L+1 > k:

                rolling[s2[L]] -= 1
                L += 1

            print(rolling)
            if rolling == counts:
                
                return True

            
        return False
