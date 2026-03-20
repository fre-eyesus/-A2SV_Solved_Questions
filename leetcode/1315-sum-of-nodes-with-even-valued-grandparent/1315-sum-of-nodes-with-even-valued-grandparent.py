# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        def solve(root, par, gpar):
            if not root:
                return
            if gpar and gpar.val % 2 == 0:
                self.ans += root.val
            
            solve(root.left, root, par)
            solve(root.right, root, par)

        solve(root, None, None)
        return self.ans