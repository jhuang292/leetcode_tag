# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            runner = cur.next
            while runner and cur.val == runner.val:
                runner = runner.next
            cur.next = runner 
            cur = runner
        return head
