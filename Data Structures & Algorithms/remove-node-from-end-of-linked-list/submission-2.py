# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        count = head
        while count:
            N += 1
            count = count.next
        curr = head
        index  = N-n
        if index == 0:
            return head.next
        for i in range(0,index - 1):
            curr = curr.next
        print(curr.val)
        
        curr.next = curr.next.next
        return head

        