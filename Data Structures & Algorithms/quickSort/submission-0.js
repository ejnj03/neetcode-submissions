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
    quickSort(pairs) {
        this.sort(pairs, 0, pairs.length - 1);
        return pairs
    }

    sort(pairs, l, r) {
        //left and right indices (inclusive)
        //r - l + 1 = length of subarray
        const ssize = r - l + 1;
        if (ssize <= 1) {
            return;
        }
        //i.e., idx 0 - 3: size 4
        const pivot = pairs[r]; 
        //index to insert (start at leftmost idx)
        let insert = l;
        //start at left idx, iterate until r-1th idx
        for (let i = l; i < r; i++) {
            if (pairs[i].key < pivot.key) {
                //swap with insert index
                let curr_insert = pairs[insert];
                //place pairs[i] at the insert location
                pairs[insert] = pairs[i];
                //place insert val in the pairs[i] location
                pairs[i] = curr_insert;
                //increment insert
                insert+=1; 
            }
        }
        //swap the insert idx with the pivot val
        pairs[r] = pairs[insert];
        pairs[insert] = pivot;
        //console.log(pairs.slice(l, insert - 1))
        //console.log(pairs.slice(insert + 1, r))
        //iterate (l up to before insert, from (and not including) after insert up to r)
        this.sort(pairs, l, insert - 1);
        // (pivot, r]
        this.sort(pairs, insert + 1, r);
    }
}
