class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        m, n = len(board), len(board[0])

        def dfs(i, j, word, board):
            if not word: return True
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[0]: return False

            tmp, board[i][j] = board[i][j], '#'
            res = dfs(i + 1, j, word[1:], board) or dfs(i - 1, j, word[1:], board) \
                  or dfs(i, j - 1, word[1:], board) or dfs(i, j + 1,
                                                                                                        word[1:], board)
            board[i][j] = tmp
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word, board): return True
        return False
