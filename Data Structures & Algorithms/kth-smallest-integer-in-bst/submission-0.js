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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let curr_count = 0;
        const min_val = (node) => {
            
            if (!node) return -1;
            const left_val = min_val(node.left);
            if (left_val != -1) return left_val;
            //first time here will be when reach left bottom
            curr_count += 1;
            console.log(node, curr_count)
            if (curr_count == k) {
                return node.val;
            }
            return min_val(node.right);
        }  
        return min_val(root);
    }
}
