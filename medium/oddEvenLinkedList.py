# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    odd = head
    even = odd.next
    evenStart = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenStart
    return head