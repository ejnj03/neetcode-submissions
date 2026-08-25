class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        bucket sort
        - can be not stable
        - have a defined range of buckets (max number of occurences = length)
        
        - get counts of each first (same as heap approach)
        - then classify into buckets

        - both counter (number of unique chars) and buckets (range of max freq) is O(N), adding to res is O(K)
        adding to each is also O(N), same for extracting top K

        **lists are by reference**
        """

        counter = defaultdict(int)
        
        for num in nums:
            counter[num]+=1


        buckets = [[] for _ in range (len(nums) + 1)] #0 to len(nums)
        
        for n, freq in counter.items():
            buckets[freq].append(n)

        res, curr = [], k
        for freq in range(len(nums), -1, -1):
            if curr == 0:
                break
            res.extend(buckets[freq])
            curr -= len(buckets[freq])
        return res
