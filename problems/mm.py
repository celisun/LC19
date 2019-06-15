def sort(A):
    if not A: return A
    curr = 0
    for i, a in enumerate(A):
        if a == 0:
            if A[curr]: A[curr], A[i] = A[i], A[curr]
            curr += 1
    return A

t1 = [0,1,0,0,1,0,0,0,1,1]
t2 = [0,0,0]
t3 = [1,1,1]
t4 = [1,0,1,1,0]
print (sort(t1))
print (sort(t2))
print (sort(t3))
print (sort(t4))
