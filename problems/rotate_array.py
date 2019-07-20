def rotate_array(A, n):

    # 1 2 3 4 5
    # 3 4 5 1 2
    n %= len(A)
    m = len(A)
    # O (m) time, constant space
    for i in range(n):
        tmp = A[i]
        j = i + n
        while j < m:
            A[j-n] = A[j]
            j += n
        A[j - n] = tmp

    # O m * n time, O 1 space
    # def rotate_1(A):
    #     if len(A) <= 1: return
    #     tmp = A[0]
    #     for i in range(1, len(A)):
    #         A[i-1] = A[i]
    #     A[-1] = tmp
    #
    # for __ in range(n): rotate_1(A)

    # get a copy, not in place n time n space
    print (A)

test = [1, 2, 3, 4, 5, 6, 7 ]
#       3  4  5  6  7  1  2
rotate_array(test, 2)

