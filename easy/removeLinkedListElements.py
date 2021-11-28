# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head