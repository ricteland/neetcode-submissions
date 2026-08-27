class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []

        def tree(level, curset):

            if level == len(nums):
                print(f'Added set {curset}')
                subsets.append(curset.copy())
                return

            curset.append(nums[level])
            tree(level + 1, curset)

            curset.pop()
            tree(level+1, curset)
        

        tree(0, list())
        return subsets

        
            





