# 86. Partition List
# https://leetcode.com/problems/partition-list/
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # create two linked lists
    head1 = list1 = ListNode(0)
    head2 = list2 = ListNode(0)
    # while there are nodes to iterate through
    while head:
        # if the current value is less than x,
        # we are going to add it to the first list
        if head.val < x:
            list1.next = head
            list1 = list1.next
        # if the current value is greater than or equal to x,
        # we are going to add it to the second list
        else:
            list2.next = head
            list2 = list2.next
        head = head.next
    # connect the lists together
    list2.next = None
    list1.next = head2.next
    return head1.next