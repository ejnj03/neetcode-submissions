class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        dependent -> course -> prereq
        """
        prereqs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        checked = set()

        def dfs(course, dependents):
            nonlocal checked, prereqs
            if course in checked:
                return True
            dependents.add(course)
            for prereq in prereqs[course]:
                if prereq in dependents: #course's prereq is its dependent -> circular dependency
                    return False
                if not dfs(prereq, dependents): return False
            checked.add(course)
            dependents.remove(course)
            return True
        

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True 

