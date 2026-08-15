class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        //create hashMap
        const hashMap = {}

        //target: idx with that target
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] in hashMap) {
                return [hashMap[nums[i]], i]
            } else {
                hashMap[target - nums[i]] = i
            }
        }
    }
}
