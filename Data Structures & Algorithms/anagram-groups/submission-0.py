from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for word in strs:

            count = [0]*26
            for c in word:
                count[ord(c) - ord("a")] += 1
            answer[str(count)].append(word)

        return list(answer.values())


