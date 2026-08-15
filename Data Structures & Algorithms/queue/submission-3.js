class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
class MyDeque {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        //return true if empty
        return this.head ? false : true;
    }

    /**
     * @param {number} value
     */
    append(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            //empty then this is head too 
            this.head = node;
        } else {
            //tail exists as long as list is not empty
            this.tail.next = node;
            node.prev = this.tail;
        }
        this.tail = node;
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            this.tail = node;
        } else {
            //if not empty head exists 
            this.head.prev = node;
            node.next = this.head;
        }
        this.head = node;
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.isEmpty()) {
            return -1;
        }
        //not empty queue = tail exists
        let tail_val = this.tail.val;
        if (this.tail.prev) {
            //if prev val exists
            let prev = this.tail.prev;
            prev.next = null;
            this.tail = prev;
        } else {
            //else tail is also head
            this.head = null;
            this.tail = null;
        }
        return tail_val;
    }

    /**
     * @return {number}
     */
    popleft() {
        if (this.isEmpty()) {
            return -1;
        }
        const head_val = this.head.val;
        //has head
        if (this.head.next) {
            let next = this.head.next;
            next.prev = null;
            this.head = next;
        } else {
            //head is also the tail
            this.head = null;
            this.tail = null
        }
        return head_val;
    }
}
