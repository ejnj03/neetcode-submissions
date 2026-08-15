class UnionFind {
    /**
     * @param {number} n
     */
    constructor(n) {
        this.num_nodes = n;
        //dict containing parents of each idx i node 
        this.parent = {}
        //height of longest subchain with i as root
        this.rank = {}
        //node idxs are 0 idxed
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
            this.rank[i] = 1;
        }

    }

    /**
     * @param {number} x
     * @return {number}
     */
    find(x) {
        if (this.parent[x] == x) {
            //this is the root node
            return x;
        }
        //also path compress
        //merge everything onto the root
        let curr_node = x;
        //its root is its parents root
        const root = this.find(this.parent[x])
        //assign the current node to the root
        this.parent[x] = root;
        //return the root for its children 
        return root;
    }

    /**
     * @param {number} x
     * @param {number} y
     * @return {boolean}
     */
    isSameComponent(x, y) {
        //if they share the same root they are part of the same component
        if (this.find(x) == this.find(y)) {
            return true;
        }
        return false;
    }

    /**
     * @param {number} x
     * @param {number} y
     * @return {boolean}
     */
    union(x, y) {
        const root_x = this.find(x)
        const root_y = this.find(y)
        if (root_x == root_y) {
            return false;
        }
        const rank_x = this.rank[root_x];
        const rank_y = this.rank[root_y];
        //merge by rank
        if (rank_x > rank_y) {
            //merge onto root_x
            //no need to change bc current rank alr >= rank of root_y + 1
            this.parent[root_y] = root_x;
        } else if (rank_y > rank_x) {
            this.parent[root_x] = root_y;
        } else {
            //rank x = rank y
            //arbitrarily break tie
            this.parent[root_x] = root_y;
            //update rank of root_y since rank of root_y is now + 1
            this.rank[root_y] += 1;
        }
        return true;
    }

    /**
     * @return {number}
     */
    getNumComponents() {
        const root_set = new Set();
        for (let i = 0; i < this.num_nodes; i++) {
            //add the nodes root to the root set
            root_set.add(this.find(i));
        }
        //return size of root set
        //console.log(root_set)
        return root_set.size
    }
}
