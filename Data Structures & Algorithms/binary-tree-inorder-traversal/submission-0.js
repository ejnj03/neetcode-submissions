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
    inorderTraversal(root) {
        const list = [];
        this.traverse(root, list);
        return list;
    }

    traverse(root, list) {
        if (!root) {
            return;
        }
        this.traverse(root.left, list);
        list.push(root.val);
        this.traverse(root.right, list);
    }

    

}
