class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []

        for i in path:
            if not i:
                continue
            
            if i == ".":
                continue
            
            if i != "..":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
            
        return "/" + "/".join(stack)

