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
        const checked = new Set()
        const dfs = (course, visited) => {
            //cycle
            if (visited.has(course)) return false
            if (checked.has(course)) return true
            if (!prereqs[course]) {
                checked.add(course)
            } else {
                visited.add(course)
                for (const prereq of prereqs[course]) {
                    if (!dfs(prereq, visited)) return false
                    //courses subtree was valid
                    checked.add(course)
                }
                visited.delete(course)
            }
            //none of its descendant prereqs has it as a prereq
            return true
        }

        for (let i = 0; i < numCourses; i++) {
            if (!dfs(i, new Set())) return false
        }

        return true
    }
}
