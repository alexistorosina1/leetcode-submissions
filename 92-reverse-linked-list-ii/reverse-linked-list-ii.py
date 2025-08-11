# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
        
        current = pre.next
        
        for _ in range(right - left):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = pre.next
            pre.next = node_to_move
        return dummy.next
