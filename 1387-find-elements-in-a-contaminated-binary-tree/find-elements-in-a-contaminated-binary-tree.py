# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen


    def bfs(self , root:TreeNode) -> None :
        queue = [root]
        root.val = 0

        while queue :
            cur_node = queue.pop(0)
            self.seen.add(cur_node.val)
            if cur_node.left :
                cur_node.left.val = cur_node.val * 2 + 1
                queue.append(cur_node.left)
            if cur_node.right :
                cur_node.right.val = cur_node.val * 2 + 2
                queue.append(cur_node.right)
            
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)