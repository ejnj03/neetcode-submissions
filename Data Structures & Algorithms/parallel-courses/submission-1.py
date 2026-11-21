class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        want path length so instead of a checking set, maintain a longest_path counter to verify whether the node's path was already checked
        """

        #adjacency list
        prerequsites = [[] for _ in range(n + 1)]
        no_dependents = [True for _ in range(n + 1)]
        for prereq, course in relations:
            prerequsites[course].append(prereq)
            no_dependents[prereq] = False 
        
        #longest path starting at node
        longest_paths = [0 for i in range(n + 1)] 
        def dfs(course, dependents): #prereqs = previously visited nodes
            nonlocal longest_paths
            #print(course, dependents, longest_paths)
            if longest_paths[course] != 0: return
            if course in dependents:
                longest_paths[course] = -1
            elif longest_paths[course] == 0:
                #add it to the path before visiting dependent courses 
                longest_paths[course] = 1 #mark visited
                dependents.add(course)
                for prereq in prerequsites[course]:
                    #print(longest_paths[course])
                    dfs(prereq, dependents)
                    if longest_paths[prereq] == -1:
                        longest_paths[course] = -1
                        break
                    longest_paths[course] = max(1 + longest_paths[prereq], longest_paths[course])
                dependents.remove(course)

        
        for course in range(1, n+1):
            if no_dependents[course]:
                dfs(course, set())

        return max(longest_paths[1:]) if min(longest_paths[1:]) > 0 else -1