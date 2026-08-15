class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        #filter edge cases
        if target > tot or target < -tot: return 0

        prev = defaultdict(int)

        prev[-nums[0]] += 1
        prev[nums[0]] += 1

        #iterate over each val in the list
        for idx in range(1, len(nums)):
            curr = defaultdict(int)
            val = nums[idx]
            for cap in prev.keys():
                combs = [cap - val, cap + val]
                for comb in combs:
                    curr[comb] += prev[cap]
            print(val, curr)
            prev = curr
        
        return prev[target]


                