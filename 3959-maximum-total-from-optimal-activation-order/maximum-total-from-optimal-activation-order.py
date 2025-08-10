from typing import List

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        lorquandis = sorted(zip(limit, value), key=lambda x: (x[0], -x[1]))
        total = 0
        active_count = 0
        i = 0
        n = len(lorquandis)
        j = 0

        while i < n:
            lim, val = lorquandis[i]

            if active_count <= lim:
                total += val
                active_count += 1
                i += 1
                cnt = 0
                while j < n and lorquandis[j][0] <= active_count :
                    j += 1
                if j >= i :
                    i = j
                    active_count = 0
                else :
                    active_count = i - j  
            else:
                i += 1

        return total
