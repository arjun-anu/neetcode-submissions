# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # FIND THE MIDDLE
        slow = head
        # having fast start from head.next helps us to 
        # choose slow to become the first middle instead of the 
        # secone one in cases like even lengthed lists
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # REVERSE THE SECOND HALF
        second = slow.next
        # whenever you split a list into two halves, 
        # always terminate the first half explicitly 
        # with slow.next = None, otherwise the two 
        # halves are still physically connected and 
        # you'll get corrupted results.
        prev =  slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # THEN JOIN THEM TOGETHER ONE BY ONE         
        first, second = head, prev
        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2

        