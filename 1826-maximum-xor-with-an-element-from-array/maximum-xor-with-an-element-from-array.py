class TrieNode:
    def __init__(self):
        self.children = [None] * 2

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for i in range(31, -1, -1):  # 32-bit number
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def max_xor(self, num: int) -> int:
        node = self.root
        max_xor = 0
        if not node.children[0] and not node.children[1]:
            return -1 
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if node.children[toggled_bit]:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children[bit]
        return max_xor
    
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        queries.sort(key=lambda x: x[1])  

        trie = Trie()
        res = [-1] * len(queries)
        idx = 0 

        for x, m, q_idx in queries:
            while idx < len(nums) and nums[idx] <= m:
                trie.insert(nums[idx])
                idx += 1
            res[q_idx] = trie.max_xor(x)

        return res
