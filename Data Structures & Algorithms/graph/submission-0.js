class Graph {
    constructor() {
        this.graph = new Map()
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {void}
     */
    addEdge(src, dst) {
        if (!(this.graph.has(src))) {
            this.graph.set(src, new Set())
        }
        this.graph.get(src).add(dst)
        console.log(this.graph)
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    removeEdge(src, dst) {
        if (!(this.graph.has(src))) return false
        if (this.graph.get(src).has(dst)) {
            this.graph.get(src).delete(dst)
            return true
        }
        return false
    }

    /**
     * @param {number} src
     * @param {number} dst
     * @return {boolean}
     */
    hasPath(src, dst) {
        const dfs = (source, dest) => {
            console.log(source, dest)
            if (dest == source) return true
            if (!this.graph.has(source)) return false //isnt dest and doesnt have it
            for (const child of this.graph.get(source)) {
                console.log(child, " child of ", source)
                if (dfs(child, dest)) return true
            }
            return false
        }
        return dfs(src, dst)
    }
}
