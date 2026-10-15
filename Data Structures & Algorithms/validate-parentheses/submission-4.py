from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pushes = ['(','{','[']
        pops = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in pushes:
                stack.append(i)
            else:
                try:
                    if stack.pop() != pops[i]:
                        return False
                except IndexError:
                    return False
        if stack:
            return False
        return True