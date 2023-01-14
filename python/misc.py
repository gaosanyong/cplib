
def catalan(n: int) -> int: 
    """Return nth Catalan number."""
    ans = 1
    for i in range(n): 
        ans *= 2*n - i
        ans //= i+1
    return ans//(n+1)


def choose(n: int, k: int) -> int:
    """Return binomial coefficient of n choose k."""
    ans = 1
    for i in range(min(k, n-k)):
        ans *= n-i
        ans //= i+1
    return ans 