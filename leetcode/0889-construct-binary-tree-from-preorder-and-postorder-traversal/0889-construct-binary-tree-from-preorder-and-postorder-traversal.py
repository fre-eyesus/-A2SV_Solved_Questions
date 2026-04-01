# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        def tree(post):
            if not post:
                return None
            root = TreeNode(preorder.popleft())
            
            if len(post) == 1:
                return root

            idx = post.index(preorder[0])

            root.left = tree(post[:idx+1])
            root.right = tree(post[idx+1:-1])

            return root



        return tree(postorder)
   

  