# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(root,res)
        
        return res
    def postorder(self, root, res):
        if root is not None:
            self.postorder(root.left,res)
            self.postorder(root.right,res)
            res.append(root.val)
    