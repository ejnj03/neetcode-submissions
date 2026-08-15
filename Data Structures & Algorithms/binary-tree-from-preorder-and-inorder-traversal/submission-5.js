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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        if (preorder.length == 0) {
            return null;
        }

        //find the root of the current subtree
        const root_val = preorder[0];
        //create the node
        const root = new TreeNode(root_val, null, null);
        //find its index in the in order list
        const iroot_idx = inorder.findIndex((e) => e == root_val);
        //console.log("index of root node in the in order list (middle of left and right): ", iroot_idx)
        //if iroot idx == 0: then there is no left subtree
        
        //left array of in order
        const ileft_arr = inorder.slice(0, iroot_idx);
        const iright_arr = inorder.slice(iroot_idx + 1);

        //console.log("current root: ", root_val)
        //console.log("current li ri: ", ileft_arr, iright_arr);
        //default if no left array

        const pleft_arr = preorder.slice(1, ileft_arr.length + 1);
        const pright_arr = preorder.slice(ileft_arr.length + 1);

        //console.log("current lp rp: ", pleft_arr, pright_arr);
        
        root.left = this.buildTree(pleft_arr, ileft_arr);
        root.right = this.buildTree(pright_arr, iright_arr);

        //console.log(root)
        return root;
    }
}
