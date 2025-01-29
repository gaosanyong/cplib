import java.util.*;

class Graph {
    public int[] tarjan(Set<Integer>[] graph) {
        int k = 0, n = graph.length;
        int[] ids = new int[n]; Arrays.fill(ids, -1);
        int[] low = new int[n]; Arrays.fill(low, -1);
        Stack<Integer> stk = new Stack<>();
        boolean[] on = new boolean[n];
        for (int u = 0; u < n; ++u)
            if (ids[u] == -1) dfs(u, k, graph, ids, low, stk, on);
        return low;
    }

    private int dfs(int u, int k, Set<Integer>[] graph, int[] ids, int[] low, Stack<Integer> stk, boolean[] on) {
        stk.push(u);
        on[u] = true;
        ids[u] = low[u] = k++;
        for (var v : graph[u]) {
            if (ids[v] == -1) k = dfs(v, k, graph, ids, low, stk, on);
            if (on[v]) low[u] = Math.min(low[u], low[v]);
        }
        if (ids[u] == low[u])
            while (true) {
                var x = stk.pop();
                on[x] = false;
                low[x] = ids[u];
                if (x == u) break;
            }
        return k;
    }
}
