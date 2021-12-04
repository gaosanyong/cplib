"""
NAME
    seg_tree - segment tree data structure

DESCRIPTION
    This module implements segment tree data structure. 

    * SegTree      segment tree
    * SegTreeLazy  segment tree with lazy propagation

CLASSES
    SegTree(arr)
     |  Return a segment tree.
     |  
     |  Methods defined here: 
     |
     |      update(idx, val, k, lo, hi)
     |
     |      query(qlo, qhi, k, lo, hi)
     |      

    SegTreeLazy(arr)
     |  Return a segment tree with lazy propagation
     | 
     |  Methods defined here: 
     |
     |      update(idx, val, k, lo, hi)
     |
     |      query(qlo, qhi, k, lo, hi)
"""

class SegTree: 

    def __init__(self, arr: List[int]): 
        """Build the setmentation tree."""
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self._build(arr, 0, 0, self.n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Build segment tree from array."""
        if lo+1 == hi: 
            self.tree[k] = arr[lo]
            return 
        mid = lo + hi >> 1
        self._build(arr, 2*k+1, lo, mid)
        self._build(arr, 2*k+2, mid, hi)
        self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def update(self, idx: int, val: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when an array value is changed."""
        if not hi: hi = self.n
        if lo+1 == hi: 
            self.tree[k] = val 
            return 
        mid = lo + hi >> 1
        if idx < mid: self.update(idx, val, 2*k+1, lo, mid) 
        else: self.update(idx, val, 2*k+2, mid, hi)
        self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if qlo <= lo and hi <= qhi: return self.tree[k] # total overlap 
        if qhi <= lo or  hi <= qlo: return inf # no overlap 
        mid = lo + hi >> 1 # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


class SegTreeLazy: 
    pass 