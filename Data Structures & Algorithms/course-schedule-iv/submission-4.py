class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = {i : [] for i in range(numCourses)}
        for prereq, course in prerequisites:
            prereqs[course].append(prereq)
        print(prereqs)

        all_prereqs = {i : set([i]) for i in range(numCourses)}
        visited = set()

        def dfs(course):
            if course not in visited:
                for prereq in prereqs[course]:
                    dfs(prereq)
                    all_prereqs[course].update(dfs(prereq))
            #mark it as visited
            visited.add(course)
            return all_prereqs[course]

        for course in range(numCourses):
            dfs(course)

        res = [False for _ in range(len(queries))]
        for q_i, [prereq, course] in enumerate(queries):
            if prereq in all_prereqs[course]:
                res[q_i] = True

        return res
        
        