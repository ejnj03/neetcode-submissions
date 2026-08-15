class Solution {
    /**
     * @param {number[][]} edges
     * @return {number[]}
     */
    findRedundantConnection(edges) {
        const num_nodes = edges.length;
        const parent = {}
        const rank = {};
        for (let i = 1; i < num_nodes + 1; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        
        const path_compress = (node_idx) => {
            if (parent[node_idx] == node_idx) {
                return node_idx; //is root
            }
            const root = path_compress(parent[node_idx]);
            parent[node_idx] = root;
            return root;
        }

        const root_merge = (root1, root2) => {
            const root1_rank = rank[root1]
            const root2_rank = rank[root2]
            if (root1_rank > root2_rank) {
                parent[root2] = root1;
            } else if (root2_rank > root1_rank) {
                parent[root1] = root2;
            } else {
                //same rank
                //arbitrary choose
                parent[root1] = root2;
                rank[root2] += 1;
            }
        }
        for (let i = 0; i < edges.length; i++) {
            const [ai, bi] = edges[i];
            //if ai doesnt already have a parent that isnt itself
            //get its root
            const root_ai = path_compress(ai);
            const root_bi = path_compress(bi);
            //check that the roots are different
            if (root_ai == root_bi) {
                //if they are same this is the edge that can be removed
                return edges[i];
            }
            //if bi doesnt have a parent that isnt itself 
            //get its root
            //merge the roots if they arent the same  
            root_merge(root_ai, root_bi);
            console.log(parent)
        }
        //if the nodes root is already not itself
    }
}
