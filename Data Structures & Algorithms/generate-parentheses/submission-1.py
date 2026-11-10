class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ["("]
        op, cl = 1, 0
        res = []

        def find():
            nonlocal curr, op, cl
            if len(curr) == 2 * n:
                res.append("".join(curr))
            else:
                if abs(op - cl) > 0: #more than 1 open bracket in front (unclosed)
                    cl += 1
                    curr.append(")")
                    find()
                    cl -= 1
                    curr.pop()
                if op < n: #when still have rem open brackets to use
                    op += 1
                    curr.append("(")
                    find()
                    op -= 1
                    curr.pop()
        find()
        return res
        