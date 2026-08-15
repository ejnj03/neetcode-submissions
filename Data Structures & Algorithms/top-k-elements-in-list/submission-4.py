class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        tots = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            counts[n] += 1
        for c, v in counts.items():
            tots[v].append(c)
        print(tots)
        ordered = []
        #for tot in tots:
            #ordered += tot
        #ordered.reverse()
        for i in range(len(tots) - 1, 0, -1):
            ordered += tots[i]
        return ordered[:k]