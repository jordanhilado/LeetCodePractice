# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    prev, curr, pos = None, head, 1
    # set prev to left of "left" node
    while pos != left:
        prev = curr
        curr = curr.next
        pos += 1
    # set start to prev
    # set end to "left" node, which after reversing will be the actual end
    start, end = prev, curr
    # reverse the nodes between "left" and "right"
    while pos != right + 1:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        pos += 1
    # connect the remaining part of the LL
    end.next = curr
    # if the "left" node is not the first node of the LL
    if start:
        start.next = prev
        return head
    return prev