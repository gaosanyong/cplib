"""
NAME 
    graph - graph algorithms

DESCRIPTION
    This module implements a few graph-related algorithms. 

    * tpsort          return a topological sort via Kahn's algo
    * tpsort3         return a topological sort via tri-coloring
    * tarjan          return the bridges (critical edges) via Tarjan's algo
    * tarjan_scc      return strongly connected components as low link
    * eulerian        check if Eulerian circuit/path exists
    * hierholzer      return a Eulerian circuit/path
    * dijkstra        return the shortest distance for a pair of nodes via Dijkstra's algo (all positive edges)
    * bellman_ford    return the shortest distnaces for a single source via Bellman-Ford algo (negative edges)
    * floyd_warshall  return the shortest distances for all pairs via Floyd-Warshall algo
    * kruskal         return a minimum spanning tree via Kruskal's algo
    * prim            return a minimum spanning tree via Prim's algo

FUNCTIONS
    tpsort(graph, indeg) 
        Topologically sort a digraph via Kahn's algo.

    tpsort3(graph)
        Topologically sort a digraph via tri-coloring.

    tarjan(grpah)
        Find bridges (critical edges) via Tarjan's algo.

    tarjan_scc(graph)
        Find strongly connected components of digraph.

    eulerian(graph)
        Check if an Eulerian path exists.

    hierholzer(graph)
        Find an Eulerian path via Hierholzer's algo.

    dijkstra(graph, start, end)
        Find shortest distance between start and end via Dijkstra's algo.

    bellman_ford(graph, start)
        Return the shortest distance from a single source

    floyd_warshall(graph)
        Return the short distances of every pair of nodes.

    kruskal(graph)
        Return the minimum spanning tree.

    prim(graph)
        Return the minimum spanning tree.
"""

def tpsort(graph: List[List[int]], indeg: List[int]) -> List[int]:
    """Kahn's algo
    Return a topological order of the digraph."""
    ans = []
    stack = [u for u in graph if indeg[u] == 0]
    while stack: 
        u = stack.pop()
        ans.append(u)
        for v in graph[u]: 
            indeg[v] -= 1
            if indeg[v] == 0: stack.append(v)
    return ans if len(ans) == len(indeg) else []


def tpsort3(graph: List[List[int]]) -> List[int]:
    """Tri-coloring algo
    Return a topological order of the digraph."""
    ans = []
    visited = [0]*len(graph) # WHITE
        
    def dfs(u):
        """Return True if a cycle is detected."""
        visited[u] = -1 # mark GRAY
        for v in digraph[u]:
            if visited[v] == -1 or not visited[v] and dfs(v): return True 
        ans.append(u)
        visited[u] = 1 # mark BLACK
        return False 
    
    for u in range(len(graph)): 
        if not visited[u] and dfs(u): return [] 
    ans.reverse()
    return ans


def tarjan(graph: List[List[int]]) -> List[List[int]]:
    """Tarjan's algo
    Return the bridges (i.e. critical edges) of a graph."""
    ans = []
    low = [inf]*len(graph)
    disc = [inf]*len(graph)
    
    def dfs(u, p, step): 
        """Traverse the graph and collect bridges via Tarjan's algo."""
        disc[u] = low[u] = step
        for v in graph[u]: 
            if disc[v] == inf: 
                step += 1
                dfs(v, u, step)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]: ans.append([u, v]) # bridge
            elif v != p: low[u] = min(low[u], disc[v])
    
    dfs(0, -1, 0)
    return ans 


def tarjan_scc(graph):
    """Tarjan's algo
    Return strongly connected components in a digraph as low link."""
    ids = [-1] * len(graph)
    low = [-1] * len(graph)
    on = [False] * len(graph)
    stack = []
    k = 0

    def dfs(u):
        nonlocal k
        stack.append(u)
        on[u] = True
        ids[u] = low[u] = k
        k += 1
        for v in graph[u]:
            if ids[v] == -1: dfs(v)
            if on[v]: low[u] = min(low[u], low[v])
        if ids[u] == low[u]:
            while True:
                x = stack.pop()
                on[x] = False
                low[x] = ids[u]
                if x == u: break

    for u in range(len(graph)):
        if ids[u] == -1: dfs(u)
    return low

