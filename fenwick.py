"""
NAME 
    fenwick - Fenwick tree data structure 

DESCRIPTION
    This module implements Fenwick tree for prefix sum and prefix max.

    * Fenwick    - Fenwick tree for prefix sum 
    * FenwickMax - Fenwick tree for prefix max 

CLASSES 
    class Fenwick(n)
     |  Return a Fenwick tree for prefix sum 
     |
     |  Methods defined here: 
     |
     |  update(k, x) 
     |      add x to the kth element 
     | 
     |  query(k)
     |      compure prefix sum of first k elements

    class FenwickMax(n)
     |  Return a Fenwick tree for prefix max
     |
     |  Methods defined here: 
     |
     |  update(k, x)
     |      update kth element with x
     |
     |  query(k)
     |      compute prefix max of first k elements
"""

class Fenwick: 
    """Fenwick tree for prefix sum query"""

    def __init__(self, n: int):
        self.nums = [0]*(n+1)

    def update(self, k: int, x: int) -> None: 
        """Add kth element with value x."""
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 

    def query(self, k: int) -> int: 
        """Return prefix sum of nums[:k+1]."""
        k += 1
        ans = 0
        while k:
            ans += self.nums[k]
            k -= k & -k
        return ans


class FenwickMax: 
    """Fenwick tree for prefix max query"""
    def __init__(self, n: int): 
        self.data = [0]*(n+1)
            
    def update(self, k: int, x: int) -> None: 
        """Update kth element with value x."""
        k += 1
        while k < len(self.data): 
            self.data[k] = max(self.data[k], x)
            k += k & -k

    def query(self, k: int) -> int: 
        """Return prefix max of nums[:k+1]."""
        k += 1
        ans = 0 
        while k:
            ans = max(ans, self.data[k])
            k -= k & -k
        return ans 