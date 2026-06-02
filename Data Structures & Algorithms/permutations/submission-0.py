from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = permutations(nums)
        result = [list(i) for i in perms]
        return result


        