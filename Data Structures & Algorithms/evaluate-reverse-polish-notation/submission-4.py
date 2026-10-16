from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ['+','-','*','/']
        temp1, temp2 = 0, 0
        for i in tokens:
            # print(i, stack)
            if i in operators:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if i == '+':
                    stack.append(temp1 + temp2)
                elif i == '-':
                    stack.append(temp2 - temp1)
                elif i == '*':
                    stack.append(temp1 * temp2)
                else:
                    stack.append(int(temp2 / temp1))
            else:
                stack.append(int(i))
        return int(stack.pop())