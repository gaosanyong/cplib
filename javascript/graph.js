/**
 * @author Ye Gao
 * @description Graph algorithms
 * @license MIT License
 * @name graph.js
 * @see {@link https://github.com/gaosanyong/cplib} for further information.
 * @version 0.0.1
 */


/**
 * Find strongly connected components of a digraph.
 *
 * @param {number[][]} graph - a digraph as adjacency list.
 */
function tarjan(graph) {
    const n = graph.length;
    const ids = Array(n).fill(-1);
    const low = Array(n).fill(-1);
    const on = Array(n).fill(false);
    const stack = [];
    let k = 0;

    function dfs(u) {
        stack.push(u);
        on[u] = true;
        ids[u] = low[u] = k++;
        for (const v of graph[u]) {
            if (ids[v] == -1) dfs(v);
            if (on[v]) low[u] = Math.min(low[u], low[v]);
        }
        if (ids[u] == low[u])
            while (true) {
                const x = stack.pop();
                on[x] = false;
                low[x] = ids[u];
                if (x == u) break;
            }
    }

    for (let u = 0; u < n; ++u)
        if (ids[u] == -1) dfs(u);
    return low;
}
