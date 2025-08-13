# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if type(p) != int and type(q) != int :
            p , q = min(p.val , q.val) , max(p.val , q.val)

        if root.val == p or root.val == q : return root

        if root.val >p and root.val < q : return root

        if root.val > p and root.val > q :
            return self.lowestCommonAncestor(root.left , p , q)
        
        return self.lowestCommonAncestor(root.right , p , q)