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
        console.log("start")
        if(!head || !head.next) {
            return head;
        }
        console.log(head.val)
        const next_node = head.next;
        //for the last node
        head.next = null;
        const last_node = this.reverseList(next_node);
        next_node.next = head;
        return last_node;
    }
}
