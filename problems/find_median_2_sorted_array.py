def find_median_2_array(A, B):

    # O log n method, binary search  log m time, constant space
    # m is the length of the shorter array
    # a = [1, 12, 15, 26, 38]
    # b = [2, 13, 17, 30, 45]
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    target = (m + n + 1) // 2 # target for odd or  target and target+1 for even
    l, r = 0, m
    while l <= r:
        i = (l + r) // 2
        j = target - i

        if i > 0 and A[i-1] > B[j]:
            r = i
        elif i < m and B[j-1] > A[i]:
            l = i + 1
        else:
            m1 = max(A[i-1] if i > 0 else float('-inf'), B[j-1] if j > 0 else float('-inf'))
            if (m + n) % 2:
                return m1
            m2 = min(A[i] or float('inf'), B[j] or float('inf'))
            return (m1 + m2) / 2.0
    return -1



    # 1 2 3  1
    # O(n) method.  n time constant space
    # m, n = len(A), len(B)
    # ctn, mid = 0, (m + n) // 2
    # i = j = prev = 0
    # for __ in range(mid):
    #     if i >= m:
    #         prev = B[j]
    #         i += 1
    #     elif j >= n:
    #         prev = A[i]
    #         i += 1
    #     elif A[i] < B[j]:
    #         prev, i = A[i], i + 1
    #     else:
    #         prev, j = B[j], j + 1
    # print (prev, i, j)
    # if (m + n) % 2:
    #     return prev
    # else:
    #     return (prev + min(A[i] or float('inf'), B[j] or float('inf')))  / 2.

a =[900]
b =[5, 8, 10, 20]
print (find_median_2_array(a,b))