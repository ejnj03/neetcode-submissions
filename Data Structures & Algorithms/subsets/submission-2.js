class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        console.log(nums.length)
        const sets = []
        const recurse = (idx, curr_set) => {
            console.log("curr idx: ", idx, " curr set: ", curr_set)
            if (idx >= nums.length) {
                //push a copy
                sets.push([...curr_set])
                return
            }
            //recurse on with the entry
            curr_set.push(nums[idx])
            recurse(idx + 1, curr_set)
            //pop so that when we return from this level it returns the set without the element
            curr_set.pop()
            recurse(idx + 1, curr_set)
        }
        recurse(0, [])
        return sets
    }
}
