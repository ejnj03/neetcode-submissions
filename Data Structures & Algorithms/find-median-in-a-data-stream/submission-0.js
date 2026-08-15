class MedianFinder {
    constructor() {
        this.lower = new MaxPriorityQueue();
        this.upper = new MinPriorityQueue();
    }

    /**
     *
     * @param {number} num
     * @return {void}
     */
    addNum(num) {
        //first add it to lower
        this.lower.enqueue(num);
        //1. check for max lower < min upper
        if (this.upper.size() > 0 && this.upper.front() < this.lower.front()) {
            //pop from lower and add to upper
            this.upper.enqueue(this.lower.dequeue())
        }
        //2. check for size discrepancy
        if (Math.abs(this.lower.size() - this.upper.size()) > 1) {
            //if by more than 1 
            const larger = this.lower.size() > this.upper.size() ? this.lower : this.upper
            const smaller =  this.lower.size() < this.upper.size() ? this.lower : this.upper
            //dequeue from larger and enqueue to smaller
            smaller.enqueue(larger.dequeue())
        }
    }

    /**
     * @return {number}
     */
    findMedian() {
        //even number of elements
        if (this.upper.size() > this.lower.size()) {
            return this.upper.front()
        } else if (this.lower.size() > this.upper.size()) {
            return this.lower.front()
        } else {
            //console.log(this.upper, this.lower)
            return (this.upper.front() + this.lower.front())/2
        }
    }
}
