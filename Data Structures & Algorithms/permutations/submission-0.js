class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        let results = []
        const permutate = (i) => {
            if (i == nums.length - 1) {
                //last idx => before and after is the same
                results.push([nums[i]])
                return
            }

            //permutate first
            permutate(i + 1)
            //console.log(i+1, results)
            const updated = []
            for (const result of results) {
                //iterate over each possible spot
                for (let insert = 0; insert <= result.length; insert++) {
                    const cpy = [...result]
                    //delete 0 items
                    cpy.splice(insert, 0, nums[i])
                    updated.push(cpy)
                }
            }
            //update results
            results = updated
            return
        }
        permutate(0)
        return results
    }
}
