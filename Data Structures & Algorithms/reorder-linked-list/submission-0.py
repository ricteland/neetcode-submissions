# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head.next, head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

        # first = None
        # second = head

        # while second != slow:

        #     tmp = second.next
        #     second.next = first
        #     first = second
        #     second = tmp

        first = None
        second = slow.next
        slow.next = None
        while second:

            temp = second.next
            second.next = first
            first = second
            second = temp

        start = head
        end = first

        while end:

            tmp_start, tmp_end = start.next, end.next

            start.next = end
            end.next = tmp_start

            end = tmp_end
            start = tmp_start

