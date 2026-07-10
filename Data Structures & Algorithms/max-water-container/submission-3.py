class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


        L, R = 0, len(heights) -1
        
        best = self.score(L, R, heights)

        while L < R:

            if self.score(L, R, heights) > best:
                best= self.score(L, R, heights)
            
            if heights[L] < heights[R]:

                L += 1

            elif heights[L] >= heights[R]:

                R -= 1

        return best


            



    def score(self, L, R, heights):

        return min(heights[L], heights[R]) * (R-L)