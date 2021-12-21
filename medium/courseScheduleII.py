# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

#################### DFS SOLUTION ####################
class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adjacency list representation of the graph
        adjList = defaultdict(list)
        # [a, b] = b -> a
        for dest, src in prerequisites:
            adjList[src].append(dest)
        ans = []
        possible = True
        # by default, all vertices are white
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal possible
            # return if cycle is FOUND
            if not possible:
                return
            # start recursion
            color[node] = Solution.GRAY
            # traverse on neighboring vertices
            if node in adjList:
                for neighbor in adjList[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        # an edge to a gray vertex == CYCLE
                        possible = False
            # recursion ends, we mark as black
            color[node] = Solution.BLACK
            ans.append(node)
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return ans[::-1] if possible else []

#################### KAHN'S ALGORITHM SOLUTION ####################
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # prepare the graph
    adjList = defaultdict(list)
    indegree = {}
    for dest, src in prerequisites:
        adjList[src].append(dest)
        # record each node's in-degree
        indegree[dest] = indegree.get(dest, 0) + 1
    # queue for maintaining list of nodes that have 0 in-degree
    zeroIndegree = deque([k for k in range(numCourses) if k not in indegree])
    ans = []
    # until there are nodes in the Q
    while zeroIndegree:
        # pop one node with 0 in-degree
        vertex = zeroIndegree.popleft()
        ans.append(vertex)
        # reduce in-degree for all the neighbors
        if vertex in adjList:
            for neighbor in adjList[vertex]:
                indegree[neighbor] -= 1
                # add neighbor to Q if in-degree becomes 0
                if indegree[neighbor] == 0:
                    zeroIndegree.append(neighbor)
    return ans if len(ans) == numCourses else []