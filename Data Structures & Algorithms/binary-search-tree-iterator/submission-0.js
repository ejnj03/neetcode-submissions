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
        while(this.curr) {
            this.stack.push(this.curr)
            this.curr = this.curr.left
        }

        this.curr = this.stack.pop()
        const curr_val = this.curr.val
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
