class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for _ in range(len(nums)):
            print(f'{nums}, {i}')
            if nums[i] == val:
                nums.pop(i)
                i-=1
            i+= 1
        
        return len(nums)