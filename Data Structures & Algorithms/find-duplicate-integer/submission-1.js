class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        // const set = new Set();
        // let ptr = 0;
        // while(ptr < nums.length) {
            
        // }
        let ptr = 0;
        while(ptr < nums.length) {
            const val = nums[ptr]
            //swap if not correct
            //increment if correct

            //ex. ptr = 0 // idx 0: val 1
            if (val == ptr + 1) {
                ptr += 1;
            } else {
                //a different val
                //swap with val's correct location
                const correct_idx = val - 1;
                if (nums[correct_idx] == val) {
                    //detected duplicate
                    return val
                    //else swap
                } else {
                    const updated_val = nums[correct_idx]
                    nums[correct_idx] = val;
                    nums[ptr] = updated_val;
                }
            }
        }
    }
}
