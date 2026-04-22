# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return True,float('inf'), float('-inf'),0
            
            leftBst, leftMin, leftMax, leftSum = dfs(node.left)
            rightBst, rightMin, rightMax, rightSum = dfs(node.right) 

            if leftBst and rightBst and leftMax < node.val < rightMin:

                curSum = leftSum + rightSum + node.val

                self.ans = max(curSum, self.ans)

                return True, min(leftMin, node.val), max(rightMax, node.val), curSum
            return False, 0, 0, 0

        dfs(root)

        return self.ans