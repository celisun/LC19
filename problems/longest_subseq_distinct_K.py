import  collections

def longest_subsq_distinct_K(S, K):
    counter = collections.Counter()
    res, k = "", 0
    i = 0
    for j, s in enumerate(S):
        if s in counter:
            counter[s] += 1
            res = max(res, S[i:j+1], key=len)
        else:
            if k == K: res = max(res, S[i:j], key=len)
            while k == K:
                counter[S[i]] -= 1
                if counter[S[i]] == 0:
                    del counter[S[i]]
                    k -= 1
                i += 1
            counter[s] += 1
            k += 1

    return res
test = "aabacbebebe"
print (longest_subsq_distinct_K(test, 3))
