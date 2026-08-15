/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        //add a copy of the current pairs array not a reference
        const history = [];
        //current idx to sort
        if (pairs.length == 0) {
            return history;
        }
        history.push([...pairs])
        for (let i = 1; i < pairs.length; i++) {
            let curr = i
            let curr_swap = i - 1
            //console.log(pairs[curr_swap].key, pairs[curr].key)
            while (curr > 0 && pairs[curr_swap].key > pairs[curr].key) {
                //swap 
                const curr_item = pairs[curr];
                //console.log(pairs[curr].key)
                pairs[curr] = pairs[curr_swap];
                pairs[curr_swap] = curr_item;
                curr = curr_swap;
                curr_swap -= 1;
            }
            //create copy and append to history
            history.push([...pairs])
        }
        return history
        
    }
}
