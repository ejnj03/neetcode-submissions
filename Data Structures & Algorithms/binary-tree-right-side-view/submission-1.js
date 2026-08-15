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
     * @return {number[]}
     */
    rightSideView(root) {
        let queue = root ? [root] : [];
        let vals = [];
        //console.log(queue)
        while(queue.length > 0) {
            //console.log(queue)
            const level_size = queue.length;
            let level_vals = []
            for (let i = 0; i < level_size; i++) {
                const node = queue.shift();
                //console.log(node)
                level_vals.push(node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            //console.log(queue)
            //add the rightmost val
            vals.push(level_vals[level_vals.length - 1]);
        }
        return vals;
    }
}
