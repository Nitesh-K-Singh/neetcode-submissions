from collections import defaultdict, deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

        def neighbors(r, c):
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        def cell(r, c): return r * n + c

        graph  = defaultdict(list)
        rgraph = defaultdict(list)

        for r in range(m):
            for c in range(n):
                for nr, nc in neighbors(r, c):
                    if heights[r][c] >= heights[nr][nc]:
                        graph[cell(r,c)].append(cell(nr,nc))
                        rgraph[cell(nr,nc)].append(cell(r,c))

        visited = [False] * (m * n)
        finish_order = []

        def dfs1(start):
            stack = [(start, False)]
            while stack:
                node, returning = stack.pop()
                if returning:
                    finish_order.append(node)
                    continue
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, True))
                for nb in graph[node]:
                    if not visited[nb]:
                        stack.append((nb, False))

        for r in range(m):
            for c in range(n):
                if not visited[cell(r, c)]:
                    dfs1(cell(r, c))

        scc_id   = [-1] * (m * n)
        scc_list = []

        def dfs2(start, sid):
            stack = [start]
            while stack:
                node = stack.pop()
                if scc_id[node] != -1:
                    continue
                scc_id[node] = sid
                scc_list[sid].append(node)
                for nb in rgraph[node]:
                    if scc_id[nb] == -1:
                        stack.append(nb)

        for node in reversed(finish_order):
            if scc_id[node] == -1:
                scc_list.append([])
                dfs2(node, len(scc_list) - 1)

        num_scc = len(scc_list)

        dag        = defaultdict(set)
        rdag       = defaultdict(set)
        out_degree = [0] * num_scc

        for u in range(m * n):
            for v in graph[u]:
                su, sv = scc_id[u], scc_id[v]
                if su != sv and sv not in dag[su]:
                    dag[su].add(sv)
                    rdag[sv].add(su)
                    out_degree[su] += 1

        pacific_border  = set()
        atlantic_border = set()

        for r in range(m):
            pacific_border.add(scc_id[cell(r, 0)])
            atlantic_border.add(scc_id[cell(r, n-1)])
        for c in range(n):
            pacific_border.add(scc_id[cell(0, c)])
            atlantic_border.add(scc_id[cell(m-1, c)])

        reaches_pacific  = [sid in pacific_border  for sid in range(num_scc)]
        reaches_atlantic = [sid in atlantic_border for sid in range(num_scc)]

        queue = deque(sid for sid in range(num_scc) if out_degree[sid] == 0)

        while queue:
            sid = queue.popleft()
            for parent in rdag[sid]:
                if reaches_pacific[sid]:
                    reaches_pacific[parent] = True
                if reaches_atlantic[sid]:
                    reaches_atlantic[parent] = True
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)

        result = []
        for r in range(m):
            for c in range(n):
                sid = scc_id[cell(r, c)]
                if reaches_pacific[sid] and reaches_atlantic[sid]:
                    result.append([r, c])

        return result