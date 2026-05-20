class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        done = 0

        while done < len(arr) - 1:
            
            right = arr[done+1:]
            arr[done] = max(right)

            done += 1
        arr[-1] = -1

        return arr
            
            

            