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
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let curr_node = head;
        //the to be next node
        let prev_node = null;
        while (curr_node != null) {
            //store the next it curr node
            const next_node = curr_node.next;
            //now set the next node to be the prev node
            curr_node.next = prev_node;
            //update the prev node to be the curr node
            prev_node = curr_node;
            //update the curr node to be the next node
            curr_node = next_node;
        }
        return prev_node;
    }
}
