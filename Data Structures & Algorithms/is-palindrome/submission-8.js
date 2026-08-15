class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0
        let r = s.length - 1
        while (l < r) {
            while(l < r && !s[l].match(/[a-zA-Z0-9]/)) {
                l++;
            }
            while(r > l && !s[r].match(/[a-zA-Z0-9]/)) {
                r--;
            }
            console.log()
            if (s[l].toLowerCase() != s[r].toLowerCase()) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
