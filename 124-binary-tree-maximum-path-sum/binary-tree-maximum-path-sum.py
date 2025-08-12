# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = root.val
        def helper(root ) :
            nonlocal ans
            if not root : return 0

            leftheight = max(helper(root.left )  , 0 )
            rightheigth = max(helper(root.right) , 0 )
            ans = max(ans , leftheight + rightheigth + root.val)
            return max(leftheight , rightheigth) + root.val

        helper(root)
        return ans