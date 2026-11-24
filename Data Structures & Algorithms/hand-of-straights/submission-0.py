class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = defaultdict(int)
        for val in hand:
            counter[val] += 1
        
        vals = sorted(list(set(hand)))
        start_i = 0 #idx on vals; start val of a group

        while start_i < len(vals):
            start = vals[start_i]
            if counter[start] <= 0:
                start_i += 1 #no more groups that start at current val
            else:
                for i in range(groupSize):
                    if start + i not in counter or counter[start + i] <= 0:
                        return False #incomplete group
                    counter[start + i] -= 1

        return True  