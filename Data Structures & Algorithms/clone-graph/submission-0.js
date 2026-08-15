/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        //const adj = []
        const visited = {}

        const dfs = (node) => {
            if (!node) return null
            //add_node(node.val, node.neighbors)
            const copy = new Node(node.val, [])
            //add the copy to the visited dict
            visited[node.val] = copy
            if (!node.neighbors) return
            //add its nbs
            for (const nb of node.neighbors) {
                if (!(nb.val in visited)) {
                    //create and push copy
                    copy.neighbors.push(dfs(nb))
                } else {
                    //copy of node already exists
                    copy.neighbors.push(visited[nb.val])
                }
            }
            return copy
        }
        return dfs(node)
    }
}
