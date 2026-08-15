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
     * @param {number} key
     * @return {TreeNode}
     */
    deleteNode(root, key) {
        if (!root) return null;
        if (key < root.val) {
            //search left subtree
            root.left = this.deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = this.deleteNode(root.right, key);
        } else {
            if (!root.left && !root.right) return null;
            if (!root.left) return root.right;
            if (!root.right) return root.left;
            //if we have both left and right 
            const left_tree = root.left;
            let parent = root.right;
            let min_val = parent;
            while(true) {
                if (!min_val.left) {
                    break;
                }
                parent = min_val;
                min_val = min_val.left;
            }
            if (min_val !== parent) {
                parent.left = min_val.right;
            } else {
                //right val is the 'smallest val in right subtree'
                root.right = parent.right;
            }
            //replace root with min val
            min_val.right = root.right;
            min_val.left = root.left;
            root = min_val
        }
        return root;
    }
}
