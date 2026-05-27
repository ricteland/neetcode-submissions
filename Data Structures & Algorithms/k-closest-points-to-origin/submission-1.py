class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []

        def dist(x, y):
            return (x**2 + y**2)

        dists = [(dist(i[0], i[1]), i) for i in points]

        topk = sorted(dists, key = lambda x: x[0])[:k]

        return [i[1] for i in topk]
        

                
            
