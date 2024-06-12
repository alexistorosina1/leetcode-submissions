# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init 2 pointers, prev and current
        prev = None
        current = head

        # store current.next in a variable temp
        # while theres a node:
        # temp = current.next
        # prev = current
        # current = temp
        # current.next = prev
        #    p     t
        #   [1, 2, 3, 4, 5]
        #       c
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev