class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0;
        let curr_set = new Set();
        //set default to min 
        let max_len = 0;
        for (let r = 0; r < s.length; r++) {
            console.log("curr set: ", curr_set)
            //check if r already in set
            while (curr_set.has(s[r])) {
                curr_set.delete(s[l]);
                //move l 
                l += 1;
                //set stays the same since this char is already in the set
            }
            
            //if not already in the set add to the set
            curr_set.add(s[r])

            max_len = Math.max(max_len, curr_set.size);
        }
        return max_len;
    }
}
