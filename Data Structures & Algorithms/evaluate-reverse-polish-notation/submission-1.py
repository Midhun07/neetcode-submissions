from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # all operands are integers
        stack = deque()

        operators = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '/': lambda a, b: a/b,
            '*': lambda a, b: a*b
        }

        for i in range(len(tokens)):
            if tokens[i] in operators.keys():
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[tokens[i]](int(a), int(b)))
            else:
                stack.append(tokens[i])

        return int(stack.pop())
        