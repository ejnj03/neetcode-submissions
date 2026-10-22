class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        #start at end, iterate through 
        #at each position:
        # store the min number of jumps it takes to get to the end
        # end: 0
        # end - 1: 1 if >= 1 else -1 (not possible)
        # end - 2: 1 + min of all possible travelable positions
        # end - n: 
            # 1 + min of all possible travelable positions
        
        approx. of sum(n) = ( n + 1 ) * n /2
        2 1 2 1 0
                0

        - top down vs bottom up dp
        """
        n = len(nums)
        counter = [n] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                counter[i] = 0
            elif nums[i] > 0:
                r = min(len(nums), i + nums[i] + 1)
                counter[i] = min([1 + min(counter[i + 1: r]), counter[i]])
            #print(counter)
        return counter[0] 
    