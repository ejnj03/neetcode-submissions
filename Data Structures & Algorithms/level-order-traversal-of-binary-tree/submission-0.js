/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        let queue = root ? [root] : [];
        let list = []
        let next_queue = [];
        let lists = [];
        while(queue.length > 0) {
            const node = queue.shift();
            list.push(node.val)

            if (node.left) next_queue.push(node.left);
            if (node.right) next_queue.push(node.right);
            //console.log(next_queue)
            //if this was the last node in that layer;
            if (queue.length == 0) {
                //add list to lists
                lists.push(list);
                //reassign list to an empty list
                list = [];
                //reassign queue to the current next_queue
                queue = next_queue;
                //reassign next_queue to an empty queue
                next_queue = [];
            }
        }
        return lists;
    }
}
