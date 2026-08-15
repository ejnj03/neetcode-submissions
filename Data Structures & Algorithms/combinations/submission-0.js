class Solution {
    /**
     * @param {number} n
     * @param {number} k
     * @return {number[][]}
     */
    combine(n, k) {
        const results = []
        const combination = (i, curr_set) => {
            //console.log(i, curr_set)
            //add and return if length is =
            if (curr_set.length == k) {
                results.push([...curr_set])
                return
            } 

            //just return if i > 
            if (i > n) return;
            
            //add the val at i to the current combination and recurse
            curr_set.push(i)
            combination(i + 1, curr_set)
            //pop and recurse
            curr_set.pop()
            combination(i + 1, curr_set)
        }
        
        //start idx, current set
        combination(1, [])
        return results
    }
}
