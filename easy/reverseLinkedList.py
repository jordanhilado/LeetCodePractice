# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr, nextNode = None, head, None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev