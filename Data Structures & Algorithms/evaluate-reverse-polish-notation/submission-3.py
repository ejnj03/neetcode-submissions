class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(a, b, op):
            if op == "-":
                return a - b
            if op == "+":
                return a + b
            if op == "*":
                return a * b
            if op == "/":
                return int(a / b)

        """
        stack [] (LIFO) (python list, pop from end) 
        iterate through tokens list
        if #:
            push onto stack (as int(x))
        if not #:
            pop 2 from stack (a, b)
        """
        stack = []
        for token in tokens:
            #print(token, stack)
            try:
                stack.append(int(token))
            except ValueError: #if operator 
                b, a = stack.pop(), stack.pop()
                stack.append(eval(a, b, token))
            #print(stack)
        
        return stack[0]


    
