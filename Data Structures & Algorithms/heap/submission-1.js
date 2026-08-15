class MinHeap {
    constructor() {
        this.heap = [null]
    }

    percolate_up(curr_i) {
        //move up tree
        const parent_i = Math.floor(curr_i / 2)
        if (parent_i < 1) {
            return curr_i
        }
        const heap = this.heap
        if (heap[curr_i] < heap[parent_i]) {
            //swap
            const parent_val = heap[parent_i]
            heap[parent_i] = heap[curr_i]
            heap[curr_i] = parent_val
            return parent_i
        } else {
            return curr_i
        }
    }

    percolate_down(curr_i) {
        const heap = this.heap
        const last_idx = this.heap.length - 1
        const left_i = 2 * curr_i <= last_idx ? 2 * curr_i : null
        const right_i = 2 * curr_i + 1 <= last_idx ? 2 * curr_i + 1 : null
        let swap_idx = null
        if (left_i && right_i) {
            swap_idx = heap[left_i] <= heap[right_i] ? left_i : right_i
        } else if (left_i) {
            swap_idx = left_i
        } else if (right_i) {
            swap_idx = right_i
        } else {
            //was leaf
            return curr_i
        }
        console.log("swap idx: ", swap_idx)
        if (heap[swap_idx] >= heap[curr_i]) {
            return curr_i
        }
        const swap_val = heap[swap_idx]
        heap[swap_idx] = heap[curr_i]
        heap[curr_i] = swap_val
        return swap_idx
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        console.log("current heap", this.heap)
        this.heap.push(val)
        
        let curr_idx = this.heap.length - 1
        while(true) {
            const new_idx = this.percolate_up(curr_idx)
            if (new_idx == curr_idx) break;
            //else update curr
            curr_idx = new_idx
        }
        console.log(this.heap)
    }

    /**
     * @return {number}
     */
    pop() {
        if (this.heap.length == 1) return -1;
        if (this.heap.length == 2) return this.heap.pop();
        console.log(this.heap)
        const smallest = this.heap[1]
        this.heap[1] = this.heap[this.heap.length - 1]
        this.heap.pop()
        console.log("percolating on ", this.heap)
        let curr_idx = 1
        while(true) {
            const new_idx = this.percolate_down(curr_idx)
            if (new_idx == curr_idx) break;
            curr_idx = new_idx
        }
        console.log("done swapping ", this.heap)
        return smallest
    }

    /**
     * @return {number}
     */
    top() {
        return this.heap.length > 1 ? this.heap[1] : -1;
    }

    /**
     * @param {number[]} nums
     * @return {void}
     */
    heapify(nums) {
        for (const num of nums) {
            this.push(num)
        }
    }
}
