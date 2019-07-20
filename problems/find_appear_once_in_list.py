def find_one(A):
    if not A: return -1
    if len(A) == 1: return A[0]
    lo, hi = 0, len(A)
    while lo <= hi:
        mid = (lo + hi) // 2
        if (mid == 0 or A[mid - 1] != A[mid]) and (mid == len(A)-1 or A[mid] != A[mid + 1]):
            return A[mid]

        if mid % 2 == 0:
            if A[mid] == A[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        else:
            if A[mid] == A[mid - 1]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

# if mid is even ,compare mid an mid + 1, both are smae, then required element is after id
# if mid is odd, compare mid and mid-1, both are same then the required element is after mid,
# i.e. between mid+2 to end. else is before start to mid
test = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
test = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]
# test = [1, 2, 2]
print (find_one(test))
