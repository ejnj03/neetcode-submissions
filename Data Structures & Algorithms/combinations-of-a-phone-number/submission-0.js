class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
        //padding to match idx to digit
        const mapping = [
            "", "", "abc", "def", 
            "ghi", "jkl", "mno", 
            "pqrs", "tuv", "wxyz"
        ]
        const results = []
        const combination = (i, curr) => {
            //console.log(i, curr_set)
            //add and return if length is =
            if (curr.length == digits.length) {
                results.push(curr)
                return
            } 

            //just return if i > 
            if (i > digits.length) return;
            //get the digit at the current idx
            const num = Number(digits[i])
            //add the val at i to the current combination and recurse
            for (const char of mapping[num]) {
                console.log(curr + char)
                combination(i + 1, curr + char)
            }
        }
        
        //start idx, current set
        combination(0, "")
        console.log(results)
        return results.length == 1 ? [] : results
    }
}
