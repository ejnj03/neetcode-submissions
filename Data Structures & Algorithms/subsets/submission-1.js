class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        console.log(nums.length)
        const sets = [[]]
        for (let idx = 0; idx < nums.length; idx++) {
            const to_add = []
            for (const set of sets) {
                //console.log(set)
                //+1 for each node
                to_add.push([...set, nums[idx]])
            }
            sets.push(...to_add)
        }
        return sets
    }
}
