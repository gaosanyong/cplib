function tarjan(graph : number[][]) {
    const n = graph.length;
    const ids : number[] = Array(n).fill(-1);
    const low : number[] = Array(n).fill(-1);
    const on : boolean[] = Array(n).fill(false);
    const stack : number[] = [];
    let k = 0;

    function dfs(u : number) {
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
                if (x != undefined) {
                    on[x] = false;
                    low[x] = ids[u];
                    if (x == u) break;
                }
            }
    }

    for (let u = 0; u < n; ++u)
        if (ids[u] == -1) dfs(u);
    return low;
}
