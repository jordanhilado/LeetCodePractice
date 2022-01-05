# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None
    A, B = headA, headB
    while A is not B:
        if A is None:
            A = headB
        else:
            A = A.next
        if B is None:
            B = headA
        else:
            B = B.next
    return A