# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        def tree(preorder,inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = tree(preorder, inorder[:idx])
                root.right = tree(preorder, inorder[idx+1:])

                return root
        return tree(preorder,inorder)

      
