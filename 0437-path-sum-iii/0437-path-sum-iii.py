# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

        self.numOfPaths = 0
        self.dfs(root, targetSum)
        return self.numOfPaths
    
    def dfs(self, node, targetSum):
        if node is None:
            return 
        self.test(node, targetSum)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)
        
    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)