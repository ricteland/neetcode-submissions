class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        sol = [0]*n

        for i in range(n):
            rightmax = -1

            for j in range(i+1, n):
                
                if rightmax < arr[j]:
                    rightmax = arr[j]

            sol[i] = rightmax

        return sol
            
            

            