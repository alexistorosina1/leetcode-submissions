# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = head
        right = head.next if head else None


        while left and right:
            if left.val != right.val:
                left = right
                right = right.next
            else:
                left.next = right.next
                right = left.next
        return dummy.next
        