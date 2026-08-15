class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let l = 0;
        //let curr_char = s[0]; 
        let max_freq = 0;
        let max_len = 0;
        let count = {};
        
        for (let r = 0; r < s.length; r++) {
            count[s[r]] = count[s[r]] || 0;
            count[s[r]] += 1;
            //var = (if) condition (then) ? _ : (else) _
            //update the max freq
            max_freq = Math.max(max_freq, count[s[r]]);
            //number of other characters excluding the current max character
            //while ((r - l + 1) - count[curr_char] > k) {
            while ((r - l + 1) - max_freq > k) {
                count[s[l]] -= 1;
                //move left ptr 
                l += 1;
                //update max freq if left ptr is greater than right
                //max_freq = Math.max(max_freq, count[s[l]]);
            }
            max_len = Math.max(max_len, r - l + 1);
        }
        return max_len;
    }
}
