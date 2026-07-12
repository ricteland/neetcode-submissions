class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        counts = Counter(s1)

        L = 0


        for R in range(k-1, len(s2)):
            
            if R-L+1 > k:

                L += 1

            

            perm = Counter(s2[L:R+1])
            print(perm)

            if perm == counts:

                return True

        return False
