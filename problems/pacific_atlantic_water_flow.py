class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not len(matrix[0]): return []
        m, n = len(matrix), len(matrix[0])
        p = set([(0, i) for i in range(n)]) | set([(j, 0) for j in range(m)])
        a = set([(m - 1, i) for i in range(n)]) | set([(j, n - 1) for j in range(m)])

        def bfs(si, sj, res, m, n, seen):
            q = [[si, sj]]
            while q:
                i, j = q.pop(0)
                res.add((i, j))
                for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] >= matrix[i][j] and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        q.append([ni, nj])

        seen1, seen2 = set(p), set(a)
        pp, aa = set(p), set(a)
        for pi, pj in pp:
            bfs(pi, pj, p, m, n, seen1)
        for ai, aj in aa:
            bfs(ai, aj, a, m, n, seen2)
        return list(p & a)