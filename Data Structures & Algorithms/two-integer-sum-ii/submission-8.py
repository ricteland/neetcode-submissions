class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, 1

        while l < len(numbers):
            print(l, r)
            while r < len(numbers):
                
                print(numbers[l], numbers[r])
                if numbers[l] + numbers[r] == target:

                    return [l+1, r+1]
                
                r+=1

            l += 1
            r = l + 1

        
        

        