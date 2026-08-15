class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        elems = deque([])
        res = []
        #visits all positions
        while True:
            if r >= len(nums):
                break
            #now add the current element
            rc = nums[r]
            while len(elems) > 0 and nums[elems[-1]] < rc:
                elems.pop() #remove out of bounds or smaller elems in front of it
            elems.append(r)

            while elems[0] < l:
                elems.popleft()

            #print("curr window: ", nums[l:r+1])
            #print([nums[i] for i in list(elems)])
            if r - l + 1 == k: #r exclusive
                #inc if out of bounds
                to_add = elems[0]
                #print("adding ", nums[to_add])
                res.append(nums[to_add]) #add element at front of the queue
                l += 1

            r += 1
        return res

                
            