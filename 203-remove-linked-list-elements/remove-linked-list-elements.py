# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # init two pointers and dummy node
        # iterate through the list and compare to val

        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current:
            temp = current.next
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next
                  
