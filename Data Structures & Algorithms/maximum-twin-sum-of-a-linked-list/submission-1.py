# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        best = -math.inf


        #Find halfway point of linked list
        mid, fast = head, head

        while fast and fast.next:

            mid = mid.next
            fast = fast.next.next

        # Reverse first half
        
        first = None
        second = head
        
        while second != mid:

            temp = second.next
            second.next = first
            first = second
            second = temp

        while first and mid:

            best = max(first.val + mid.val, best)
            first = first.next
            mid = mid.next

        return best



            



        