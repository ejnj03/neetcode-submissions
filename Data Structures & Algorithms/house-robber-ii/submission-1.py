class Solution:
    #bottom up
    def rob(self, nums: List[int]) -> int:
        inc = [0, 0, 0] #includes last
        ninc = [0, 0, 0] #doest include last

        inc[(len(nums) - 1) % 3] = nums[len(nums) - 1]
        
        i = len(nums) - 2
        
        while i > -1:
            if i == 0: #can't include 0th element in either case
                inc[i % 3] = max(inc[(i + 1) % 3], inc[(i + 2) % 3])
            else:
                inc[i % 3] = max(inc[(i + 1) % 3], nums[i] + inc[(i + 2) % 3])
            ninc[i % 3] = max(ninc[(i + 1) % 3], nums[i] + ninc[(i + 2) % 3])
            i-=1
        return max(inc[0], ninc[0])
