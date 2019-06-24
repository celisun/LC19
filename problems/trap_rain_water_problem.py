def trap_water(A):
    # n = len(A)
    # left = [0] * n
    # right = [0] * n
    # water = 0
    # left[0], right[-1] = A[0], A[-1]
    # for i in range(1, n):
    #     left[i] = max(left[i-1], A[i])
    # print (left)
    # for j in range(n-2, -1, -1):
    #     right[j] = max(right[j+1], A[j])
    # print (right)
    # for i in range(n):
    #     water += max(0, min(left[i], right[i]) - A[i])
    #
    # return water

    n, water  = len(A), 0
    lo, hi = 0, n-1
    lmax = rmax = 0
    while lo <= hi:   # both approach compute each cell'water one by one.
        if A[lo] < A[hi]:  # smaller post at left, count and move
            if A[lo] > lmax:
                lmax = A[lo]
            else:
                water += lmax - A[lo]
                lo += 1
        else:   # other sise
            if A[hi] > rmax:
                rmax = A[hi]
            else:
                water += rmax - A[hi]
                hi -= 1
    return water
test = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trap_water(test)
print (res)