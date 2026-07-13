class Solution:
    def trap(self, height: List[int]) -> int:
        
        fromleft, fromright = [0] * len(height), [0] * len(height)

        hleft = 0

        for i, n in enumerate(height):

            hleft = max(n, hleft)
            fromleft[i] = hleft
        
        hright = 0

        for i, n in enumerate(height[::-1]):

            hright = max(n, hright)
            fromright[i] = hright

        fromright = fromright[::-1]
        
        avail = [0] * len(height)

        for i, n in enumerate(height):

            avail[i] = min(fromleft[i], fromright[i]) - height[i]

        return sum(avail)