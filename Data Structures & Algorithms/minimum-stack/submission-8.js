class MinStack {
    constructor() {
        this.stack = [];
        this.minstack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.minstack.length > 0) {
            //min of the stack excluding current element
            const curr_min = this.minstack[this.minstack.length - 1];
            this.minstack.push(Math.min(curr_min, val));
            //console.log("min val:", Math.min(curr_min, val))
        } else {
            //if no vals yet then this val is naturally the min
            this.minstack.push(val);
        }
        //console.log("min stack: ", this.minstack);
        //console.log("stack: ", this.stack);
    }

    /**
     * @return {void}
     */
    pop() {
        //also pop from min stack
        this.minstack.pop();
        return this.stack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minstack[this.minstack.length - 1];
    }
}
