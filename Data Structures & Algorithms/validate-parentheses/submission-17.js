class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        //number of opening chars = number of closing chars
        const matches = {"{":"}", "(":")", "[":"]"}
        const openings = ["{", "[", "("]
        //dynamic array
        const stack = [];
        //removes decimals
        for (let i = 0; i < s.length; i++) {
            console.log("stack: ", stack)
            console.log("s[i]:", s[i])
            if (openings.includes(s[i])) {
                //push the char onto the stack
                stack.push(s[i]);
            } else {
                //if its a closing char, the most recent opening pushed onto stack should be its match
                try {
                    const opening = stack.pop();
                    console.log("to match", matches[opening])
                    if (s[i] != matches[opening]) {
                    //if it doesnt match, return false
                        return false;
                    }
                } catch(e) {
                    //more closings than openings
                    return false;
                } 
            } 
        }
        if (stack.length > 0) {
            //more openings than closings
            return false;
        }
        return true 
    }
}