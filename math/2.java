/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode iterator = head;
        
        while (l1 != null || l2 != null) {
            if (l1 != null) {
                iterator.val += l1.val;
                l1 = l1.next;
            }
            
            if (l2 != null) {
                iterator.val += l2.val;
                l2 = l2.next;
            }
            
            if (l1 != null || l2 != null || iterator.val > 9) {
                iterator.next = new ListNode(0);
                if (iterator.val > 9) {
                    iterator.next.val = 1;
                    iterator.val -= 10;
                }
            }
            iterator = iterator.next;
        }
        return head;
    }
}
