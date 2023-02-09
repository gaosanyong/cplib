
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


def factor(n: int) -> List[int]:
    """Trial division
    Return all prime factors."""
    ans = []
    d = 2
    while d*d <= n: 
        while n % d == 0: 
            ans.append(d)
            n //= d
        d += 1
    if n > 1: ans.append(n)
    return ans 


def factor_wheel(n: int) -> List[int]: 
    """Wheel factorization
    Return all prime factors."""
    ans = []
    while n % 2 == 0: 
        ans.append(2)
        n //= 2
    d = 3
    while d*d <= n: 
        while n % d == 0: 
            ans.append(d)
            n //= d
        d += 2
    if n > 1: ans.append(n)
    return ans 


def gcd_ext(x: int, y: int) -> List[int]: 
    """Extended Euclidean algo
    Return the greatest common divisor and coefficients such that 
    a * x + b * y == gcd(x, y)."""
    a = bb = 1
    b = aa = 0
    while y: 
        q = int(x / y) 
        a, aa = aa, a - q*aa 
        b, bb = bb, b - q*bb 
        x, y = y, x - q*y 
    return x, a, b


def gcd(x: int, y: int) -> int:
    """Euclidean algo
    Return the greatest common divisor."""
    while y: x, y = y, x%y
    return abs(x)


def is_prime(n: int) -> bool: 
    """Check primality via trial division."""
    if n <= 1: return False 
    for p in range(2, isqrt(n)+1): 
        if n % p == 0: return False
    return True 


def lcm(x: int, y: int) -> int:
    """Return the least common multiple."""
    if x == 0 or y == 0: return 0
    return abs(x*y)//gcd(x, y)


def pow(x: int, p: int, m: int) -> int: 
    """Binary exponentiation
    Return power mod m."""
    ans = 1
    while p:
        if p & 1: ans = ans * x % m
        x = x * x % m
        p >>= 1
    return ans 


def fact_mod(n, m=1_000_000_007): 
    """Return factorial and inverse factorial modulo."""
    inv = [1]*n
    fact = [1]*n
    ifact = [1]*n
    for x in range(1, n): 
        if x >= 2: inv[x] = mod - mod//x * inv[mod % x] % mod
        fact[x] = fact[x-1] * x % mod 
        ifact[x] = ifact[x-1] * inv[x] % mod 


def sieve(n: int) -> List[int]:
    """Sieve of Eratosthenes
    Return  O(N*log(log(N)))"""
    prime = [True] * (n+1)
    prime[0] = prime[1] = False 
    for i in range(int(sqrt(n+1))+1): # "sieving till root" optimization
        if prime[i]:
            for ii in range(i*i, n+1, i): 
                prime[ii] = False 
    return prime


def sieve_lin(n: int) -> List[int]: 
    """Linear sieve 
    Return the smallest prime factors in O(N)."""
    spf = list(range(n+1))
    prime = []
    for i in range(2, n+1): 
        if spf[i] == i: prime.append(i)
        for x in prime: 
            if x <= spf[i] and i*x <= n: spf[i*x] = x
            else: break 
    return spf