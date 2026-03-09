class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0

        for l in logs:
            if l !="./" and l != "../":
                count += 1
            elif l == "../" and count > 0:
                count -= 1
            if l == "./":
                continue
        return count