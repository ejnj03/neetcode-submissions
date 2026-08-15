class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        ex. 
        A: [1 3 5 7 9]
        B: [2 8 8 8 10]
        total 10 so initial K = 6 (want to find 6th largest number in A + B)
        """

        (A, B) = (nums1, nums2) if len(nums2) > len(nums1) else (nums2, nums1)
        combined = len(A) + len(B)
        l, r = 0, len(A) - 1 #all or none case
        is_odd = True if (combined) % 2 == 1 else False
        target = combined // 2 + 1 if is_odd else combined // 2 #the middle element
        while True:
            pa = (l + r) // 2 #idx  
            mid = pa + 1 #number of elements in left of a 
            #index of possible B partition 
            pb = (target - mid) - 1 #total - from a, 0 idxed so -1
            
            #skip by considering as always less than right elem
            vpa = float('-inf') if pa < 0 else A[pa]
            vpb = float('-inf') if pb < 0 else B[pb]
            print(vpa, vpb)
            #right elems of each partition
            ar = float('inf') if pa > len(A) - 2 else A[pa + 1]
            br = float('inf') if pb > len(B) - 2 else B[pb + 1]
            print(ar, br)
            #if the value in the left partition of a is greater than min(right B) 
            if vpa > br:
                r = pa - 1
            elif vpb > ar: #increase lower bound (increase partition)
                l = pa + 1
            else:
                #found correct partition
                if is_odd:
                    return max(vpa, vpb)
                return (max(vpa, vpb) + min(ar, br))/2
                
                
            
       
    
        