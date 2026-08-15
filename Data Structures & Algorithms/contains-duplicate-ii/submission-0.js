class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        const window = new Set();
        //l_ptr: target element 
        let l_ptr = 0;
        for (let r_ptr = 0; r_ptr < nums.length; r_ptr++) {
            
            //if exceeded the window limit
            if (r_ptr > l_ptr + k) {
                //remove l_ptr element from set 
                window.delete(nums[l_ptr]);
                //advance l_ptr 
                l_ptr += 1;
            } 
            //if within window and already in set:
            if (window.has(nums[r_ptr])) {
                return true; //early stop
            } else {
                //if within window but not duplicate
                window.add(nums[r_ptr]);
            }
        }
        //if reach here then ret false
        return false;
        
    }
}
