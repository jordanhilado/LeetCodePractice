# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # fast and slow pointer, slow becomes middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    # reverse the second half of the LL
    while slow:
        nextNode = slow.next
        slow.next = prev
        prev = slow
        slow = nextNode
    # compare the reversed second half (which starts at prev), with the first half, which starts at head
    while prev:
        # compare the values
        if prev.val != head.val:
            return False
        # iterate
        prev = prev.next
        head = head.next
    return True