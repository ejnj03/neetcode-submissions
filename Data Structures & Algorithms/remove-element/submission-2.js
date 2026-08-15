class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let l_ptr = 0;
        for (let r_ptr = 0; r_ptr < nums.length; r_ptr++) {
            if (nums[r_ptr] != val) {
                if (l_ptr != r_ptr) {
                    nums[l_ptr] = nums[r_ptr];
                }
                l_ptr += 1;
            }
        }
        //number of non val elems
        return l_ptr
    }
}
