class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums) {
        const colors = new Array(3).fill(0)
        for (const num of nums) {
            colors[num] += 1
        }
        console.log(colors)
        let curr_pos = 0
        for (let color = 0; color < colors.length; color++) {
            for (let i = 0; i < colors[color]; i++) {
                nums[curr_pos] = color
                curr_pos += 1
            }
        }
    }
}
