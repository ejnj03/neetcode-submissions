import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort(start, end):
            if end >= len(nums) or end <= start:
                return
            #quicksort 
            #choose a random pivot
            chosen = random.randint(start, end)
            #swap with the first element in the array
            pivot = nums[chosen]
            #print("pivot: ", pivot)
            nums[chosen] = nums[start]
            nums[start] = pivot

            l = start
            while True:
                #move left to a val greater than pivot
                while l <= end and nums[l] <= pivot:
                    l += 1
                r = l + 1
                #move right to val less than pivot
                while r <= end and nums[r] > pivot:
                    r += 1
                #check that both are in bounds
                if l > end or r > end:
                    break
                #swap the vals 
                l_val = nums[l]
                nums[l] = nums[r]
                nums[r] = l_val
                #increment l 
                l += 1
                #print("step:", nums[start:end + 1])
            #swap back
            l_val = nums[l - 1]
            nums[l-1] = pivot
            nums[start] = l_val
            #print(nums[start:end + 1])
            #print("recursing: ", start, l - 2)
            sort(start, l - 2)
            #print("recursing: ", l, end)
            sort(l, end)
            #print("returning: ", nums[start:end + 1])
        sort(0, len(nums) - 1)
        return nums
            
            
                

                
                
        
        
