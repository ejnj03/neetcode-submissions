class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        nlogn solution 
        """
        counter = defaultdict(int)
        for val in hand:
            counter[val] += 1
        
        vals = list(counter.keys())
        start_i = 0 #idx on vals; start val of a group

        while start_i < len(vals):
            start = vals[start_i]
            if counter[start] <= 0:
                start_i += 1 #no more groups that start at current val
            else:
                #move to the start of the group
                while start - 1 in counter and counter[start - 1] > 0:
                    start -= 1
                for i in range(groupSize):
                    if start + i not in counter or counter[start + i] <= 0:
                        return False #incomplete group
                    counter[start + i] -= 1

        return True  