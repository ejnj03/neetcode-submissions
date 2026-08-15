class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        crit = len(nums) // 3
        
        counts = defaultdict(int)
        res = set()
        for num in nums:
            if num in res:
                continue
            counts[num] += 1
            if counts[num] > crit:
                res.add(num)
        
        return list(res)