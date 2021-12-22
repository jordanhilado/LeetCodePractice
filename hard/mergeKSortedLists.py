# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # helper function to merge two linked lists
    def merge(headA, headB):
        dummyNode = ListNode(0)
        tail = dummyNode
        while True:
            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break
            if headA.val <= headB.val:
                tail.next = headA
                headA = headA.next
            else:
                tail.next = headB
                headB = headB.next
            tail = tail.next
        return dummyNode.next
    # handle base cases
    if not lists:
        return None  
    if len(lists) == 1: 
        return lists[0]
    if len(lists) == 2:
        return merge(lists[0], lists[1])
    # set left, right and mid pointers
    left, right = 0, len(lists)-1
    mid = (left+right) // 2
    leftSide = lists[:mid]
    rightSide = lists[mid:]
    # divide and conquer
    leftDone = self.mergeKLists(leftSide)
    rightDone = self.mergeKLists(rightSide)
    return merge(leftDone, rightDone)