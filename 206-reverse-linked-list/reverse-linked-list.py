# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize pointers
        prev = None
        current = head

        # while loop 
        while current:
        # record the current.next into a variable
            temp = current.next
        # point the current.next to the prev pointer
            current.next = prev
        # move prev to current
            prev = current
        # move current to temp
            current = temp
        
        return prev