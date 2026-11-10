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
                for j in range(i + 1, len(candidates)):
                    if j > len(candidates) - 1: return
                    if j > i + 1 and candidates[j - 1] == candidates[j]: continue
                    currSet.append(candidates[j])
                    currSum += candidates[j]
                    #print(currSet, currSum, target)
                    checkSum(j)
                    currSet.pop()
                    currSum -= candidates[j]
        
        checkSum(-1)
        return res

        