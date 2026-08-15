/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * function guess(num) {}
 */

class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    guessNumber(n) {
        //define lb and hb, inclusive
        let l = 1;
        let r = n;
        while(l <= r) {
            const ans = Math.floor((r - l + 1)/2) + l;
            console.log(ans)
            const result = guess(ans);
            if (result == 0) {
                return ans;
            } else if (result == 1) {
                //guess is lower
                l = ans + 1;
            } else if (result == -1) {
                //guess is higher
                r = ans - 1;
            }
        }
    }
}
