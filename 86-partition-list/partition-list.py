# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # creating 2 lists then merging them at the end
        # loop through og list and compare values
        # if current val < x
        # push current val to left
        # else push to right

        left_head, right_head = ListNode(), ListNode()
        left, right = left_head, right_head

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        
        right.next = None
        left.next = right_head.next
        return left_head.next