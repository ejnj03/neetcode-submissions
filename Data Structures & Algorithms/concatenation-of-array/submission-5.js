class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const ans = new Array();
        console.log(ans.length, nums.length);
        for (let i = 0; i < nums.length * 2; i++) {
            //assign val to loc i and loc nums.
            ans.push(nums[i % nums.length])
        }
        console.log(ans)
        return ans
    }
}
