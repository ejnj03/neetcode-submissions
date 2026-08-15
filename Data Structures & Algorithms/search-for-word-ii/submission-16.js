class mapNode {
    constructor() {
        this.isWord = false;
        this.children = new Map();
        this.refs = 0;
        this.index = null;
    }
}


class Solution {
    /**
     * @param {character[][]} board
     * @param {string[]} words
     * @return {string[]}
     */
    l
    findWords(board, words) {
        const found = [];
        //create word trie from words
        const root = this.createWordTrie(words);
        const num_rows = board.length;
        const num_cols = board[0].length;
        
        //TODO: keep track of visited nodes in a different way 
        //navigate overlapping words (remove from grid (set to -1) only after we finish all the words that start at a given character
        //keep track of a set

        //curr node: the current node to check if exists in nbs of most recently visited node // visited: nodes that have been visited in this search
        const findWord = (prev_node, row, col) => {

            if (!(row < num_rows && row > -1) || !(col < num_cols && col > -1)) {
                //terminated without finding a word
                return;
            }
            
            //want to find element at r c in the children of the prev_node
            const letter = board[row][col];

            //skip if already visited during this search or part of another word
            //terminated without finding a word
            if (letter == "*") return;
            //mark it visited for now
            board[row][col] = "*";

            let curr_node;
            if (prev_node.children.has(letter)) {
                curr_node = prev_node.children.get(letter);
                //console.log("current node: ", letter)
                //console.log(curr_node)
                //console.log("board: ", board)
            } else {
                //terminate if not valid
                //unmark the board before returning
                board[row][col] = letter; 
                return;
            }
            //check if end of word
            if (curr_node.isWord && curr_node.index != -1) {
                found.push(words[curr_node.index]);
                    console.log("found state: ", found)
                                    //mark word as visited
                curr_node.index = -1;
                curr_node.refs -= 1;
                //if no more words use this sequence, terminate the search
                if (curr_node.refs == 0) {
                    //terminated after finding a word
                    //unmark and return
                    board[row][col] = letter;
                    return;
                }
            }
            const nbs = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]];
            //top bottom left right

            for (const nb of nbs) {
                //console.log("nb: ", nb)
                const [r, c] = nb;
                //whether this idx was used in a valid word
                findWord(curr_node, r, c);
            }
            //unmark
            board[row][col] = letter;
            //return whether part of valid seq
            return;
        }
        
        //iterate over all
        for (let row = 0; row < num_rows; row++) {
            for (let col = 0; col < num_cols; col++) {
                findWord(root, row, col);
            }
        }

        return found;
    }

    createWordTrie(words) {
        const root = new mapNode();

        //first create a tree from all of the words
        for (let word_i = 0; word_i < words.length; word_i++) {
            let prev_node = root;
            const word = words[word_i]
            for (let i = 0; i < word.length; i++) {
                const char = word[i];
                if (!prev_node.children.has(char)) {
                    //add char
                    prev_node.children.set(char, new mapNode());
                }
                //current node
                const curr_node = prev_node.children.get(char);
                //increment its refs
                curr_node.refs += 1;
                //if this is the last char
                if (i == word.length - 1) {
                    curr_node.isWord = true;
                    //the word
                    curr_node.index = word_i;
                }
                //update node
                prev_node = curr_node;
            }
        }
        //console.log(root)
        return root;
    }
}
