# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current and current.next:
            first = current
            second = current.next

            # swap 
            prev.next = second
            first.next = second.next
            second.next = first

            # move pointers up
            prev = first
            current = first.next
        
        return dummy.next