# 143. Reorder List
# https://leetcode.com/problems/reorder-list/

def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = fast = start = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        start = slow.next
    slow.next = None
    l1, l2 = head, self.reverse(start)
    while l2 is not None:
        y = l2.next
        x = l1.next
        l1.next = l2
        l2.next = x
        l1 = x
        l2 = y
        
    
def reverse(self, start):
    prev, curr, nex = None, start, None
    while curr is not None:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    return prev