# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    firstNum, secondNum = "", ""
    while l1 or l2:
        if l1:
            firstNum += str(l1.val)
            l1 = l1.next
        if l2:
            secondNum += str(l2.val)
            l2 = l2.next
    total = str(int(firstNum) + int(secondNum))
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