class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """
        derive length of shortest possible subsequence from sequences, and then if len(nums) == that length return True else False

        derive an adjacency list from sequences
        i.e., [1, 2, 3]
        -> [1: 2, 2: 3]
        - use sets for lists to check
        i.e., [1, 2]
        -> 2 is already in 1's adjacency list

        think of as [A ->, B ->, C] so A is in node of B
        [[1,2],[1,3],[1,2,3]] -> results in out nodes = [1: [2, 3], 2: 3]
        in nodes would be reverse: 
        in nodes = [1: [], 2: [1], 3: [1, 2]]]  ([1: 0, 2: 1, 3: 2])
        
        - if count (all unique nodes that appear in sequences < len(nums)): return False [filter for shortest possible condition ]
        - optimal sequence/ordering:
        - do level by level pruning
        i.e. start with 1:
            1 -> prune from its out nodes the count of its in nodes
            [1: 0, 2: 0, 3: 1]
            append all 0s to the q
            - only possible: there should be only 1 element appended to the q
                or else since q elements = means that for all of the current q elements its upstreams have been visited, they can be placed in any order = so there is not 1 possible supersequence, theres multiple
        """

        out_nodes = defaultdict(set)
        in_nodes = defaultdict(int)
        visited = set()

        for seq in sequences:
            for i in range(len(seq)):
                if seq[i] not in visited:
                    visited.add(seq[i])
                if i < len(seq) - 1 and seq[i + 1] not in out_nodes[seq[i]]:
                    #prevent double counting
                    out_nodes[seq[i]].add(seq[i + 1])
                    in_nodes[seq[i + 1]] += 1

        if len(visited) != len(nums): return False 
        q = [n for n in list(visited) if in_nodes[n] == 0]
        res = []
        while len(q) > 0:
            #print(q[0], dict(out_nodes), dict(in_nodes))
            if len(q) > 1:
                return False
            node = q.pop()
            res.append(node)
            for out_node in out_nodes[node]:
                in_nodes[out_node] -= 1
                if in_nodes[out_node] == 0:
                    if len(q) > 0: return False
                    q.append(out_node)

        #print(res)
        return True if res == nums else False
            

        
