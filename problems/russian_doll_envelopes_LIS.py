def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    from bisect import bisect_left
    envelopes.sort(key=lambda v: [v[0], -v[1]])
    # sort by aceding in width and descending in height,
    # if tie in width
    # 2 3, 5 4, 6 7, 6 4, 7 5

    # then LIS for the second dimension is the answer
    def LIS(envelopes):  # using bisect
        q = []
        for __, n in envelopes:
            i = bisect_left(q, n)
            if i == len(q):
                q.append(n)
            else:
                q[i] == n
        return len(q)

    def LIS_bs(envelopes):  # using bianry search
        tail = [0] * len(envelopes)
        res = 0
        for __, e in envelopes:
            i, j = 0, res  # search in scope of all possible longest sequence so far
            while i < j:
                mid = (i+j)//2
                if tail[mid] < e:
                    i = mid+1
                else:
                    j = mid
            tail[i] = e
            res = max(res, i+1)  # the longest so far possible
        return res
    return LIS_bs(envelopes)

t1 = [[5,4],[6,4],[6,7],[2,3]]
print (maxEnvelopes(t1))