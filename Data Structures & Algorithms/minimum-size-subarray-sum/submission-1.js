class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        let l_ptr = 0;
        //let curr_sum = nums[0];
        let curr_sum = 0;
        //let min_length = Number.POSITIVE_INFINITY;
        let min_length = Infinity;
        for (let r_ptr = 0; r_ptr < nums.length; r_ptr++) {
            // if (r_ptr != l_ptr) {
            //     curr_sum += nums[r_ptr];
            // }
            curr_sum += nums[r_ptr];
            while (curr_sum >= target) {
                //update based on current subarray length
                min_length = Math.min(min_length, r_ptr - l_ptr + 1);
                
                // //don't move l_ptr further if its already at r_ptr loc
                // if (l_ptr == r_ptr) {
                //     break;
                // }

                //ㄴ don't need bc when reach idx where rptr = lptr and val is = target:
                //we would have already accounted for the min length 1 array so we can now subract 
                //the target from the sum (so curr_sum = 0) and move onto the next possible l_ptr val
                //r_ptr would be updated in the next loop though its at a psn before l_ptr inside the current loop iteratioon
                
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
