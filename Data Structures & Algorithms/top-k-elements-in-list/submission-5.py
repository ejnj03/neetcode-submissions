class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        k most frequent elems = maintain refs to top k count 
        min heap
        when num's count >= kth most frequent, pop kth and push
        """
        
        counter = defaultdict(int)
        
        for num in nums:
            counter[num]+=1
        
        h = []
        for n, freq in counter.items():
            if len(h) == k and h[0][0] < freq:
                heapq.heappop(h)
                heapq.heappush(h, (freq, n))
            elif len(h) < k:
                heapq.heappush(h, (freq, n))
        
        return [item[1] for item in h]
