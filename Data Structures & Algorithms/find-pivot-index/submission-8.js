class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    pivotIndex(nums) {
        let total = 0;
        const parr = new Array(nums.length).fill(0);

        for (let i = 1; i < nums.length; i++) {
            //parr[i]: all terms up to and not including nums[i]
            parr[i] = nums[i-1] + parr[i-1];
        }

        const sarr = new Array(nums.length).fill(0);
        for (let i = nums.length - 2; i > -1; i--) {
            sarr[i] = sarr[i+1] + nums[i+1];
        }

        console.log(parr, sarr)

        for (let i = 0; i < nums.length; i++) {
            if (sarr[i] == parr[i]) {
                return i
            }
        }
        return -1;
        //console.log(nums)
    }
}
