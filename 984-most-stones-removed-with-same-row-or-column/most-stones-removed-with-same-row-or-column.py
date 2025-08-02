class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        group = [-1] * n  # dp-like array: group[i] = component id of i-th stone
        component_id = 0
        
        # Tabular adjacency: store rows and columns
        row_map = {}
        col_map = {}
        
        for i, (x, y) in enumerate(stones):
            row_map.setdefault(x, []).append(i)
            col_map.setdefault(y, []).append(i)

        for i in range(n):
            if group[i] == -1:
                # simulate component marking without DFS/Union-Find
                stack = [i]
                while stack:
                    u = stack.pop()
                    if group[u] != -1:
                        continue
                    group[u] = component_id
                    x, y = stones[u]

                    for nei in row_map[x] + col_map[y]:
                        if group[nei] == -1:
                            stack.append(nei)

                component_id += 1  # next component
        
        # Result: total stones - total components
        return n - component_id
