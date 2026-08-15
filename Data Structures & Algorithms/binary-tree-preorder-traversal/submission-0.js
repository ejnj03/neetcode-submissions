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
    preorderTraversal(root) {
        const stack = [root]
        const result = []
        while(stack.length > 0) {
            const node = stack.pop()
            if (!node) continue;
            console.log(node.val)
            result.push(node.val)
            stack.push(node.right)
            stack.push(node.left)
        }
        return result
    }
}
