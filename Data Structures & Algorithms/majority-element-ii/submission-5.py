class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        crit = len(nums) // 3
        #max 2 elements that fit the criteria
        e1, e2 = -1, -1
        c1, c2 = 0, 0

        for num in nums:
            if e1 == num:
                c1 += 1
            elif e2 == num:
                c2 += 1
            elif c1 < 1:
                #e1 and e2 both not num
                e1, c1 = num, 1
            elif c2 < 1:
                e2, c2 = num, 1
            else:
                #what if e1 is num and e2 isnt but has valid count
                # only decrement both if both not the element
                # if either is then leave the other in tact (why)
                c1 -= 1
                c2 -= 1
            print(e1, c1, e2, c2)

        res = []
        print(crit)
        if e1 >= 0:
            count = sum([1 if n == e1 else 0 for n in nums])
            print(e1, count)
            if count > crit:
                res.append(e1)
        if e2 >= 0:
            count = sum([1 if n == e2 else 0 for n in nums])
            if count > crit:
                res.append(e2)
        return res
