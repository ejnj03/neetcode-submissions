class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        j - i of idx j > i and t[j] > t[i]
        
        - init res to 0s 
        - pop everything that came before it (store idxs) that has a value < it
        then add it

        for stack top [b, a] bottom
        guarenteed that b (most recently added) temp < a bc if b > a then a would have been popped before b was added (so stack order cannot be top [ higher temp, lower temp] bottom in which case if higher temp < curr temp < lower temp then lower temp would miss its idx)
        """
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res