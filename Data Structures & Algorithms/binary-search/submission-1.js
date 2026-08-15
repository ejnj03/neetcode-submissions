class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        //range of vals to search [l, r]
        let l = 0;
        let r = nums.length - 1;
        while(l <= r) {
            //ex. length 5 arr => pivot idx is 2 (mid)
            //length 4 arr => pivot idx is 2 (rounded up)
            //(first part is the idx within the subarr! )
            let pivot = Math.floor((r - l + 1)/2) + l;

            //console.log(l, r, " pivot: ", pivot)
            if (target < nums[pivot]) {
                //target is less than the number at the pivot
                //move r
                r = pivot - 1;
            } else if (target > nums[pivot]) {
                l = pivot + 1;
            } else {
                //target = pivot val
                return pivot;
            }
        }
        return -1;
    }
}
