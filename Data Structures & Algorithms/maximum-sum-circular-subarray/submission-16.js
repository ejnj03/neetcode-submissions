class Solution {
    maxSubarraySumCircular(nums) {
        let min_R = 0;
        let min_L = 0;
        let l_ptr = 0;

        let curr_sum = 0;
        let global_min = nums[0];

        let curr_msum = 0;
        let curr_max = nums[0];

        for (let r_ptr = 0; r_ptr < nums.length; r_ptr++) {
            //update for max non-wrapped sum
            if (curr_msum < 0) {
                curr_msum = 0
            }
            curr_msum += nums[r_ptr];
            curr_max = Math.max(curr_msum, curr_max);

            //prev values make a positive contribution
            if (curr_sum > 0) {
                //therefore min sum that ends at this value starts at the value
                l_ptr = r_ptr;
                //reinitialize curr sum
                curr_sum = 0;
            }

            //add current value to the current sum
            curr_sum += nums[r_ptr];

            console.log("curr sum:", curr_sum)
            console.log("min sum:", global_min)
            console.log("lptr: ", l_ptr, " r_ptr: ", r_ptr);
            //if curr min < global min, then set max R and max L to the current L and R ptrs
            if (curr_sum < global_min) {
                min_R = r_ptr;
                min_L = l_ptr;
                //update the global min to the current sum
                global_min = curr_sum;
            }
        }
        console.log(curr_max);
        console.log("range to exlude: ", min_L, min_R);
        //return the sum excluding the vals [max_L, max_R]
        let result = 0;

        //if all -, then min sum will be the entire array so we should just use the regular max
        if (min_L == 0 && min_R == nums.length - 1) {
            return curr_max; 
        }
        for (let i = 0; i < nums.length; i++) {
            // val is on left of lptr or on right of rptr
            if (i < min_L || i > min_R) {
                result += nums[i];
            }
        }
        
        return Math.max(result, curr_max);
    }
}
