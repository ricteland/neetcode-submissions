class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triples = []
        arr = sorted(nums)

        for curr in range(len(arr)):

            l, r = curr+1, len(arr)-1

            target = arr[curr]

            while l < r:

                if l == curr:

                    l+= 1

                    continue

                elif r == curr:

                    r -= 1

                    continue
                else: 
                    if arr[l] + arr[r] == -arr[curr]:
                        triples.append((arr[l], arr[r], arr[curr]))
                        l += 1
                        r -= 1
                    elif arr[l] + arr[r] + arr[curr] > 0:

                        r -= 1

                    else:

                        l += 1

        result = [list(i) for i in set(triples)]
        return result




        

                
                
                

                

            
            

        