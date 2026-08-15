class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let max_sum = nums[0];
        //curr sum is the max sum of subarrays ending at nums[i-1] 
        let curr_sum = 0;
        for (const n of nums) {
            //max sum of subarrays ending at nums[i]:
            //max(nums[i] + max subarray sum of subarrays ending at nums[i-1], nums[i])
            //= max(curr_sum, 0) + nums[i]
            const n_max = Math.max(curr_sum, 0) + n;

            //max sum is the max of the current maximum sum and n_max
            max_sum = Math.max(n_max, max_sum);
            
            //set curr_sum = n_max for nums[i+1]
            curr_sum = n_max;
        }
        return max_sum
    }
}
