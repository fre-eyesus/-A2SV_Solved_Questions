# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      
        if not subRoot:
            return True
        if not root:
            return False
        
        if root.val == subRoot.val and self.check(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def check(self, r,sub):
        if not sub and not r :
            return True
        if not r or not sub:
            return False
        if r.val != sub.val:
            return False
        return self.check(r.left, sub.left) and self.check(r.right, sub.right)
