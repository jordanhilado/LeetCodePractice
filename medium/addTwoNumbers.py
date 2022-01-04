# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

#################### Faster Solution ####################

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    firstNum, secondNum = "", ""
    while l1 or l2:
        if l1:
            firstNum += str(l1.val)
            l1 = l1.next
        if l2:
            secondNum += str(l2.val)
            l2 = l2.next
    total = str(int(firstNum[::-1]) + int(secondNum[::-1]))[::-1]
    head = ListNode()
    newList = head
    for i, num in enumerate(total):
        if i == 0:
            newList.val = int(num)
        else:
            x = ListNode(int(num))
            newList.next = x
            newList = newList.next
    return head

#################### Non-optimized Solution ####################

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(prev, curr, nex):
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
    l1 = reverse(None, l1, None)
    l2 = reverse(None, l2, None)
    firstNum, secondNum = "", ""
    while l1 or l2:
        if l1:
            firstNum += str(l1.val)
            l1 = l1.next
        if l2:
            secondNum += str(l2.val)
            l2 = l2.next
    total = str(int(firstNum) + int(secondNum))[::-1]
    head = ListNode()
    newList = head
    for i, num in enumerate(total):
        if i == 0:
            newList.val = int(num)
        else:
            x = ListNode(int(num))
            newList.next = x
            newList = newList.next
    return head