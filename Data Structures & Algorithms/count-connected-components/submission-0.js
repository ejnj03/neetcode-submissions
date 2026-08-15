class UnionSet {
    constructor(n) {
        this.num_nodes = n;
        //n = number of nodes
        this.parent = {}
        this.rank = {}
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
            this.rank[i] = 1;
        }
    }

    findRoot(node) {
        if (this.parent[node] == node) {
            return node;
        }
        const root = this.findRoot(this.parent[node]);
        //path compress
        this.parent[node] = root;
        //console.log("found root of ", node, root)
        return root;
    }

    merge(n1, n2) {
        const rank = this.rank;
        const parent = this.parent;
        console.log("parent: ", parent)
        //every time we merge any trees, we call find which path compresses the trees the nodes belong to
        const r1 = this.findRoot(n1);
        const r2 = this.findRoot(n2);
        if (r1 == r2) {
            //already part of same tree
            return false;
        }
        //console.log("root 1:", r1, "root 2: ", r2)
        if (rank[r1] > rank[r2]) {
            parent[r2] = r1;
        } else if (rank[r2] > rank[r1]) {
            parent[r1] = r2;
        } else {
            //same length
            parent[r1] = r2;
            //console.log("rank: ", rank)
            rank[r2] += 1;
        }
        //console.log("parent: ", parent)
        return true;
    }

    numConnected() {
        const unique = new Set();
        for (let i = 0; i < this.num_nodes; i++) {
            unique.add(this.findRoot(i));
        }
        return unique.size;
    }
}
class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const union_set = new UnionSet(n);
        for (const edge of edges) {
            const [n1, n2] = edge;
            //add edge
            console.log("merging", n1, n2)
            union_set.merge(n1,n2);
        }
        console.log(union_set.parent)
        //after adding all edges count number of connected components
        return union_set.numConnected()
    }
}
