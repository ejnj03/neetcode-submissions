class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Intuition:
        
        - same number = every bit is identical 
            - so the XOR of 2 identical numbers (since 0 0 => 0, 1 1 => 0) will be 0
            so the XOR product of every identical pair of numbers = 0
            that XOR'ed with the single occuring number:
                pair ^ total    single number      result 
                    0               1               1
                    0               0               0 
            only the single number falls through 
        """
        res = 0 
        for n in nums:
            res ^= n
        return res