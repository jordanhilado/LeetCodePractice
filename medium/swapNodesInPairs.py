# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = prev = ListNode(0)
    dummy.next = head
    while head and head.next:
        temp = head.next
        head.next = temp.next
        temp.next = head
        prev.next = temp
        head = head.next
        prev = temp.next
    return dummy.next