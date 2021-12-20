# 863. All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    def convert(node, parent, g):
        if not node:
            return
        if parent:
            g[node].append(parent)
        if node.right:
            g[node].append(node.right)
            convert(node.right, node, g)
        if node.left:
            g[node].append(node.left)
            convert(node.left, node, g)
    g = defaultdict(list)
    vis, q, res = set(), deque(), []
    convert(root, None, g)
    q.append((target, 0))
    while q:
        n, d = q.popleft()
        vis.add(n)
        if d == k:
            res.append(n.val)
        for i in g[n]:
            if i not in vis:
                q.append((i, d+1))
    return res