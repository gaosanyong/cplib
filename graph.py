"""
NAME 
    graph - graph algorithms

DESCRIPTION
    This module implements a few graph-related algorithms. 

    * tpsort          topological sort via Kahn's algo
    * tpsort3         topological sort via tri-coloring
    * tarjan          find bridges (critical edges) via Tarjan's algo
    * hierholzer      find Eulerian path
    * dijkstra        find shortest path via Dijkstra's algo (all positive edges)
    * bellman_ford    find shortest path via Bellman-Ford algo (negative edges)
    * floyd_warshall  find shortest path for all pairs via Floyd-Warshall algo
    * kruskal         find minimum spanning tree via Kruskal's algo
    * prim            find minimum spanning tree via Prim's algo

FUNCTIONS
    tpsort(graph, indeg) 
        Topologically sort a digraph via Kahn's algo.

    tpsort3(graph)
        Topologically sort a digraph via tri-coloring.

    tarjan(grpah)
        Find bridges (critical edges) via Tarjan's algo.

    eulerian(graph)
        Check if an Eulerian path exists.

    hierholzer(graph)
        Find an Eulerian path via Hierholzer's algo.
"""

def tpsort(graph: Dict[int, List[int]], indeg: List[int]) -> List[int]:
    """Topologically sort a digraph via Kahn's algo."""
    stack = [n for n in graph if indeg[n] == 0]
    ans = []
    while stack: 
        n = stack.pop()
        ans.append(n)
        for nn in graph.get(n, []): 
            indeg[nn] -= 1
            if indeg[nn] == 0: stack.append(nn)
    if len(ans) == len(indeg): return ans
    return [] # cycle detected 


def tpsort3(graph: Dict[int, List[int]]) -> List[int]:
    """Topologically sort a digraph via tri-coloring."""
        
    def dfs(n):
        """Return True if a cycle is detected."""
        if visited[n]: return visited[n] == -1 # mark GRAY
        visited[n] = -1
        for nn in digraph.get(n, []):
            if visited[nn] != 1 and dfs(nn): return True 
        ans.append(n)
        visited[n] = 1 # mark BLACK
        return False 
    
    ans = []
    visited = [0]*len(graph) # WHITE
    for n in range(len(graph)): 
        if dfs(n): return [] 
    return ans[::-1]


def tarjan(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Find bridges (critical edges) via Tarjan's algo."""
    n = len(graph)
    
    def dfs(x, p, step): 
        """Traverse the graph and collect bridges via Tarjan's algo."""
        disc[x] = low[x] = step
        for xx in graph.get(x, []): 
            if disc[xx] == inf: 
                step += 1
                dfs(xx, x, step)
                low[x] = min(low[x], low[xx])
                if low[xx] > disc[x]: ans.append([x, xx]) # bridge
            elif xx != p: low[x] = min(low[x], disc[xx])
    
    ans = []
    low = [inf]*n
    disc = [inf]*n
    
    dfs(0, -1, 0)
    return ans 


"""
DEFINITIONS
    * An Eulerian path is a path in a finite graph that visits every edge exactly once. 
    * An Eulerian circuit is an Eulerian path that starts and ends on the same vertex.

CONDITIONS
    * A directed graph has an Eulerian cycle iff every vertex has equal in 
      degree and out degree, and all of its vertices with nonzero degree belong 
      to a single strongly connected component.
    * A directed graph has an Eulerian path iff at most one vertex has 
      (out-degree) − (in-degree) = 1, at most one vertex has 
      (out-degree) − (in-degree) = -1, every other vertex has equal in-degree and 
      out-degree, and all of its vertices with nonzero degree belong to a single 
      connected component of the underlying undirected graph.
"""

def hierholzer(graph):
    """Find an Eulerian path via Hierholzer algo"""
    degree = [0]*len(graph) # net out degree 
    for u in graph: 
        degree[u] += len(graph[u])
        for v in graph[u]: degree[v] -= 1
    cnt0 = cnt1 = start = 0 
    for x in degree: 
        if abs(x) > 1: return # no Eulerian path 
        if x == 1: 
            start = x
            cnt0 += 1
        elif x == -1: cnt1 += 1
    if not (cnt0 == cnt1 == 0 or cnt0 == cnt1 == 1): return # no Eulerian path 

    ans = []
    # iterative implementation of Hierholzer's algo
    stack = [start]
    while stack: 
        while graph[stack[-1]]: 
            stack.append(graph[stack[-1]].pop())
        ans.append(stack.pop())
    """
    # recursive implementation of Hierholzer's algo
    def fn(x): 
        while graph[x]: fn(graph[x].pop()) 
        ans.append(x)
    fn(start)
    """
    ans.reverse()
    return ans 


# Dijkstra's algo 

def dijkstra(): 
    pass 

# Bellman-Ford algo 

def bellman_ford(): 
    pass 

# Floyd-Warshall algo 

def floyd_warshall(): 
    pass 

# minimum spanning tree 

# Kruskal's algo 

def kruskal():
    pass 

# Prim's algo 

def prim():
    pass 