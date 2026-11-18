class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        nb - node - nb 
        of longest + second longest nb + 1
        ㄴ update res using this 
        ㄴ return longest nb + 1 

        node w 1 nb = leaf 
        root?? - you can technically think of anything as the root 
        """
        #create adjacency list 
        nbs = defaultdict(list)
        for ai, bi in edges:
            nbs[ai].append(bi)
            nbs[bi].append(ai)
        
        visited = set() #avoid cycles (going from parent - child - parent)
        res = 0

        def dfs(node):
            nonlocal visited, res
            visited.add(node) #mark visited to prevent cycles
            heap = [0, 0] #min heap of size 2 (heap[0] = second largest)
            for nb in nbs[node]:
                if nb in visited: continue 
                longest_path = dfs(nb)
                if longest_path > heap[0]: #> than 2nd largest
                    heapq.heappop(heap)
                    heapq.heappush(heap, longest_path)
            res = max(sum(heap), res) #1st and 2nd largest + 1
            return heap[-1] + 1 #longest path inc curr node 
        
        dfs(0)
        return res
                
        
            