import collections

class Solution(object):
    def criticalConnections(self, n, connections):
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for u, v in connections:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        graph = makeGraph(connections)
        connections = set(frozenset((u, v)) for u, v in connections)
        rank = [-2] * n  # -2 means unvisited

        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth
            min_back_depth = n  # Max possible depth

            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # Skip parent node
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(frozenset((node, neighbor)))
                min_back_depth = min(min_back_depth, back_depth)

            return min_back_depth

        dfs(0, 0)

        # Convert frozensets back to list format
        return [list(edge) for edge in connections]
