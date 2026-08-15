class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    maxTurbulenceSize(arr) {
        let curr_rule1_max = 0;
        let curr_rule2_max = 0;
        let global_max = 0;

        for (let r_ptr = 0; r_ptr < arr.length; r_ptr++) {
            //check if the idx corresponding to the current r_ptr val is valid
            //(last idx element doesnt need to follow the rule)
            let r1_valid = false;
            let r2_valid = false;
            //to do: add if statement to check if r_ptr + 1 idx is valid and what to do if it isn't (end of array)
            //(just skip to curr_max += 1, max(global_max, curr_max))
            if (r_ptr == arr.length - 1) {
                r1_valid = r2_valid = true;
            } else {
                let next_val = arr[r_ptr + 1];
                let curr_val = arr[r_ptr];
                //even valid condition
                if (r_ptr % 2 == 0) {
                    //r1 condition
                    if (curr_val < next_val) {
                        r1_valid = true;
                    } else if (curr_val > next_val) {
                        r2_valid = true;
                    }
                //odd valid condition
                } else if (r_ptr % 2 == 1) {
                    //
                    if (curr_val > next_val) {
                        r1_valid = true;
                    } else if (curr_val < next_val) {
                        r2_valid = true;
                    }
                }
            }
            
            //increment since if its not valid -> last element of an array so should be counted before we reset counter
            //if valid -> extend current subarray 

            curr_rule1_max += 1;
            curr_rule2_max += 1;

            console.log("curr idx: ", r_ptr, " curr val: ", arr[r_ptr])
            console.log("curr 1 valid: ", r1_valid, " curr_max 1: ", curr_rule1_max)
            console.log("curr 2 valid: ", r2_valid, " curr_max 2: ", curr_rule2_max)

            global_max = Math.max(curr_rule1_max, curr_rule2_max, global_max);
            //reset if not valid (current element is the start of a new array)
            if (!r1_valid) {
                curr_rule1_max = 0;
            } 
            if (!r2_valid) {
                curr_rule2_max = 0;
            }
        }
        return global_max;
    }
}
