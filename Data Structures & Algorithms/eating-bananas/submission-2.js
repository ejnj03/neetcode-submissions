class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let min_speed = Number.MAX_VALUE;
        //we want the lowest valid pile size
        //let low = Math.min(...piles);
        let low = 1 //time = sum of all vals (pile val hours each)
        let high = Math.max(...piles); //time = length of array (1 hour each)
        //console.log(low, high)
        while(low <= high) {
            //console.log(low, high)
            const speed = Math.floor((high - low + 1)/2) + low;
            const time = this.total_time(piles, speed, h);
            
            if (time == -1) {
                //time was invalid (speed was too low)
                //update min 
                low = speed + 1;
            } else {
                //valid time;
                //record it
                min_speed = Math.min(speed, min_speed);
                //try a smaller value
                high = speed - 1;
            }
        }
        return min_speed;
    }

    total_time(piles, k, h) {
        // k is the eating rate
        //total is the total time it takes to eat all the piles
        let total = 0;
        for (let i = 0; i < piles.length; i++) {
            const pile = piles[i];
            //ex. if pile size is 7, k = 3 should be 3 hrs
            total += Math.ceil(pile/k);
        }
        if (total > h) {
            //invalid total
            return -1;
        } else {
            return total;
        }
    }
}
