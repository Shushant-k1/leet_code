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

    def find_max_xor(self, num: int) -> int:
        node = self.root
        max_xor = 0
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
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        max_result = 0
        for num in nums:
            max_result = max(max_result, trie.find_max_xor(num))
        return max_result
