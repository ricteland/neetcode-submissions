class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []

        def combine(temp, idx):

            if idx == len(nums):
                return

            if sum(temp) == target:
                
                # print(f'Added {temp}')
                res.append(temp.copy())
                return

            if sum(temp) > target:

                return

            #Case where we add same number:
            temp.append(nums[idx])
            combine(temp, idx)

            #Case where we add next number:
            temp.pop()
            combine(temp, idx+1)

            

            

        combine([], 0)
        return res
        