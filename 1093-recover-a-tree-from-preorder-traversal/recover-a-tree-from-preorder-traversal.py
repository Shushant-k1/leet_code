# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        st = []
        ind = 0

        while ind < len(traversal) :
            dep = 0
            while ind < len(traversal) and traversal[ind] == "-" :
                dep += 1
                ind += 1
            
            val = 0
            while ind < len(traversal)  and traversal[ind].isdigit() :
                val = val * 10 + int(traversal[ind])
                ind += 1
            
            node = TreeNode(val)

            while len(st) > dep :
                st.pop()
            if st :
                if st[-1].left is None :
                    st[-1].left = node
                else :
                    st[-1].right = node
            st.append(node)
        
        return st[0]