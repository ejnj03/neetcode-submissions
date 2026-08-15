class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashMap = {}

        for (const num of nums) {
            if (!(num in hashMap)) {
                hashMap[num] = 1
            } else {
                return true
            }
        }

        return false
    }
}
