class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {"[": "]", "{": "}", "(": ")"}

        stack = []

        for i in s:

            if i in mapping:

                stack.append(i)

            else:
                
                if not stack:
                    return False

                elif i == mapping[stack[-1]]:
                    stack.pop()
                
                else:
                    return False

        return stack == []

