from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, des, dist in roads:
            adj[src].append((des,dist))
            adj[des].append((src,dist))
        def dfs(node):
            if node in visted:
                return
            visted.add(node)
            nonlocal res
            for des, dist in adj[node]:
                res=min(res,dist)
                dfs(des)
        visted=set()
        res=float("inf")
        dfs(1)
        return res