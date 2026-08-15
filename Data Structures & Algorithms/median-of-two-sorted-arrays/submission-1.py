class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sz = len(nums1) + len(nums2)
        half = sz // 2
        l1, l2 = len(nums1), len(nums2)
        #larger arr 
        if len(nums1) > len(nums2):
            p1 = min(len(nums1) - 1, half)
            p2 = half - p1
        else:
            p2 = min(len(nums2) - 1, half)
            p1 = half - p2
        print(p1, p2)

        def valid(i, l):
            return True if i >= 0 and i < l else False
        
        while valid(p1, l1) and valid(p2 - 1, l2) and nums1[p1] < nums2[p2 - 1]:
            p2 -= 1
            p1 += 1
        while valid(p2, l2) and valid(p1 - 1, l1) and nums2[p2] < nums1[p1 - 1]:
            p1 -= 1
            p2 += 1
        print(p1, p2)

        
        ub = min(nums1[p1] if p1 < l1 else float('inf'), nums2[p2] if p2 < l2 else float('inf'))

        if sz % 2 == 0:
            v1, v2 = valid(p1 - 1, l1), valid(p2 - 1, l2)
            lb1, lb2 = float('-inf') if not v1 else nums1[p1 - 1], float('-inf') if not v2 else nums2[p2 - 1]  # ✓ Fixed
            lb = max(lb1, lb2)
            print(lb, ub)
            return (lb + ub) / 2
        return ub
            
        

            
                
        
