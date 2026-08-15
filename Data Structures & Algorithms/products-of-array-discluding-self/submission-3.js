class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        const result = new Array(nums.length).fill(1);

        for (let i = 1; i < nums.length; i++) {
            //parr[i]: all terms up to and not including nums[i]
            result[i] = result[i-1] * nums[i-1];
        }
        
        //suffix of the idx that came before i 
        let prev = 1
        for (let i = nums.length - 2; i > -1; i--) {
            //last idx doesn't have a suffix so we can skip it
            prev = prev * nums[i+1]
            result[i] *= prev
        }

        return result;
        //console.log(nums)
    }
}
