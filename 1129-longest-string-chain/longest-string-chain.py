from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]

            max_length = 1  # chain length including current word

            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in word_set:
                    length = 1 + dfs(predecessor)
                    max_length = max(max_length, length)

            memo[word] = max_length
            return max_length

        max_chain = 1
        for w in words:
            max_chain = max(max_chain, dfs(w))

        return max_chain
