# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False