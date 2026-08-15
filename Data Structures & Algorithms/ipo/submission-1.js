class Solution {
    /**
     * @param {number} k: number of distinct projects we can choose 
     * @param {number} w: initial capital 
     * @param {number[]} profits (profits[i]: profit from completing project i)
     * @param {number[]} capital (capital[i]: capital needed to start project)
     * @return {number}
     */
    findMaximizedCapital(k, w, profits, capital) {
        /**
         * use max heap based on profit for idxs with capital <= current budget
         * use min heap based on capital for idxs with budget > current budget
         * 
         * like sliding window, pop the current max heap root
         * increment budget
         * while min heap root idx's capital <= current budget, pop and insert to profit heap
         */
        
        
        const maxProfit = new MaxPriorityQueue((p_i)=> profits[p_i])
        const minBudget = new MinPriorityQueue((c_i)=> capital[c_i])
        const num_choices = profits.length
        //const selected = new Array

        let curr_budget = w
        //create heaps based on initial budget by iterating through idxs
        for (let i = 0; i < num_choices; i++) {
            //if capital needed is <= current budget, insert into the maxProfit heap
            if (capital[i] <= curr_budget) {
                maxProfit.enqueue(i)
            } else {
                //means capital needed > current budget
                minBudget.enqueue(i)
            }
        }

        const projects = [] //for debugging
        //select projects based on current heap state and current budget
        //need to also check that our queue for currently available projects is not empty
        while(maxProfit.size() > 0 && projects.length < k) {
            //select the project of those available to us with the max profit
            const optimalProject = maxProfit.dequeue()
            projects.push(optimalProject);
            //update our curr budget
            curr_budget+= profits[optimalProject];
            //update our heaps based on the new current budget (move all possible from minBudget heap to maxProfit heap)
            while(capital[minBudget.front()] <= curr_budget) {
                maxProfit.enqueue(minBudget.dequeue())
            }
        }
        
        return curr_budget
    }
}
