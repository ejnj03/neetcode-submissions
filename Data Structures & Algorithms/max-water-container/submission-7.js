class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        let l = 0;
        let r = heights.length - 1;
        while (l < r) {
            const area = Math.min(heights[r], heights[l]) * (r - l);
            maxArea = Math.max(maxArea, area);
            if (heights[r] < heights[l]) {
                r -= 1;
            } else {
                l += 1;
            }
        }
        return maxArea;
    }
}
