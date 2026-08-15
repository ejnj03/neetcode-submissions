class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxHeap = new MaxPriorityQueue()
        //heapify
        for (const stone of stones) {
            maxHeap.enqueue(stone)
        }
        //console.log(maxHeap)
        //console.log(maxHeap.size())
        while(true) {
            if (maxHeap.size() <= 1) {
                break
            }
            const s1 = maxHeap.dequeue()
            const s2 = maxHeap.dequeue()
            //console.log(s1, s2)
            //console.log(maxHeap)
            if (s1 == s2) {
                continue
            } if (s2 > s1) {
                maxHeap.enqueue(s2 - s1)
            } else {
                maxHeap.enqueue(s1 - s2)
            }
            //console.log("updated ", maxHeap)
        }
        return maxHeap.size() == 1 ? maxHeap.dequeue() : 0
    }
}