"""
DEFINITIONS
    * An Eulerian path is a path that visits every edge exactly once. 
    * An Eulerian circuit is an Eulerian path that ends on the starting vertex.

CONDITIONS
    * A digraph has an Eulerian cycle iff 
      1) every vertex has equal in degree and out degree, 
      2) all of its vertices with nonzero degree belong to a single connected 
         component.
    * A digraph has an Eulerian path iff 
      1) at most one vertex has (out-degree) − (in-degree) = 1, 
      2) at most one vertex has (out-degree) − (in-degree) = -1, 
      3) every other vertex has equal in-degree and out-degree, and all of its 
         vertices with nonzero degree belong to a single connected component.
"""

def eulerian(graph: List[List[int]]) -> bool: 
    """Return start node if graph has a Eulerian circuit/path."""
    for u in range(len(graph)): 
        if u & 1: return -1
    return 0


def eulerian(digraph: List[List[int]]) -> int: 
    """Return start node if digraph has a Eulerian circuit/path."""
    degree = [0]*len(digraph) # net out degree
    for u in digraph: 
        degree[u] += len(digraph[u])
        for v in digraph[u]: degree[v] -= 1
    pos = neg = start = 0 
    for x in degree: 
        if abs(x) > 1: return -1 # no Eulerian path 
        if x == 1: 
            pos += 1
            start = x
        elif x == -1: neg += 1
    if not (pos == neg == 0 or pos == neg == 1): return -1 # no Eulerian path 
    return start 


def hierholzer(graph: List[List[int]]) -> List[int]:
    """Hierholzer's algo
    Return an Eulerian path."""
    ans = []
    start = eulerian(graph)
    if start > -1: 
        # iterative implementation of Hierholzer's algo
        stack = []
        while stack: 
            while digraph[stack[-1]]: 
                stack.append(digraph[stack[-1]].pop())
            ans.append(stack.pop())
        ans.reverse()
        """
        # recursive implementation of Hierholzer's algo
        def fn(x): 
            while graph[x]: fn(graph[x].pop()) 
            ans.append(x)
        fn(start)
        """
    return ans


def dijkstra(graph: List[List[List[int]]], start: int, end: int) -> int: 
    """Dijkstra's algo 
    Return the shortest distance between start and end."""
    pq = [(0, start)]
    dist = [inf] * n 
    dist[start] = 0 
    while pq: 
        d, u = heappop(pq)
        if u == end: return d
        for v, w in graph[u]: 
            if dist[u] + w < dist[v]: 
                dist[v] = dist[u] + w 
                heappush(pq, (dist[v], v))
    return -1 


def bellman_ford(n, edges: List[List[int]], start): 
    """Bellman-Ford algo
    Return the shortest distance from a single source."""
    dist = [inf] * n
    dist[start] = 0 
    for i in range(n-1): 
        for u, v, w in edges: 
            if dist[u] + w < dist[v]: dist[v] = dist[u] + w
    return dist 


def floyd_warshall(n, edges: List[List[int]]): 
    """Floyd-Warshall algo
    Return the short distances of every pair of nodes."""
    dist = [[inf]*n for _ in range(n)] # adjacency matrix 
    for u in range(n): dist[u][u] = 0 
    for u, v, w in edges: dist[u][v] = w 
    for k in range(n): 
        for u in range(n): 
            for v in range(n): 
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    return dist


def kruskal(n, edges: List[List[int]]):
    """Kruskal's algo
    Return the minimum spanning tree."""
    parent = list(range(n))

    def find(p): 
        if p != parent[p]: parent[p] = find(parent[p])
        return parent[p]

    pq = [(w, u, v) for u, v, w in edges]
    heapify(pq)
    ans = []
    while pq: 
        w, u, v = heappop(pq)
        uu, vv = find(u), find(v)
        if uu != vv: 
        ans.append((u, v))
        parent[uu] = parent[vv]
    return ans 


def prim():
    """Prim's algo
    Return the minimum spanning tree."""
    pass 


"""
Konig's Theorem
The maximum mathcing for a bipartite graph equals its minimum vertex cover.
"""
