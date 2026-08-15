class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        nums.sort((a, b) => a - b)
        console.log(nums)
        //maintain a min heap of length k, so that the root element always corresponds to the kth largest element
        //k + 1 as we X care about 0th idx element
        this.heap = nums.length < k+1 ? new Array((k + 1) - nums.length).fill(-1001).concat(nums.slice(-k)) : nums.slice(-(k+1))
        console.log("heap: ", this.heap)
        this.heap[0] = null
        this.k = k
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val) {
        
        const heap = this.heap
        console.log("current heap state: ", heap, " val: ", val)
        const k = heap.length - 1

        //if smaller (or equal to) kth, then we don't care 
        if (val <= heap[1] && heap.length - 1) {
            return heap[1]
        }
        //if larger than k
        //swap and bubble down
        
        heap[1] = val
        let curr_i = 1
        console.log("bubbling down: ", heap)
        //heap size is k + 1 so last idx will be k
        while(curr_i <= k) {
            const left_i = 2 * curr_i <= k ? 2 * curr_i : null
            const right_i = 2 * curr_i + 1 <= k ? 2 * curr_i + 1 : null
            let swap_idx = null
            if (left_i && right_i) {
                //swap with the lower of the two, so we maintain root is min
                swap_idx = heap[left_i] <= heap[right_i] ? left_i : right_i
            } else if (left_i) {
                swap_idx = left_i
            } else if (right_i) {
                swap_idx = right_i
            } else {
                //no children 
                break
            }
            //check if min of its children is < val (so need to swap)
            if (heap[swap_idx] >= val) {
                //can stop bubble down
                break
            }
            //bubble down
            heap[curr_i] = heap[swap_idx]
            heap[swap_idx] = val
            curr_i = swap_idx
        }
        console.log("ordered: ", heap)
        return heap[1]
    }
}
