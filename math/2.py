# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        iterator = head
        
        while l1 != None or l2 != None:
            if l1 != None:
                iterator.val += l1.val
                l1 = l1.next
            if l2 != None:
                iterator.val += l2.val
                l2 = l2.next
            
            if l1 != None or l2 != None or iterator.val > 9:
                iterator.next = ListNode(0)
                if iterator.val > 9:
                    iterator.next.val = 1
                    iterator.val -= 10
            iterator = iterator.next
        
        return head
