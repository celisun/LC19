import collections
def get_GC_percentage(A):
    counter = collections.Counter(list(A))
    all = sum(counter.values())
    return (counter['G'] + counter['C']) / all * 1.0

test = 'GATATATAGCATATACTTGAGCCTACTAAC GGG  ATAT  AAA'
# print (get_GC_percentage(test))


sub = 'TATA'
def get_substring(A, sub):
    i, res = 0, []
    while i < len(A):
        if sub not in A[i:]: return res
        idx = A[i:].index(sub)
        res.append(i + idx)
        i += idx + 1
    return res
print (get_substring(test, sub))


classes = [0,1,2,3,4,3,2,1,0]
# [[1,0,0,0,0],[0,1,0,0,0]...]
def one_hot(L):
    res = []
    n_classes = len(set(classes))
    for c in L:
        dummpy = [0] * n_classes
        dummpy[c] = 1
        res.append(dummpy)
    return res

print (one_hot(classes))


