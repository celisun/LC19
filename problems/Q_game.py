class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n: return []

        #  any other locations (p, q) where p + q == x + y or p - q == x - y would be invalid.
        def dfs(i, sums, diffs, cols, curr, res):
            if i == n:
                res.append(curr)
                return
            for j in xrange(n):
                if i + j not in sums and i - j not in diffs and j not in cols:
                    dfs(i + 1, sums | set([i + j]), diffs | set([i - j]), cols | set([j]),
                        curr + ["." * j + "Q" + "." * (n - j - 1)], res)

        res = []
        dfs(0, set(), set(), set(), [], res)
        return res