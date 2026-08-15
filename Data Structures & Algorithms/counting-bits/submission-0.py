class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]

        def count(num):
            counter = 0
            while num > 0:
                if num < len(counts):
                    return counts[num] + counter
                #removes one 1 from bit rep of the number
                num &= num - 1
                counter += 1
            return counter

        for i in range(1, n + 1):
            counts.append(count(i))
        
        return counts
