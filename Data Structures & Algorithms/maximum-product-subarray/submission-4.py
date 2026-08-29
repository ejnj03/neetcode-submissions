class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #max neg/pos that includes n - 1 th element
        curr_neg = None
        curr_pos = None
        res = float('-inf')
        
        for num in nums:
            #end at current num vs start at current num
            p, n = curr_pos, curr_neg
            if num < 0:
                if p:
                    curr_neg = p * num
                else:
                    curr_neg = num
                if n:
                    curr_pos = n * num
                else:
                    curr_pos = None 
            if num >= 0:
                if p:
                    curr_pos *= num
                else:
                    curr_pos = num
                if curr_neg:
                    curr_neg *= num 
            #print(num, curr_neg, curr_pos)
            if curr_pos:
                res = max(curr_pos, res)
            res = max(num, res)
        return res