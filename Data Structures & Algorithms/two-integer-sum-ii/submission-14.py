class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers) 
        l, r = 0, n - 1

        while l < r:

            print(numbers[l], numbers[r] )
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]


            difflup = (numbers[l+1] + numbers[r]) - target
            diffrdown = (numbers[r-1] + numbers[l]) - target
            print(difflup, diffrdown)
            if abs(difflup) < abs(diffrdown):
                l+=1
            
            else:
                r-=1

        
        

        