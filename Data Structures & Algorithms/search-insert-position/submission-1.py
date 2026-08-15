class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bs(lb, rb):
            print(nums[lb], nums[rb])
            if lb == rb:
                if target <= nums[lb]:
                    return lb
                return lb + 1 #upper idx if greater 
            p = (lb + rb) // 2 #lower idx if even
            if nums[p] == target:
                return p
            if nums[p] > target:
                return bs(lb, p)
            return bs(p + 1, rb)

        l, r = 0, len(nums) - 1
        return bs(l, r)
        