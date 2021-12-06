# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

def detectCycle(self, head: ListNode) -> ListNode:
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while head:
                if head == slow:
                    return head
                head = head.next
                slow = slow.next
    return None