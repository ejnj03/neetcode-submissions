class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        print(prereqs)
        
        ordering = []
        #all alr added to ordering
        visited = set()
        
        def dfs(course, prev):
            #print("running dfs on ", course, prev)
            #if alr added to ordering
            if course in visited: return True
            #if contains cycle
            if course in prev: return False
            #add it to prev
            prev.add(course)
            for prereq in prereqs[course]:
                res = dfs(prereq, prev)
                #if contains cycle early ret
                if not res: return False
            #after adding all its prereqs add it to the list
            visited.add(course)
            ordering.append(course)
            return True

        for course in range(numCourses):
            res = dfs(course, set())
            if not res: return []
        
        return ordering
        
        
        