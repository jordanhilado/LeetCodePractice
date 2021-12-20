# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return None
    q = [root]
    prev = root
    while q:
        curr = q.pop(0)
        if curr.left is not None: q.append(curr.left)
        if curr.right is not None: q.append(curr.right)
        if curr == prev:
            curr.next = None
            prev = q[-1] if len(q) > 0 else None
        else:
            curr.next = q[0]
    return root