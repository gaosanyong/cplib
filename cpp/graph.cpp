#include <functional>
#include <stack>
#include <vector>

using namespace std; 

vector<int> tarjan(vector<vector<int>>& graph) {
    int n = graph.size(); 
    vector<int> ids(n, -1); 
    vector<int> low(n, -1); 
    vector<bool> on(n);
    stack<int> stk;
    int k = 0; 

    function<void(int)> dfs = [&](int u) {
        stk.push(u);
        on[u] = true;
        ids[u] = low[u] = k++;
        for (auto& v : graph[u]) {
            if (ids[v] == -1) dfs(v);
            if (on[v]) low[u] = min(low[u], low[v]);
        }
        if (ids[u] == low[u])
            while (true) {
                auto x = stk.top(); stk.pop();
                on[x] = false;
                low[x] = ids[u];
                if (x == u) break;
            }
    };

    for (int u = 0; u < n; ++u)
        if (ids[u] == -1) dfs(u);
    return low;
}
