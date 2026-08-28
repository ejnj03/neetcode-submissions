class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        #identify only the starting elements, skip the rest
        #so that total iterations of inner loop = chain length 
        #net count across all chains is n so its O(n)
        res = 0
        for elem in elems: #only unique elements
            if elem - 1 in elems: continue #not a root
            offset = 1
            while elem + offset in elems:
                offset += 1
            res = max(offset, res)

        return res
            