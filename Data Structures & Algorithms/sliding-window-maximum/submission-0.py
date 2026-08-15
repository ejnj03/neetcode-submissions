class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        counts = defaultdict(int)
        ret = [float('inf')]
        nums = [-1 * n for n in nums] #minheap

        #initalize window of size k
        for i in range(k):
            if nums[i] not in counts:
                heapq.heappush(q, nums[i])
            counts[nums[i]] += 1
            ret[0] = min(nums[i], ret[0]) 

        l, r = 0, k - 1

        for l in range(1, len(nums) - k + 1):
            counts[nums[l - 1]] -= 1
            #the previous max
            prev = ret[l - 1]
            
            #the new val
            r += 1
            if counts[nums[r]] == 0:
                heapq.heappush(q, nums[r])
            counts[nums[r]] += 1

            #if max is still in the array or r is the new max
            if counts[prev] > 0 or nums[r] <= prev:
                ret.append(min(prev, nums[r]))
            else:
                #need to find new max
                to_add = heapq.heappop(q)
                while counts[to_add] == 0:
                    to_add = heapq.heappop(q)
                ret.append(to_add)
        
        return [-1 * n for n in ret]

            

            