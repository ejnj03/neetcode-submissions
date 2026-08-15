
class Node {
    constructor() {
        this.isWord = false;
        this.children = new Map();
    }
}
class PrefixTree {
    constructor() {
        this.root = new Node();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let curr_node = this.root;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            if (!curr_node.children.has(char)) {
                curr_node.children.set(char, new Node());
            }
            curr_node = curr_node.children.get(char);
            //if last char
            if (i == word.length - 1) {
                curr_node.isWord = true;
            }
        }
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        let curr_node = this.root;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            if (!curr_node.children.has(char)) {
                return false;
            }
            //else move to the char
            curr_node = curr_node.children.get(char);
            //if last, check if word
            if (i == word.length - 1 && !curr_node.isWord) {
                return false
            }
        }
        return true;
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        let curr_node = this.root;
        for (let i = 0; i < prefix.length; i++) {
            const char = prefix[i];
            if (!curr_node.children.has(char)) {
                return false;
            }
            //else move to the char
            curr_node = curr_node.children.get(char);
            //if last, check if word
            //if (i == prefix.length - 1 && curr_node.isWord) {
                //return false;
            //}
        }
        return true;
    }
}
