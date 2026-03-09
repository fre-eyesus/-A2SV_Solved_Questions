class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for st in s:
            if stack and st == "*" :
                stack.pop()
            else:
                stack.append(st)
        return ''.join(stack)
