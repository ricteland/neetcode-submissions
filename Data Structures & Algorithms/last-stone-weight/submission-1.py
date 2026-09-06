import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            
            battle = heapq.nsmallest(2, heap)

            x, y = battle[0], battle[1]

            if x == y:

                heapq.heappop(heap)
                heapq.heappop(heap)

            else:

                new = x - y
                heapq.heappop(heap)
                heapq.heappop(heap)
                heapq.heappush(heap, new)

        
        return (heap[0] * -1) if heap else 0