class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        //1. brute force solution

        let total = 0;
        for (let i = 1; i < height.length - 1; i++) {
            let left = i - 1;
            let right = i + 1;

            let left_max = height[left];
            let right_max = height[right];

            while(left > -1) {
                left_max = Math.max(left_max, height[left]);
                left--;
            }

            while (right < height.length) {
                right_max = Math.max(right_max, height[right]);
                right++;
            }

            const wall_height = Math.min(left_max, right_max);
            if (height[i] < wall_height) {
                total += wall_height - height[i];
            }
        }
        return total
    }
}
