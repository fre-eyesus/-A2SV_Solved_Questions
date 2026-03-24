# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.check(root)

    def check(self,r):
        # check no node
        if r is None:
            return 0
        # check if both left and right doesnt exist
        if not r.left and not r.right:
            return 1
        # if left misses
        if not r.left:
            return 1 + self.check(r.right)
        # if right misses
        if not r.right:
            return 1 + self.check(r.left)

        
        return 1 + min(self.check(r.left), self.check(r.right))


        
        
        