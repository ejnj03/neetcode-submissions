class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: return -1
        l, r = 0, 0
        N = len(gas)
        curr = 0
        while r - l + 1 <= N:
            while curr >= 0 and r - l + 1 <= N:
                curr += gas[r % N] - cost[r % N]
                r += 1
            while curr < 0:
                curr -= gas[l] - cost[l]
                l += 1
        return l 