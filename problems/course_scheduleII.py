class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        nxt = collections.defaultdict(set)
        for a, b in prerequisites:
            graph[a].add(b)  # check all prerequist, if cleaned
            nxt[b].add(a)
        res = []
        # why bfs not dfs
        # when reach other prerequist, bfs stop, reach other first
        s = [x for x in range(numCourses) if x not in graph]
        while s:
            curr = s.pop(0)
            res.append(curr)  # visit safe
            for ntxx in nxt[curr]:
                graph[ntxx].remove(curr)  # clean current prerequsite
                if not graph[ntxx]: s.append(ntxx)
        return res if len(res) == numCourses else []

