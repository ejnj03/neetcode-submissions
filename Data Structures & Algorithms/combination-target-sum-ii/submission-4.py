class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        currSet, currSum = [], 0
        candidates.sort()

        def checkSum(i):
            nonlocal currSet, currSum
            if currSum > target: return
            if currSum == target:
                res.append(currSet.copy())
            if currSum < target:
                visited = set()
                for j in range(i + 1, len(candidates)):
                    if j > len(candidates) - 1: return
                    if candidates[j] in visited: continue #non unique number
                    currSet.append(candidates[j])
                    currSum += candidates[j]
                    visited.add(candidates[j])
                    checkSum(j)
                    currSet.pop()
                    currSum -= candidates[j]
        
        checkSum(-1)
        return res

        