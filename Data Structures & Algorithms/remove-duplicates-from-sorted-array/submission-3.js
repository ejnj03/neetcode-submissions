class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let end_idx = nums.length - 1;
        let curr_idx = 0;

        //will reach deleted if there is at least one pair
        //will reach end of array if there are no pairs (all elems are unique so none are deleted)
        while (curr_idx != end_idx) {
            if (nums[curr_idx] == nums[curr_idx + 1]) {
                this.remove_elem(nums, curr_idx + 1, end_idx);
                //update end idx since we deleted an elem
                end_idx -= 1;
            } else {
                //if the next element is unique
                curr_idx += 1; 
            }
        }

        //number of elems up to end idx
        return end_idx + 1;
    }

    remove_elem(nums, idx, end_idx) {
        //remove element at a given index
        for (let i = idx; i < end_idx; i++) {
            nums[i] = nums[i+1];
        }
    }
}
