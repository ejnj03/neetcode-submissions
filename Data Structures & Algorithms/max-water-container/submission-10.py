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
            #print(heights[l], heights[r], r - l)
            return width * height
        
        res = 0

        l, r = 0, len(heights) - 1
        while l < r:
            res = max(res, getArea(l, r))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
        
