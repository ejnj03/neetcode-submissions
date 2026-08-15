class TreeNode {
    constructor(key, left_key, right_key) {
        this.key = key;
        this.left = left_key;
        this.right = right_key;
    }
}

class TreeMap {
    constructor() {
        this.pairs = {};
        this.root = null;
    }

    /**
     * @param {number} key
     * @param {number} val
     * @returns {void}
     */
    insert(key, val) {
        //override the original val is exists, else insert pair to map
        this.pairs[key] = val;
        const to_insert = new TreeNode(key, null, null);
        const recurse = (root) => {
            if (!root) {
                return to_insert;
            }
            //if belongs to left_subtree
            if (key < root.key) {
                //if left node exists
                if (root.left) {
                    //recurse
                    root.left = recurse(root.left)
                } else {
                    //no left node
                    root.left = to_insert;
                }
            } else if (key > root.key) {
                if (root.right) {
                    root.right = recurse(root.right);
                } else {
                    root.right = to_insert;
                }
            }
            //do nothing to the tree if val already exists, just return the root
            return root;
        }
        //reassign in case root doesnt exist yet (is null)
        this.root = recurse(this.root)
        //console.log(this.root, "inserted: ", key);
    }

    /**
     * @param {number} key
     * @returns {number}
     */
    get(key) {
        return key in this.pairs ? this.pairs[key] : -1;
    }

    /**
     * @returns {number}
     */
    getMin() {
        //utilize tree structure to get result in O(logn time)
        const findMin = (node) => {
            if (!node) {
                return -1;
            }
            //return leftmost tree node
            if (!node.left) {
                //return the VALUE mapped to the smallest KEY
                return this.pairs[node.key]
            }
            //recurse on left child
            return findMin(node.left);
        }
        return findMin(this.root);
    }

    /**
     * @returns {number}
     */
    getMax() {
        console.log(this.root)
        console.log(this.pairs)
        const findMax = (node) => {
            if (!node) {
                return -1;
            }
            if (!node.right) {
                console.log(node.key)
                return this.pairs[node.key];
            }
            return findMax(node.right);
        }
        return findMax(this.root)
    }

    /**
     * @param {number} key
     * @returns {void}
     */
    remove(key) {
        //remove from map
        delete this.pairs[key]
        console.log(this.pairs)

        const findMin = (node) => {
            if (!node) {
                return -1;
            }
            //return leftmost tree node
            if (!node.left) {
                //return the VALUE mapped to the smallest KEY
                return node.key
            }
            //recurse on left child
            return findMin(node.left);
        }

        const findKey = (curr_node, key) => {
            if (!curr_node) {
                return null;
            }
            const curr_key = curr_node.key;
            if (key < curr_key) {
               curr_node.left = findKey(curr_node.left, key);
            } else if (key > curr_key) {
                curr_node.right = findKey(curr_node.right, key);
            } else {
                console.log("found key: ", curr_node.key)
                //key is current key
                if (!curr_node.left && !curr_node.right) {
                    return null;
                } else if (!curr_node.right) {
                    return curr_node.left;
                } else if (!curr_node.left) {
                    return curr_node.right;
                } else {
                    //has both children
                    //the node to update to
                    //replace its value   
                    curr_node.key = findMin(curr_node.right);
                    //* important! use this function to remove the min node from the right subtree
                    curr_node.right = findKey(curr_node.right, curr_node.key)
                }
            }
            return curr_node;
        }
        this.root = findKey(this.root, key);
        console.log(this.root)
    }

    /**
     * @returns {number[]}
     */
    getInorderKeys() {
        let list = [];
        const recordKeys = (node) => {
            if (!node) {
                return;
            }
            recordKeys(node.left);
            list.push(node.key);
            recordKeys(node.right);
        }
        recordKeys(this.root);
        //console.log(list)
        return list;
    }
}
