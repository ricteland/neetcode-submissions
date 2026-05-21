# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Generate dummy node for output list
        dummy = ListNode()
        cursor=dummy
        l1, l2 = list1, list2

        #While both lists non empty
        while l1 and l2:

            #If value of 1 smaller
            if l1.val < l2.val:
              #Add smaller node to next
                cursor.next = l1
                #Update l1, so cut off node we added
                l1 = l1.next

            #Same for l2
            else:
                cursor.next = l2
                l2 = l2.next
            
            #We go to the next node to update
            cursor = cursor.next

        #When one of the lists becomes null, we will have items left in the next one


        if l1:
            #If l1 is still nonempty/not null, we link the output with whats left of l1
            cursor.next = l1

        elif l2:
            #Same for l2
            cursor.next = l2
        
        #Return list without dummy
        return dummy.next
            
            
