import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort(start, end):
            if end >= len(nums) or end <= start:
                return
            chosen = random.randint(start, end)
            pivot = nums[chosen]
            nums[chosen], nums[start] = nums[start], nums[chosen]
            
            l = start
            while True:
                while l <= end and nums[l] <= pivot:
                    l += 1
                r = l + 1
                while r <= end and nums[r] > pivot:
                    r += 1
                if l > end or r > end:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            #swap back
            nums[l-1], nums[start] = nums[start], nums[l-1]
            sort(start, l - 2)
            sort(l, end)

        sort(0, len(nums) - 1)
        return nums
            
            
                

                
                
        
        
