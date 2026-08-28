class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        maximize min(l, r) (height)
        maximize r - l (width)
        max = (r - l) * min (l, r)
        """
        
        def getArea(l, r):
            nonlocal heights
            if r <= l:
                return 0
            width = r - l
            height = min(heights[r], heights[l])
            return width * height
        
        res = 0

        l, r = 0, len(heights) - 1
        while l < r:
            res = max(res, getArea(l, r))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                res = max(res, getArea(l + 1, r))
                res = max(res, getArea(l, r - 1))
                l, r = l + 1, r - 1

        return res
        
