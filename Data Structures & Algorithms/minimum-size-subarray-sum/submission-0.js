class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        let l_ptr = 0;
        let curr_sum = nums[0];
        let min_length = Number.POSITIVE_INFINITY;
        
        for (let r_ptr = 0; r_ptr < nums.length; r_ptr++) {
            if (r_ptr != l_ptr) {
                curr_sum += nums[r_ptr];
            }
            while (curr_sum >= target) {
                //update based on current subarray length
                min_length = Math.min(min_length, r_ptr - l_ptr + 1);
                
                //don't move l_ptr further if its already at r_ptr loc
                if (l_ptr == r_ptr) {
                    break;
                }
                
                //update left pointer location
                //update current sum
                curr_sum -= nums[l_ptr]
                l_ptr += 1;
            }
        }

        if (min_length == Number.POSITIVE_INFINITY) {
            return 0;
        } else {
            return min_length;
        }
    }
}
