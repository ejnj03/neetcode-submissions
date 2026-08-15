class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0 
        l = 0
        r = len(people) - 1
        
        while l <= r:
            print(l, r)
            if l == r:
                boats += 1
                break
            while people[r] >= limit and r > l:
                r -= 1
                boats += 1
            tot = people[l] + people[r]
            if tot <= limit:
                boats += 1
                r -= 1
                l += 1
            elif tot > limit:
                boats += 1
                r -= 1

        return boats
