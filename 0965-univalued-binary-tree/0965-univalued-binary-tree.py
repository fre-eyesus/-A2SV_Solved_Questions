# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        num = root.val
        # def dfs(root):
        #     if not root:
        #         return True 
        #     if root.val != num:
        #         return False
            
        
        #     return  dfs(root.left) and dfs(root.right)

        # return dfs(root)

        q = deque([root])
        while q:

            node = q.popleft()

            if node.val != num:
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return True

    