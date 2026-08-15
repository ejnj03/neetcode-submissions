class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        //if A is parent of B then B cannot be parent of A (no loops)
        //course : prereq
        const prereqs = new Array(numCourses).fill(null)
        //create adjacency list
        for (const pair of prerequisites) {
            const [course, prereq] = pair
            if (!prereqs[course]) {prereqs[course] = []}
            prereqs[course].push(prereq)
        }
        console.log(prereqs)

        const dfs = (course, visited) => {
            //cycle
            if (visited.has(course)) return false
            if (!prereqs[course]) return true

            visited.add(course)
                for (const prereq of prereqs[course]) {
                    if (!dfs(prereq, visited)) return false
                    //courses subtree was valid
                    //think of prereqs[course] not as all prereqs of the course but as unchecked prereqs of the course
                    //since we just checked all prereqs:
                    prereqs[course] = null
                }
            visited.delete(course)

            //none of its descendant prereqs has it as a prereq
            return true
        }

        for (let i = 0; i < numCourses; i++) {
            if (!dfs(i, new Set())) return false
            prereqs[i] = null
        }

        return true
    }
}
