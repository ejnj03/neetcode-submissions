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
     * @return {boolean}
     */
    hasCycle(head) {
        let fptr = head;
        let sptr = head;
        let init = true;
        while(fptr && fptr.next) {
            fptr = fptr.next.next
            sptr = sptr.next

            if (fptr == sptr) {
                return true;
            }
        }
        //fptr reached null (end of list)
        return false;
    }
}
