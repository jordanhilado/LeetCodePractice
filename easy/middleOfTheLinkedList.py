# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow