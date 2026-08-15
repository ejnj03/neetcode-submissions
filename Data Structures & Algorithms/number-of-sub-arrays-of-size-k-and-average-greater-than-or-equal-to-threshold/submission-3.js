class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} threshold
     * @return {number}
     */
    numOfSubarrays(arr, k, threshold) {
        let sum = 0;
        let result_count = 0;

        let l_ptr = 0;
        for (let r_ptr = 0; r_ptr < arr.length; r_ptr++) {
            //length of current subarray
            const count = r_ptr - l_ptr + 1;
            //add current element to sum 
            sum += arr[r_ptr];

            if (count == k)  {
                const avg = sum / k;
                //increment count if meet condition
                if (avg >= threshold) {
                    result_count += 1;
                } 
                //move l_ptr and subtract l_ptr from sum
                sum -= arr[l_ptr]
                l_ptr += 1;
            }
        }
        return result_count;
    }
}
