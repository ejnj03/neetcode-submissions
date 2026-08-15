class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let l = 0;
        let r = numbers.length - 1;
        let sum = 0;
        while (l < r) {
            sum = numbers[l] + numbers[r];
            if (sum > target) {
                //if sum is greater than target move r ptr (decrease sum)
                r -= 1
            } else if (sum < target) {
                //increase sum (move l ptr)
                l += 1
            } else {
                //if equal to target
                //one indexed
                return [l + 1, r + 1]
            }
        }
    }
}
