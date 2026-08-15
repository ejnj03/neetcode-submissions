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
     * @param {number} targetSum
     * @return {boolean}
     */
    hasPathSum(root, targetSum) {
        const hasSum = (node, curr_sum) => {
            if (!node) {
                return false
            }
            curr_sum += node.val
            if (!node.left && !node.right && curr_sum == targetSum) {
                return true
            } 
            const left_sum = hasSum(node.left, curr_sum)
            if (left_sum) return left_sum
            return hasSum(node.right, curr_sum)
        }

        return hasSum(root, 0)
    }
}
