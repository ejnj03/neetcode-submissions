class Node {
    constructor() {
        this.isWord = false;
        this.children = new Map();
    }
}

class WordDictionary {
    constructor() {
        this.root = new Node();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        let node = this.root;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            
            if (!node.children.has(char)) {
                 node.children.set(char, new Node());   
            }
            //update
            node = node.children.get(char);
            if (i == word.length - 1) {
                node.isWord = true;
            }
        }

    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        
        const searchWord = (word, root) => {
            let prev_node = root;
            for (let i = 0; i < word.length; i++) {
                const char = word[i];
                //console.log(char);
                //check if its a period
                if (char == ".") {
                    //if this is the last we only care if theres a char that is last
                    let isLast = false;
                    if (i == word.length - 1) {
                        isLast = true;
                    }
                    for (const node of prev_node.children.values()) {
                        let result;
                        //search 
                        if (isLast) {
                            result = node.isWord;
                        } else {
                            result = searchWord(word.slice(i+1), node);
                        }
                        if (result) {
                            return true;
                        }
                    }
                    return false;
                }
                if (!prev_node.children.has(char)) {
                    return false;
                }
                //update
                prev_node = prev_node.children.get(char);
                if (i == word.length - 1 && !prev_node.isWord) {
                    return false;
                }
                console.log(prev_node)
            }
            return true;
        }
        return searchWord(word, this.root);
    }
}
