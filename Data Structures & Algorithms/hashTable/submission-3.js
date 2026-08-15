class HashTable {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.hashMap = new Array(capacity).fill(null)
        this.curr_size = 0
    }

    /**
     * converts the key into idx at current hashMap
     */
    convert(key) {
        let idx = 0
        for (let i = 0; i < key.length; i++) {
            const char = key[i]
            idx += char.charCodeAt()
        }
        return idx % this.capacity
    }

    insert_pair(key, value) {
        let idx = this.convert(key)

        while(true) {
            const position = idx % this.getCapacity()
            if (this.hashMap[position] == null || this.hashMap[position] == "visited") {
                this.hashMap[position] = {"key": key, "val": value}
                this.curr_size += 1
                //console.log("updated size: ", this.curr_size)
                break
            } else if (this.hashMap[position].key == key) {
                this.hashMap[position].val = value
                break
            } 
            idx += 1
        }
    }
    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    insert(key, value) {
        this.insert_pair(key, value)
        
        //more than half of capacity filled
        if (Math.floor(this.getCapacity() / 2) == this.getSize()) {
            this.resize()
        }
        //console.log("Inserted key: ", key)
        //console.log("current size: ", this.getSize())
        //console.log(this.hashMap)
    }

    getIndex(key) {
        //console.log(this.hashMap)
        const start_idx = this.convert(key)
        //let idx = start_idx
        for (let idx = start_idx; idx < start_idx + this.getCapacity(); idx++) {
            const to_look = idx % this.getCapacity()
            if (this.hashMap[to_look] == null) {
                break
            }
            if (this.hashMap[to_look].key == key) {
                return to_look
            }
            if (to_look == start_idx - 1) {
                break
            }
        }
        return -1
    }
    /**
     * @param {number} key
     * @returns {number}
     */
    get(key) {
        //console.log("Looking for key: ", key)
        //console.log(this.hashMap)
        const target_idx = this.getIndex(key)
        console.log("get result: ", target_idx)
        return target_idx != -1 ? this.hashMap[target_idx].val : -1
    }

    /**
     * @param {number} key
     * @returns {boolean}
     */
    remove(key) {
        console.log("to remove key: ", key, " hashMap: ")
        console.log(this.hashMap)
        console.log("get key result ", this.get(key))
        if (this.get(key) == -1) {
            return false
        }
        console.log("found key")
        //want to mark as visited!
        this.hashMap[this.getIndex(key)] = "removed"
        this.curr_size -= 1
        return true
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.curr_size
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }

    /**
     * @return {void}
     */
    resize() {
        // double the capacity
        const prev_capacity = this.getCapacity()
        this.hashMap.push(...Array(prev_capacity).fill(null))
        this.capacity *= 2
        for (let i = 0; i < prev_capacity; i++) {
            if (this.hashMap[i]) {
                const pair = this.hashMap[i]
                this.hashMap[i] = null
                this.curr_size -= 1
                //console.log("updated size: ", this.curr_size)
                //console.log(this.hashMap)
                this.insert_pair(pair.key, pair.val)
            }
        }
    }
}
