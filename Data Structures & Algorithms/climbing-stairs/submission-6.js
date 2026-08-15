class Solution {
    constructor() {
        this.map = {};
        //map of n: count
    }
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        //consider n to be the number of remaining steps
        if (n == 0 || n == 1) {
            return 1;
        } 
        if (!(n in this.map)) {
            //recurse
            let n_count = 0;
            //1. chose 1 step at current level
            n_count += this.climbStairs(n-1)
            //2. chose 2 steps at current level
            n_count += this.climbStairs(n-2)
            //add it into the dict
            this.map[n] = n_count;
        }
        return this.map[n];
    }
}
