class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # dfs solution
        if not s: return [s]
        numR = numL = 0
        for char in s:  # minimum removal needed
            if char == "(":
                numL += 1
            elif char == ")":
                if numL > 0:
                    numL -= 1
                else:
                    numR += 1

        # add a lower bound and upper bound, stop dfs when reach
        def dfs(i, maxL, maxR, curr, res, open):
            if maxL < 0 or maxR < 0 or open < 0:
                return
            if i >= len(s):
                if maxL == 0 and maxR == 0 and open == 0:
                    res.add("".join(curr))
                return
            if s[i] == '(':
                dfs(i + 1, maxL, maxR, curr + ['('], res, open + 1)
                dfs(i + 1, maxL - 1, maxR, curr, res, open)
            elif s[i] == ')':
                dfs(i + 1, maxL, maxR - 1, curr, res, open)
                dfs(i + 1, maxL, maxR, curr + [')'], res, open - 1)
            else:
                dfs(i + 1, maxL, maxR, curr + [s[i]], res, open)

        res = set()
        dfs(0, numL, numR, [], res, 0)
        return list(res)

        # # bfs solution
        # # ( )))
        # if not s: return [s]
        # def isValid(S):
        #     numL = 0
        #     for s in S:
        #         if s == "(":
        #             numL += 1
        #         elif s == ")":
        #             numL -= 1
        #             if numL < 0: return False
        #     return numL == 0
        # do = {s}
        # while True:
        #     tmp = filter(isValid, do)
        #     # print do
        #     if tmp:
        #         return tmp
        #     do = {ss[:i] + ss[i+1:] for ss in do for i in range(len(ss)) }
        #     # print do

