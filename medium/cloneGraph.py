# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return
    d = {node:Node(node.val)}
    stack = [node]
    while stack:
        curr = stack.pop()
        for i in curr.neighbors:
            if i not in d:
                d[i] = Node(i.val)
                stack.append(i)
            d[i].neighbors.append(d[curr])
    return d[node]