# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minSwap(self , arr, n):

        ans = 0
        temp = arr.copy()
        h = {}

        temp.sort()

        for i in range(n):

            h[arr[i]] = i

        init = 0

        for i in range(n):
            if (arr[i] != temp[i]):
                ans += 1
                init = arr[i]

                arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

                h[init] = h[temp[i]]
                h[temp[i]] = i

        return ans

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        pq = deque()
        pq.append([root,0])
        ans = 0
        while pq :
            cur = []
            for i in range(len(pq)) :
                ele , lev = pq.popleft()
                if ele.left :
                    pq.append([ele.left , lev + 1])
                    cur.append(ele.left.val)
                if ele.right :
                    pq.append([ele.right , lev + 1])
                    cur.append(ele.right.val)
            ans += self.minSwap(cur , len(cur))
        return ans
                