class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        offset = ord("A")

        for task in tasks:
            counts[ord(task) - offset] += 1
        
        ceil = max(counts)
        tot = sum([1 if count == ceil else 0 for count in counts])

        return max((n + 1) * (ceil - 1) + tot, len(tasks))
        


