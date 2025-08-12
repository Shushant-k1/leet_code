# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root ) :
            nonlocal ans
            if not root : return 0

            leftheight = helper(root.left ) 
            rightheigth = helper(root.right) 
            ans = max(ans , leftheight + rightheigth)
            return max(leftheight , rightheigth) + 1
        helper(root)
        return ans