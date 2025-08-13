# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        if not root :
            return TreeNode(val)
            return 
        
        if root.val > val :
            self.insertIntoBST(root.left, val)
            if root.left is None :
                root.left = TreeNode(val)
        elif root.val < val :
            self.insertIntoBST(root.right , val)
            if root.right is None :
                    root.right = TreeNode(val)
        

        return root