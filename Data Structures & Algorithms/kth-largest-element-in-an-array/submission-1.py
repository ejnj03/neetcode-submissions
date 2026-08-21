class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maintain top k- max heap
        curr = nums[:k]
        heapq.heapify(curr)
        for i in range(k, len(nums)):
            if nums[i] > curr[0]:
                heapq.heappop(curr)
                heapq.heappush(curr, nums[i])
        
        return curr[0]