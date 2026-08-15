class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let l_ptr = 0;

        for (let r_ptr = 1; r_ptr < nums.length; r_ptr++) {
            if (nums[l_ptr] != nums[r_ptr]) {
                //update l_ptr
                l_ptr += 1; 
                //set
                nums[l_ptr] = nums[r_ptr];
            }
        }

        //number of elems up to and not including left idx
        return l_ptr + 1
    }

}
