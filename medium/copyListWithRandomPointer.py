# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = { None : None }
    curr = head
    while curr:
        copy = Node(curr.val) # create deep copy of node
        oldToCopy[curr] = copy # map old node to copy node
        curr = curr.next # iterate
    curr = headw 
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
    return oldToCopy[head]