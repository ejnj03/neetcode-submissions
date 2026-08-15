class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = {i : [] for i in range(numCourses)}
        for prereq, course in prerequisites:
            prereqs[course].append(prereq)
        print(prereqs)

        all_prereqs = {i : set() for i in range(numCourses)}
        visited = set()

        def dfs(course, all_p):
            if course in visited:
                all_p.add(course)
                all_p.update(all_prereqs[course])
                return

            for prereq in prereqs[course]:
                rec_prereqs = set()
                #find all of its prereqs
                dfs(prereq, rec_prereqs)
                print("prereq: ", prereq, " ret: ", rec_prereqs, " to ", course)
                all_p.update(rec_prereqs)
                
            print("course: ", course, all_p)
            #add all of its prereqs
            all_prereqs[course].update(all_p)
            #add it for the course that called it
            all_p.add(course)
            #mark it as visited
            visited.add(course)
            return

        for course in range(numCourses):
            dfs(course, set())

        res = [False for _ in range(len(queries))]
        for q_i, [prereq, course] in enumerate(queries):
            if prereq in all_prereqs[course]:
                res[q_i] = True

        return res
        
        