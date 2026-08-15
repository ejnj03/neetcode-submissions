class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let curr = this.head;
        let i = 0;
        while (curr) {
            if (i == index) {
                return curr.val;
            }
            i += 1;
            curr = curr.next;
        }
        
        console.log("get: ", index)
        console.log("current vals: ", this.getValues())

        return -1; 
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let node = new Node(val);
        //no nodes in list
        if (!this.tail) {
            this.tail = node;
        }
        //set next node to current head
        node.next = this.head;
        //set this to the new head
        this.head = node;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const node = new Node(val);
        //if there are no nodes 
        if (!this.head) {
            this.head = node;
        }
        //set next node to current head
        if (this.tail) {
            this.tail.next = node;
        }
        this.tail = node;
        console.log("inserted: ", val, " array: ", this.getValues())
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let curr = this.head;
        //let node = null;
        let prev = null;
        let to_remove = null;
        let i = 0;
        while (curr) {
            if (i == index - 1) {
                prev = curr;
            }
            if (i == index) {
                to_remove = curr;
                break;
            }
            i += 1;
            curr = curr.next;
        }
        
        if (to_remove) {
            //if the previous value doesnt exist
            if (!prev) {
                this.head = to_remove.next;
            } else {
                //prev val exists
                prev.next = to_remove.next;
                //if the removed node was the last node
                if (!to_remove.next) {
                    this.tail = prev;
                }
            }
            console.log("removed idx: ", index, " array: ", this.getValues())
            return true;
        }
        return false; 
    }   

    /**
     * @return {number[]}
     */
    getValues() {
        const result = []
        let curr = this.head;
        while (curr) {
            //
            result.push(curr.val)
            //update curr to the next node
            curr = curr.next;
        }
        return result
    }
}
