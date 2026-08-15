class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.cache = {}
        this.head = null
        this.tail = null
    }

    add_to_history(key) {
        //console.log(this.cache[key])
        if (this.tail == key) {
            return
        }
        //if this is the first
        if (!this.head) {
            this.head = key
        } else if (this.head == key) {
            this.head = this.cache[key].next
        }
        if (this.cache[key].prev) {
             this.cache[this.cache[key].prev].next = this.cache[key].next
        }
        if (this.cache[key].next) {
            this.cache[this.cache[key].next].prev = this.cache[key].prev
        }
        this.cache[key].next = null
        this.cache[key].prev = this.tail
        if (this.tail) {
            this.cache[this.tail].next = key
        }
        
        this.tail = key
    }

    delete_head() {
        //console.log(this.cache[key])
        const prev_head = this.head
        if (this.cache[this.head].next) {
            this.cache[this.cache[this.head].next].prev = null
        }
        this.head = this.cache[this.head].next
        if (this.tail == prev_head) {
            this.tail = this.head
        }
    }
    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (key in this.cache) {
            this.add_to_history(key)
            console.log(this.cache, " Updated history, used ", key)
            return this.cache[key].value
        } else {
            return -1
        }
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        console.log(this.cache, " Adding: ", key)
        console.log("head: ", this.head)
        if (key in this.cache) {
            this.cache[key].value = value
        } else {
            if (Object.keys(this.cache).length >= this.capacity) {
                const to_delete = this.head
                this.delete_head()
                delete this.cache[to_delete]
            }
            this.cache[key] = {"value": value, "prev": null, "next":null}
            //console.log(this.cache)
            //console.log(this.cache[key])
        }
        this.add_to_history(key)
        console.log(this.cache, "Added: ", key)
        console.log("\n")
    }
}