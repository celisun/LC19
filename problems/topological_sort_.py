import collections
def topologicalSort(A, n):

    graph = collections.defaultdict(list)
    for i, j in A:
        graph[i].append(j)

    def dfs(i, stack, visited, graph):
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                dfs(j, stack, visited, graph)

        stack.insert(0, i)
        print (stack)

    visited = [0] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, stack, visited, graph)

    return stack

test = [[5,2],[5,0],[2,3],[3,1],[4,0],[4,1]]
print (topologicalSort(test, 6))
