class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ['+', '-', '*', '/']
        stack = []

        for item in tokens:

            if item not in ops:
                stack.append(int(item))

            elif item in ops:

                if item == "+":

                    s = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(s)

                elif item == "-":

                    s = stack[-2] - stack[-1]

                    stack.pop()
                    stack.pop()
                    stack.append(s)

                elif item == "*":

                    s = stack[-2] * stack[-1]

                    stack.pop()
                    stack.pop()
                    stack.append(s)

                elif item == "/":
                    

                    s = int(float(stack[-2] / stack[-1]))

                    stack.pop()
                    stack.pop()
                    stack.append(s)
                    

        return stack[0]
        