class SeqMap {
    constructor(nums) {
        this.parent = {};
        this.rank = {};
        for (const n of nums) {
            this.parent[n] = n;
            this.rank[n] = 1;
        }
        this.maxRank = nums.length == 0 ? 0 : 1;
    }

    findRoot(node) {
        if (this.parent[node] == node) {
            return node;
        }
        //path compress
        const root = this.findRoot(this.parent[node]);
        this.parent[node] = root;
        return root;
    }
    
    add(n, prev) {
        const n_root = this.findRoot(n);
        const prev_root = this.findRoot(prev);
        if (n_root == prev_root) {
            //had same value already
            return;
        }
        //else merge n_root onto prev_root
        this.parent[n_root] = prev_root;
        this.rank[prev_root] += this.rank[n_root];
        this.maxRank = Math.max(this.maxRank, this.rank[prev_root]);
    }
    
}
class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        
        const numMap = new SeqMap(nums);
        for (const n of nums) {
            //check if O(1)
            if (n-1 in numMap.parent) {
                //merge
                numMap.add(n, n-1);
            }
            if (n+1 in numMap.parent) {
                numMap.add(n+1, n);
            }
        }
        console.log(numMap.parent)
        console.log(numMap.rank)
        return numMap.maxRank
    }
}
