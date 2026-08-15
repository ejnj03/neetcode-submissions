class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.arr = new Array(capacity);
        //console.log("array of size: ", this.arr.length)
        this.endptr = -1;
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.arr[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        //assume i <= this.endptr 
        this.arr[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        //console.log(`pushing back ${n}`)
        //if the current array is full
        if (this.getCapacity() == this.getSize()) {
            //resize the array
            this.resize()
        }
        //update location of the last element in the array
        this.endptr += 1;
        this.arr[this.endptr] = n;
        //console.log(this.arr)
    }

    /**
     * @returns {number}
     */
    popback() {
        //assuming arr is non empty (this.endptr > -1)
        //console.log("popping back, updating last element to ", this.arr[this.endptr - 1])
        const last_elem = this.arr[this.endptr];
        this.endptr -= 1;
        return last_elem;
    }

    /**
     * @returns {void}
     */
    resize() {
        //assume called when the previous array is full
        const prev_size = this.getCapacity()
        //console.log("resizing array of size: ", prev_size);
        const new_arr = new Array(prev_size * 2);
        for (let i = 0; i < prev_size; i++) {
            new_arr[i] = this.arr[i];
        }
        //endptr idx remains the same
        this.arr = new_arr;
        //console.log("resized array: ", this.arr)
    }

    /**
     * @returns {number}
     */
    getSize() {
        //how much of the array is filled
        //console.log("array of size: ", this.arr.length)
        //console.log(this.arr)
        return this.endptr + 1;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.arr.length;
    }
}
