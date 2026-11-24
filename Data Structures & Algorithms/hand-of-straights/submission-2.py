class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        nlogn solution 
        """
        counter = defaultdict(int)
        for val in hand:
            counter[val] += 1
        
        vals = list(counter.keys())
        for curr in list(counter.keys()):
            if counter[curr] <= 0:
                continue
            else:
                #move to the start of the group
                start = curr
                while counter[start - 1] > 0:
                    start -= 1
                while start <= curr:
                    while counter[start] > 0:
                        for i in range(groupSize):
                            if counter[start + i] <= 0:
                                return False #incomplete group
                            counter[start + i] -= 1
                    start += 1

        return True  