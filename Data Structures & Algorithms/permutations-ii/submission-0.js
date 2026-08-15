class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */

    permuteUnique(nums) {
        let results = [[...nums]]
        //for each idx swap upstream until you reach the same val
        const permute = (end_idx) => {
            if (end_idx >= nums.length) return;
            let arrs = []
            for (const res of results) {
                arrs.push([...res])
                let start_i = end_idx
                //console.log("res: ", res)
                while (start_i > 0 && res[start_i] != res[start_i - 1]) {
                    //console.log("start i: ", start_i)
                    //swap
                    const prev_val = res[start_i - 1]
                    res[start_i - 1] = res[start_i]
                    res[start_i] = prev_val
                    arrs.push([...res])
                    //console.log("arrs: ", arrs)
                    start_i -= 1
                    //console.log("updated idx to: ", start_i)
                }
            }
            //results.concat(arrs)
            results = arrs
            console.log("updated results to: ", results)
            permute(end_idx + 1)
        }
        
        permute(1)
        return results
    }
}
