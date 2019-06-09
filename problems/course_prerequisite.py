class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        wait = collections.defaultdict(set)
        visited = [0] * numCourses

        def dfs(i, visited):  # if cycle
            if visited[i] == 1: return True  # haved checked and pass
            if visited[i] == -1: return False
            visited[i] = -1
            for pre in wait[i]:
                if not dfs(pre, visited): return False
            visited[i] = 1
            return True

        # detect deadlock
        for a, b in prerequisites:
            wait[a].add(b)  # after b, if no other prequi for a, safe to visit a
        for i in range(numCourses):
            if not dfs(i, visited): return False
        return True

