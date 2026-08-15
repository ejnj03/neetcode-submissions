class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        ordered = sorted(counts.keys(), key=lambda x: -counts[x])
        return ordered[:k]