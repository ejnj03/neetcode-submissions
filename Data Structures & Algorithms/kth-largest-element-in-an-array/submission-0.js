class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k) {
        //always k elements, where root is the smallest element (kth largest)
        //so if find larger, that becomes the root instead
        const pq = new MinPriorityQueue()
        for (const num of nums) {
            if (pq.size() < k) {
                pq.enqueue(num)
            } else {
                if (pq.front() < num) {
                    pq.enqueue(num)
                    pq.pop()
                }
            }
        }
        return pq.front()
    }
}
