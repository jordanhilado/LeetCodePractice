# 148. Sort List
# https://leetcode.com/problems/sort-list/

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # only one value, or no value at all
    if not head or not head.next:
        return head
    slow, prev, fast = head, None, head
    while fast and fast.next:
        prev = slow
        slow, fast = slow.next, fast.next.next
    prev.next = None
    return self.merge(self.sortList(head), self.sortList(slow))

def merge(self, l1, l2):
    dummy = ListNode(None)
    curr = dummy
    while l1 and l2:
        if l1.val > l2.val:
            curr.next, l2 = l2, l2.next
        else:
            curr.next, l1 = l1, l1.next
        curr = curr.next
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    return dummy.next