/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
        
    mergeSort(pairs) {
        if (pairs.length <= 1) {
            return pairs;
        }
        const half = Math.floor(pairs.length / 2);
        //idx 0 to half - 1
        const left_arr = this.mergeSort(pairs.slice(0, half))
        //idx half to end of arr
        const right_arr = this.mergeSort(pairs.slice(half))

        //current idx in the original array 
        let curr = 0;
        let l_ptr = 0;
        let r_ptr = 0;
        while(curr < pairs.length) {
            //console.log("pairs: ", pairs)
            if (l_ptr < left_arr.length && r_ptr < right_arr.length) {
                if ((right_arr[r_ptr]).key < (left_arr[l_ptr]).key) {
                    pairs[curr] = right_arr[r_ptr]
                    r_ptr += 1
                } else {
                    pairs[curr] = left_arr[l_ptr]
                    l_ptr += 1;
                }
            } else if (l_ptr == left_arr.length) {
                pairs[curr] = right_arr[r_ptr];
                r_ptr += 1;
            } else if (r_ptr == right_arr.length) {
                pairs[curr] = left_arr[l_ptr]
                l_ptr += 1;
            }
            curr += 1;
        }
        return pairs
    }
}
