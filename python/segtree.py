"""
NAME
    seg_tree - segment tree data structure
    * assignment update vs increment update 

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
        self.n = n = len(arr)
        self.tree = [0]*(4*n)
        self._build(arr, 0, 0, n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Build segment tree from array."""
        if lo+1 == hi: self.tree[k] = arr[lo]
        else: 
            mid = lo + hi >> 1
            self._build(arr, 2*k+1, lo, mid)
            self._build(arr, 2*k+2, mid, hi)
            self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def update(self, i: int, delta: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when array value at i is incresed by delta."""
        if not hi: hi = self.n
        if lo+1 == hi: self.tree[k] += delta # leaf node
        else: 
            mid = lo + hi >> 1
            if i < mid: self.update(i, delta, 2*k+1, lo, mid) 
            else: self.update(i, delta, 2*k+2, mid, hi)
            self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if qhi <= lo or  hi <= qlo: return inf          #      no overlap 
        if qlo <= lo and hi <= qhi: return self.tree[k] #   total overlap 
        mid = lo + hi >> 1                              # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


class LazySegTreeMin:
    
    def __init__(self, arr: List[int]): 
        """Build the segmentation tree."""
        self.n = n = len(arr)
        self.lazy = [0]*(4*n)
        self.tree = [0]*(4*n)
        self._build(arr, 0, 0, n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Build segment tree from array."""
        if lo+1 == hi: self.tree[k] = arr[lo]
        else: 
            mid = lo + hi >> 1
            self._build(arr, 2*k+1, lo, mid)
            self._build(arr, 2*k+2, mid, hi)
            self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2]) 

    def update(self, qlo: int, qhi: int, delta: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when value in [qlo, qhi) is incresed by delta."""
        if not hi: hi = self.n
        if self.lazy[k]: 
            self.tree[k] += self.lazy[k]
            if lo+1 < hi: # non-leaf 
                self.lazy[2*k+1] += self.lazy[k] # mark children for lazy propagation
                self.lazy[2*k+2] += self.lazy[k] # mark children for lazy propagation
            self.lazy[k] = 0
        if lo < hi and qlo < hi and lo < qhi: 
            if qlo <= lo and hi <= qhi: # total overlap
                self.tree[k] += delta
                if lo+1 < hi: 
                    self.lazy[2*k+1] += delta 
                    self.lazy[2*k+2] += delta 
            else: 
                mid = lo + hi >> 1
                self.update(qlo, qhi, delta, 2*k+1, lo, mid) 
                self.update(qlo, qhi, delta, 2*k+2, mid, hi)
                self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if self.lazy[k]: 
            self.tree[k] += self.lazy[k]
            if lo+1 < hi: 
                self.lazy[2*k+1] += self.lazy[k]
                self.lazy[2*k+2] += self.lazy[k]
            self.lazy[k] = 0 
        if qhi <= lo or  hi <= qlo: return inf          #      no overlap 
        if qlo <= lo and hi <= qhi: return self.tree[k] #   total overlap 
        mid = lo + hi >> 1                              # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


class LazySegTreeSum:

    def __init__(self, arr: List[int]):
        """Build the segmentation tree."""
        self.n = n = len(arr)
        self.tree = [0]*(4*n)
        self.lazy = [0]*(4*n)
        self._build(arr, 0, 0, n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None:
        """Build segment tree from array."""
        if lo+1 == hi: self.tree[k] = arr[lo]
        else:
            mid = lo + hi >> 1
            self._build(arr, 2*k+1, lo, mid)
            self._build(arr, 2*k+2, mid, hi)
            self.tree[k] = self.tree[2*k+1] + self.tree[2*k+2]

    def update(self, qlo: int, qhi: int, delta: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when value in [qlo, qhi) is incresed by delta."""
        if not hi: hi = self.n
        if self.lazy[k]:
            self.tree[k] += (hi-lo)*self.lazy[k]
            if lo+1 < hi: # non-leaf
                self.lazy[2*k+1] += self.lazy[k] # mark children for lazy propagation
                self.lazy[2*k+2] += self.lazy[k] # mark children for lazy propagation
            self.lazy[k] = 0
        if lo < hi and qlo < hi and lo < qhi:
            if qlo <= lo and hi <= qhi: # total overlap
                self.tree[k] += (hi-lo)*delta
                if lo+1 < hi:
                    self.lazy[2*k+1] += delta
                    self.lazy[2*k+2] += delta
            else:
                mid = lo + hi >> 1
                self.update(qlo, qhi, delta, 2*k+1, lo, mid)
                self.update(qlo, qhi, delta, 2*k+2, mid, hi)
                self.tree[k] = self.tree[2*k+1] + self.tree[2*k+2]

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int:
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if self.lazy[k]:
            self.tree[k] += (hi-lo)*self.lazy[k]
            if lo+1 < hi:
                self.lazy[2*k+1] += self.lazy[k]
                self.lazy[2*k+2] += self.lazy[k]
            self.lazy[k] = 0
        if qhi <= lo or  hi <= qlo: return 0            #      no overlap
        if qlo <= lo and hi <= qhi: return self.tree[k] #   total overlap
        mid = lo + hi >> 1                              # partial overlap
        return self.query(qlo, qhi, 2*k+1, lo, mid) + self.query(qlo, qhi, 2*k+2, mid, hi)


class SegTreeIter: 
    """Iterative implementation of segment tree
    Reference: https://codeforces.com/blog/entry/18051
    """

    def __init__(self, arr: List[int]): 
        """Initialie the segment tree."""
        self.n = len(arr)
        self.tree = [0] * (2*self.n)
        for i in range(2*self.n-1, 0, -1): 
            if i >= self.n: self.tree[i] = arr[i - self.n]
            else: self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

    def query(self, lo: int, hi: int) -> int: 
        """Range query sum from lo (inclusive) and hi (exclusive)
        (Alternatively, one could range query max or min from lo to hi)."""
        ans = 0 
        lo += self.n 
        hi += self.n
        while lo < hi: 
            if lo & 1: 
                ans += self.tree[lo]
                lo += 1
            if hi & 1: 
                hi -= 1
                ans += self.tree[hi]
            lo >>= 1
            hi >>= 1
        return ans 

    def update(self, i: int, delta: int) -> None: 
        """Point increment update the value at i by delta
        (Alternativley, one could point assignment update the value at it to val)."""
        i += self.n 
        self.tree[i] += delta # increment update
        while i > 1: 
            self.tree[i>>1] = self.tree[i] + self.tree[i^1]
            i >>= 1


class LazySegTreeIter:

    def __init__(self, arr: List[int]): 
        self.n = n = len(arr)
        self.ht = n.bit_length()
        self.tree = [0] * (2*n)
        self.lazy = [0] * n

    def _apply(self, p: int, val: int) -> None: 
        self.tree[p] += val 
        if p < self.n: self.lazy[p] += val

    def _build(self, p: int) -> None: 
        while p > 1: 
            p >>= 1
            self.tree[p] = max(self.tree[p<<1], self.tree[p<<1|1]) + self.lazy[p]

    def _push(self, p: int) -> None: 
        for s in range(self.ht, 0, -1): 
            i = p >> s
            if self.lazy[i]: 
                self._apply(i<<1, self.lazy[i])
                self._apply(i<<1|1, self.lazy[i])
                self.lazy[i] = 0

    def query(self, lo: int, hi: int) -> int: 
        """Range query max from lo (inclusive) and hi (exclusive)
        (Alternatively, one could range query max or min from lo to hi)."""
        ans = -inf 
        lo += self.n 
        hi += self.n
        self._push(lo)
        self._push(hi-1)
        while lo < hi: 
            if lo & 1: 
                ans = max(ans, self.tree[lo])
                lo += 1
            if hi & 1: 
                hi -= 1
                ans = max(ans, self.tree[hi])
            lo >>= 1
            hi >>= 1
        return ans 

    def update(self, lo: int, hi: int, val: int) -> None: 
        lo += self.n
        hi += self.n
        ll = lo 
        hh = hi 
        while lo < hi: 
            if lo & 1: 
                lo += 1
                self._apply(lo, val) 
            if hi & 1: 
                hi -= 1
                self._apply(hi, val) 
        self._build(ll)
        self._build(hh - 1)
