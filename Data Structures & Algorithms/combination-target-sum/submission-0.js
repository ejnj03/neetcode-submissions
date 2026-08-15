class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        //sort in ascending order
        nums.sort()
        const result = []

        const cSum = (curr_idx, curr_target, curr_set) => {
            //console.log(curr_idx, curr_target, curr_set)
            const min_num = nums[curr_idx]
            if (curr_target == 0) {
                result.push(curr_set)
                return
            } else if (curr_target < min_num) {
                //invalid set
                return
            }
            const num_choices = Math.floor(curr_target / min_num)
            for (let i = 0; i <= num_choices; i++) {
                //i: number of min_nums we will choose for current combination
                cSum(curr_idx + 1, curr_target - i * min_num, new Array(i).fill(min_num).concat(curr_set))
            }
        }
        cSum(0, target, [])
        return result
    }
}
