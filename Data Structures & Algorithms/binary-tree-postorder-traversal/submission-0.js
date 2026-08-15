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
    postorderTraversal(root) {
        const stack = [root]
        const visit = [false]
        const result = []

        while (stack.length > 0) {
            //console.log(stack)
            const curr = stack.pop()
            const visited = visit.pop()
            if (!curr) continue;
            if (visited) {
                //we've already visited its children so now we can pop it 
                result.push(curr.val) 
            } else {
                //add it back
                //add par -> right -> left (popped in reverse order)
                stack.push(curr)
                //since we will add its children to the stack in the following line
                //and bc of the order we know when we pop this all of is subtree will already have been visited
                visit.push(true)

                stack.push(curr.right), visit.push(false);
                stack.push(curr.left), visit.push(false);
            }
        }
        return result
    }
}
