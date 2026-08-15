class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let total = 0;
        //max of elems that come before it
        let prefix_map = {1: height[0]}
        let suffix_map = {}
        suffix_map[height.length - 2] = height[height.length - 1];

        for (let i = 2; i < height.length; i++) {
            //max of (max of elems before i - 1, val at i - 1)
            prefix_map[i] = Math.max(prefix_map[i - 1], height[i-1]); 
        }

        for (let i = height.length - 3; i > 0; i--) {
            //max of (max of elems after i + 1, val at i + 1)
            suffix_map[i] = Math.max(suffix_map[i + 1], height[i+1]); 
        }

        console.log(prefix_map)
        console.log(suffix_map)
        
        for (let i = 1; i < height.length - 1; i++) {
            let wall = Math.min(suffix_map[i], prefix_map[i])
            if (wall > height[i]) {
                total += wall - height[i];
            }
        }
        return total
    }
}
