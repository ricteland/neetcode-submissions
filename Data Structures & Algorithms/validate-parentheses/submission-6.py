class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        openers = ["[", "{", "("]
        closers = ["]", "}", ")"]
        mapping = {"[": "]", "{": "}", "(": ")"}

        stack = []

        for i in s:

            if i in openers:

                stack.append(i)

            else:
                
                if not stack:
                    return False

                elif i == mapping[stack[-1]]:
                    stack.pop()
                
                else:
                    return False

        return stack == []

