class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target: return []
        candidate = sorted(candidates)

        def search(i, num, curr, res):
            if not num:
                res.append(curr)
                return
            for j in range(i, len(candidate)):
                if candidate[j] > num: break
                search(j, num - candidate[j], curr + [candidate[j]], res)

        res = []
        search(0, target, [], res)
        return res


