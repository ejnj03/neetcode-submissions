class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const ans = new Array(nums.length * 2);
        console.log(ans.length, nums.length);
        for (let i = 0; i < nums.length; i++) {
            //assign val to loc i and loc nums.
            ans[i] = ans[i + nums.length] = nums[i]
        }
        console.log(ans)
        return ans
    }
}
