# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, current
        # record current.next in a temp variable
        # as we loop through the ll we change the pointers

        current, prev = head, None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev