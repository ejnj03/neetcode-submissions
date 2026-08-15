/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        //maintain the current elem of each list
        //maintain the head of the new list
        let curr1 = list1;
        let curr2 = list2;
        let head = null;
        let tail = null;
        
        while(true) {
            let next_node = null;
            if (curr1 == null && curr2 == null) {
                break
            } else if (curr1 == null) {
                next_node = curr2;
            } else if (curr2 == null) {
                next_node = curr1;
            } else {
                next_node = curr1.val < curr2.val ? curr1 : curr2;
            }
        
            if (!head) {
                head = next_node;
                tail = next_node;
            } else {
                //set next node of tail to next node
                tail.next = next_node; 
                //update tail to the next node
                tail = tail.next;
            }

            if (next_node == curr1) {
                curr1 = curr1.next
            } else {
                curr2 = curr2.next
            }

        }
        return head;
    }
}
