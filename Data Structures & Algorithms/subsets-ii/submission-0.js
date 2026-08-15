class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        const results = []
        //first sort array
        nums.sort()
        const getSubsets = (start_i, set)  => {
            //invalid start idx
            if (start_i >= nums.length) {
                //push copy of the current set
                results.push([...set])
                return 
            }
            //set with the val at start_i
            set.push(nums[start_i])
            getSubsets(start_i + 1, set)
            //pop the value we just added 
            let prev_val = set.pop()
            //pop then move idx to the last that includes the same val
            while(start_i < nums.length && nums[start_i] == prev_val) {
                start_i += 1
            }
            //recurse on that idx + 1
            getSubsets(start_i, set) 
        }
        getSubsets(0, [])
        return results
    }
}
