class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {

        //brute force 

        let count = 0;
        for (let s = 0; s < nums.length; s++) {
            //all sequences starting at s
            let curr_sum = 0;
            for (let e = s; e < nums.length; e++) {
                //sequence starting at s and ending at e
                curr_sum += nums[e];
                if (curr_sum == k) {
                    count += 1;
                }
            }
        }
        return count;
    }
}
