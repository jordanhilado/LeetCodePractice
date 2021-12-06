# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head