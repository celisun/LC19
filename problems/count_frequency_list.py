def count_freq(A):
    if not A: return
    n = len(A)
    # count how many numbers of n
    # index use A[i]%n
    i = 0
    while i < n:
        if A[i] <= 0:
            i += 1
            continue

        idx = A[i] - 1
        if A[idx] > 0:
            A[i], A[idx] = A[idx], -1
        else:
            A[idx] -= 1
            A[i] = 0
            i += 1
    # for i in range(n):
    #     A[i] -= 1
    # for j, v in enumerate(A):
    #     A[v % n] += n
    for i, m in enumerate(A):
        print(str(i+1)+" :  "+str(abs(m)))

test = [1]
count_freq(test)