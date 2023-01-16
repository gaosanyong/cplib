"""
NAME 
    fenwick - Fenwick tree data structure 

DESCRIPTION
    This module implements Fenwick tree for prefix sum and prefix max.

    * Fenwick     Fenwick tree for prefix sum query
    * Fenwick2D   Fenwick tree for 2-dim prefix sum query
    * FenwickMax  Fenwick tree for prefix max query

CLASSES 
    class Fenwick(n)
     |  Return a Fenwick tree for prefix sum 
     |
     |  Methods defined here: 
     |
     |  add(k, delta) 
     |      add delta to the kth element 
     | 
     |  query(k)
     |      compure prefix sum of first k elements

    class Fenwick2D(m, n)
     |  Return a Fenwick tree for 2-dim prefix sum 
     |
     |  Methods defined here: 
     |
     |  add(i, j, delta) 
     |      add delta to the data at ith row and jth column 
     | 
     |  query(i, j)
     |      compure prefix sum of first i rows and j columns

    class FenwickMax(n)
     |  Return a Fenwick tree for prefix max
     |
     |  Methods defined here: 
     |
     |  update(k, x)
     |      update kth element to x
     |
     |  query(k)
     |      compute prefix max of first k elements
"""

class Fenwick: 
    """Fenwick tree for prefix sum query"""

    def __init__(self, n: int):
        """Initialize a Fenwick tree."""
        self.nums = [0]*(n+1)

    def add(self, k: int, delta: int) -> None: 
        """Update tree upon adding delta to kth element."""
        k += 1
        while k < len(self.nums): 
            self.nums[k] += delta
            k += k & -k 

    def query(self, k: int) -> int: 
        """Return the prefix sum up to kth index (inclusive)."""
        ans = 0
        k += 1
        while k:
            ans += self.nums[k]
            k -= k & -k 
        return ans


class Fenwick2D: 
    """Fenwick tree for 2-dim prefix sum query"""
    
    def __init__(self, m: int, n: int): 
        """Initialize a 2-dim Fenwick tree."""
        self.m = m 
        self.n = n 
        self.nums = [[0]*(n+1) for _ in range(m+1)]
            
    def add(self, i: int, j: int, delta: int) -> None: 
        """Update tree upon adding delta to ith row and jth column."""
        i += 1
        jj = j+1
        while i <= self.m: 
            j = jj
            while j <= self.n: 
                self.nums[i][j] += delta 
                j += j & -j
            i += i & -i 
        
    def query(self, i: int, j: int) -> int: 
        """Return 2d prefix sum upto ith row and jth column (inclusive)."""
        ans = 0 
        i += 1
        jj = j+1
        while i: 
            j = jj 
            while j: 
                ans += self.nums[i][j]
                j -= j & -j
            i -= i & -i 
        return ans 


class FenwickMax: 
    """Fenwick tree for prefix max query. 
    Caveat: 
    In order for Fenwick tree to work for max query, the updated value has to 
    larger than the original value."""
    def __init__(self, n: int): 
        self.nums = [0]*(n+1)
            
    def update(self, k: int, x: int) -> None: 
        """Update kth element with value x."""
        k += 1
        while k < len(self.data): 
            self.nums[k] = max(self.nums[k], x)
            k += k & -k

    def query(self, k: int) -> int: 
        """Return prefix max up to kth index (inclusive)."""
        k += 1
        ans = 0 
        while k:
            ans = max(ans, self.nums[k])
            k -= k & -k
        return ans 