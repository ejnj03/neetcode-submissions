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
class BSTIterator {
    /**
     * @constructor
     * @param {TreeNode} root
     */
    constructor(root) {
        this.stack = []
        this.curr = root
    }

    /**
     * @return {number}
     */
    next() {
        //runs only if there is a curr node
        let left_node = this.curr
        while(left_node) {
            this.stack.push(left_node)
            left_node = left_node.left
        }

        //pop the leftmost node of the current subtree
        this.curr = this.stack.pop()
        const curr_val = this.curr.val
        //iterate on the right subtree of the leftmost node
        this.curr = this.curr.right     

        return curr_val  
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        return this.curr || this.stack.length > 0 ? true : false
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
