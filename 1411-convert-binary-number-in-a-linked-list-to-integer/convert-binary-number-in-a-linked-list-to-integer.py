# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans, current = 0, head

        while current:
            ans = ans * 2 + current.val
            current = current.next
        return ans

        # 0 * 2 + 1 = 1
        # 1 * 2 + 0 = 2
        # 2 * 2 + 1 = 5
        