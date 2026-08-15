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
     * @param {number} val
     * @return {TreeNode}
     */
    insertIntoBST(root, val) {
        if(!root) {
            return new TreeNode(val, null, null);
        }
        //if val < root.val and no left child yet: insert here
        if (val < root.val) {
            if (!root.left) {
                //if no left val yet
                root.left = new TreeNode(val, null, null);
            } else {
                //recurse on the left subtree
                this.insertIntoBST(root.left, val);
            }
        } else if (val > root.val) {
            if (!root.right) {
                root.right = new TreeNode(val, null, null);
            } else {
                this.insertIntoBST(root.right, val);
            }
        }
        //assuming that val != root
        return root;
    }
}
