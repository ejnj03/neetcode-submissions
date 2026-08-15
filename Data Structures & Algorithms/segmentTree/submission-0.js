class TreeNode {
    constructor(L, R) {
        this.L = L
        this.R = R
        this.sum = 0
        //ptrs
        this.left = null
        this.right = null
    }
}

class SegmentTree {
    /**
     * @param {number[]} nums
     */
    constructor(nums) {
        const build = (L, R) => {
            //new node
            const node = new TreeNode(L, R);
            //if base case
            if (L==R) {
                //assign the val (only 1) to sum
                node.sum = nums[L];
                //return the node
                return node;
            }
            //if L == R => return the node
            //left end idx
            //left will be larger than right
            //odd: will be (odd - 1)/2 = idx of middle element
            //even: (ex) size 4: (3-0)/2 = 1.5 rounded down will be 1 (idx of last left)
            //same: (ex) size 2: (1-0)/2 = 0.5 rounded down will be 0 (Left end will be L + 0 = L)
            const split_idx = Math.floor((R-L)/2);
            const left_end = L + split_idx
            node.left = build(L, left_end);
            node.right = build(left_end + 1, R);
            node.sum = node.left.sum + node.right.sum;
            return node;
        }
        this.arr_size = nums.length;
        this.root = build(0, this.arr_size - 1);
        //console.log(this.root)
    }

    /**
     * @param {number} index
     * @param {number} val
     */
    update(index, val) {
        const find = (node) => {
            //base case (update val and return)
            if (node.L == index && node.R == index) {
                //update the val
                node.sum = val;
                //return the ?
                return val;
            }
            //const split_idx = Math.floor((R-L)/2);
            //whichever split it belongs to recurse on it
            //if idx < right end of the left node
            if (index <= node.left.R) {
                node.sum = node.sum - node.left.sum + find(node.left);
            } else {
                //idx belongs to right node
                node.sum = node.sum - node.right.sum + find(node.right);
            }
            //return the updated node sum
            return node.sum
        }
        find(this.root)
        //console.log("updated idx ", index, " to value ", val);
        //console.log(this.root)
    }

    /**
     * @param {number} L
     * @param {number} R
     * @returns {number}
     */
    query(L, R) {
        const sum = (node, l, r) => {
            //base case
            if (node.L == l && node.R == r) {
                return node.sum;
            }
            //if in left subarr
            if (r <= node.left.R) {
                return sum(node.left, l, r);
            } else if (l >= node.right.L) {
                //in right subarr
                return sum(node.right, l, r);
            } else {
                //in both arrays
                return sum(node.left, l, node.left.R) + sum(node.right, node.right.L, r)
            }
        }
        return sum(this.root, L, R)
    }
}
