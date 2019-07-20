a = [1,2,5,7,8, 10]
b = [1,3,7,10]
c = [10]


def find_common_3(a, b, c):
    if not a or not b or not c: return -1
    m, n, p = len(a), len(b), len(c)
    i = j = k = 0
    while i < m and j < n and k < p:
        if a[i] == b[j] == c[k]:
            return a[i]
        maxn = max(a[i], b[j], c[k])
        if b[j] == maxn:  # swap, a to be max
            a, b, i, j, m, n = b, a, j, i, n, m
        elif c[k] == maxn:
            a, c, i, k, m, p = c, a, k, i, p, m
        while j < n and b[j] < a[i]: 
            j += 1
        while k < p and c[k] < a[i]:
            k += 1
    return -1


print (find_common_3(a,b,c))
