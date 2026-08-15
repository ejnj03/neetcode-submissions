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
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        let curr = null;
        console.log(lists.length)
        if (lists.length > 0) {
            curr = lists[0];
        } else {
            return curr; 
        }
        for (let merge = 1; merge < lists.length; merge++) {
            //merge the merge list with the current list
            //set root node
            let root = null;
            let curr_node = null;
            let cnode = curr;
            let mnode = lists[merge];
            while(true) {
                //console.log("merging ", merge, " current list: ", root)
                //console.log("cnode: ", cnode, " mnode", mnode);
                //node to add
                let add_node = null;
                if (!cnode && !mnode) {
                    break;
                }
                //& cnode for when !cnode but mnode exists so its gna check the second case => throws error
                //checks 2nd condition only when mnode exists
                if (!mnode || cnode && cnode.val <= mnode.val) {
                    //console.log("cnode is add node")
                    //cnode should be added to the chain
                    add_node = cnode;
                    //advance cnode ptr
                    cnode = cnode.next;
                } else if (!cnode && mnode || mnode && mnode.val < cnode.val) {
                    //if do separate if statement we update cnode and compare that with the mnode
                    //(deal with = case)
                    add_node = mnode;
                    mnode = mnode.next
                }
                //console.log("add node: ", add_node)
                if (!root) {
                    root = add_node;
                } else {
                    curr_node.next = add_node;
                }
                //update the current node 
                curr_node = add_node
            }
            //update curr to the root
            curr = root;
        }
        return curr;
    }
}
