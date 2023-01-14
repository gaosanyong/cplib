"""
NAME
    union_find - union-find data structure 

DESCRIPTION 
    This module implements union-find data structure including 
        1) find with path compression 
        2) union with rank. 

    * UnionFind      union-find via array implementation
    * UnionFindDict  union-find via dictionary implementation

CLASSES
    class UnionFind(n)
     |  Return a union-find data structure 
     |  
     |  Methods defined here: 
     | 
     |  find(p)
     |      find the parent of p
     | 
     |  union(p, q) 
     |      connect p and q into one component 

    class UnionFindDict()
     |  Return a union-find data structure 
     |  
     |  Methods defined here: 
     | 
     |  find(p) 
     |      find the parent of p 
     | 
     |  union(p, q)  
     |      connect p and q into one component
"""

class UnionFind:
    """Union-Find via array implementation"""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p: int) -> int:
        """Find with path compression"""
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        """Union with rank"""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt 
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class UnionFindDict:
    """Union-Find via dictionary implementation"""

    def __init__(self): 
        self.parent = {}
        self.rank = defaultdict(lambda: 1)
    
    def find(self, p):
        """Find with path compression"""
        if p not in self.parent: self.parent[p] = p
        elif p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        """Union with rank"""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt 
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 