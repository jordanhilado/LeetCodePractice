# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

def isBipartite(self, graph: List[List[int]]) -> bool:
    visited = set()
    two_color = [set(), set()]
    for i in range(len(graph)):
        if i not in visited:
            q = [(i, 0)]
            while q:
                node, level = q.pop()
                visited.add(node)
                two_color[level].add(node)
                for n in graph[node]:
                    if n in two_color[level]:
                        return False
                    if n not in visited:
                        q.append((n, 1 if level == 0 else 0))
    return True