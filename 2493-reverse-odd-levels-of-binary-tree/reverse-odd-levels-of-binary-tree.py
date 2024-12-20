# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        rev = False
        while q :
            n = len(q)
            arr = []
            for i in range(n) :
                node = q.popleft()
                if node.left : 
                    q.append(node.left)
                    q.append(node.right)
                if rev :
                    arr.append(node) 
                    if i >= n/2 :
                        arr[i].val , arr[n - i - 1].val = arr[n-i - 1].val , arr[i].val
            rev = not rev
        return root
                
