class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == 'D':
                score.append(2*score[-1])

            elif i == "+":
                score.append(score[-1] + score[-2])

            elif i == "C":
                score.pop()
            
            else:
                score.append(int(i)) 

        print(score)
        return sum(score)