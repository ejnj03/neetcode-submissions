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
    middleNode(head) {
        let sptr = head;
        let fptr = head;
        while (fptr) {
            if (fptr.next) {
                //for odd (will be no next at last ptr)
                fptr = fptr.next.next;
            } else {
                break;
            }
            sptr = sptr.next;
        }
        return sptr;
    }
}
