class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        starts: 
        init: start w every position marked to 1 (longest subseq ending at i is 1)
            for number in nums:
                for prev in idxs before it
                    if prev < number: res[number] = max(res[number], res[prev] + 1)
        """
        counts = [1] * len(nums)
        for ei in range(len(nums)):
            for pi in range(0, ei):
                if nums[pi] >= nums[ei]: continue #cant be extended by ei
                counts[ei] = max(counts[pi] + 1, counts[ei])
    
        return max(counts)