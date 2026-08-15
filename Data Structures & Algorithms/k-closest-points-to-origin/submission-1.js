class Point {
    constructor(point) {
        const [x, y] = point
        this.x = x, this.y = y
        this.distance = Math.sqrt(x**2 + y**2)
    }
}
class Solution {
    /**
     * @param {number[][]} points
     * @param {number} k
     * @return {number[][]}
     */
    kClosest(points, k) {
        //console.log("About to create PQ");
        const pq = new MaxPriorityQueue((point) => point.distance);
        //console.log("PQ created successfully");
        for (const point of points) {
            //we only care if the points have shorter distance then the current kth min distance
            const p = new Point(point);
            //console.log("point", p)
            //if not filled yet just enqueue and cont
            if (pq.size() < k) {
                pq.enqueue(p)
                continue
            }
            //strictly less than the kth
            if (p.distance < pq.front().distance) {
                //enqueue and pop the k+1th
                pq.enqueue(p)
                pq.dequeue()
            }
            console.log(pq.toArray())
        }
        const result = []
        //console.log(pq)

        return pq.toArray().map(point => [point.x, point.y])
    }
}
