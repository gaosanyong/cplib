"""
NAME - prime 

DESCRIPTION
    This module implements below algorithms:    
    * sieve of eratosthenes
    * linear sieve
    * primality tests
        o trial division
        o Fermat primality test
        o Miller-Rabin primality test 
            + deterministic version
    * integer factorization
        o trial division
          + wheel factorization
          + precomputed primes 
        o Fermat's factorizatoin method
        o Pollard's p-1 method
        o Pollard's rho algorithm
          + Brent's algorithm

FUNCTIONS
    sieve(n)
        Compute sieve of Eratosthenes.

    linear_sieve(n)
        Compute liear sieve to calculate smallest prime factors.

    is_prime(x)
        Check if x is a prime number via trial division.

    fermat(x)
        Check if x is a prime number via Fermat primality test.

    miller_rabin(x)
        Check if x is a prime number via Miller-Rabin test. 
    
    miller_rabin_d(x)
        Check if x is a prime number via deterministic Miller-Rabin test.

    factor(n)


    wheel(n)

    precomp(n)

    fermat(n)

    pminus1(n)

    rho(n)

    brent(n)
"""


from math import ceil, gcd, sqrt
from prime import sieve
from random import randint
from typing import List

"""
SIEVE OF ERATOTHENES 
Sieve of Eratosthenes is an algorithm for finding all the prime numbers up to n 
using O(Nlog(log(N))) operations.
"""

def sieve(n: int) -> List[int]:
    """Compute sieve of Eratosthenes O(N*log(log(N)))"""
    prime = [True] * (n+1)
    prime[0] = prime[1] = False # 0 and 1 are not prime
    for i in range(int(sqrt(n+1))+1): # "sieving till root" optimization
        if prime[i]:
            for ii in range(i*i, n+1, i): 
                prime[ii] = False 
    return prime


"""
LINEAR SIEVE
Linear sieve is an algorithm for calculating smallest prime factors up to n 
using O(N) operations. 
"""

def linear_sieve(n: int) -> List[int]: 
    """Compute linear sieve to calculate smallest prime factors in O(N)."""
    spf = list(range(n+1)) # smallest prime factor
    prime = []
    for i in range(2, n+1): 
        if spf[i] == i: prime.append(i)
        for x in prime: 
            if x <= spf[i] and i*x <= n: spf[i*x] = x
            else: break 
    return spf

    """
    # alternative O(N*log(log(N))) spf routine 
    spf = list(range(n+1))
    for i in range(4, n+1, 2): spf[i] = 2
    for i in range(3, int(sqrt(n+1))+1): 
        if spf[i] == i: 
            for ii in range(i*i, n+1, i): 
                spf[ii] = min(spf[ii], i)
    """

"""
PRIMALITY TEST

1) trial division
2) Fermat primality test 
3) Miller-Rabin primality test 
"""

def is_prime(n: int) -> bool: 
    """Check if n is a prime number via trial division."""
    if n <= 1: return False 
    if n == 2: return True 
    if n % 2 == 0: return False 
    for d in range(3, int(sqrt(n))+1, 2): 
        if n % d == 0: return False
    return True 


def fermat(n: int, repeat: int = 5) -> bool: 
    """Check if n is a prime number via Fermat primality test.

    Fermat's little theorem states that for a prime number p and a coprime 
    integer a the following equation holds: a^(p−1) ≡ 1 mod p. 

    In general this theorem doesn't hold for composite numbers. This can be 
    used to create a primality test. We pick an integer 2 ≤ a ≤ p−2, and check 
    if the equation holds or not. If it doesn't hold, e.g. a^(p−1) !≡ 1 mod p, 
    we know that p cannot be a prime number. In this case we call the base a 
    "Fermat witness" for the compositeness of p. 

    However it is also possible, that the equation holds for a composite number. 
    So if the equation holds, we don't have a proof for primality. We only can 
    say that p is probably prime. If it turns out that the number is actually 
    composite, we call the base a a "Fermat liar".
    
    By running the test for all possible bases a, we can actually prove that a 
    number is prime. However this is not done in practice, since this is a lot 
    more effort than just doing trial division. Instead the test will be 
    repeated multiple times with random choices for a. If we find no witness 
    for the compositeness, it is very likely that the number is in fact prime.
    
    There is one bad news though: there exist some composite numbers where 
    a^(n−1) ≡ 1 mod n holds for all a coprime to n, for instance for the number 
    561 = 3⋅11⋅17. Such numbers are called Carmichael numbers. The Fermat 
    primality test can identify these numbers only, if we have immense luck and 
    choose a base a with gcd(a,n) ≠ 1. The Fermat test is still used in 
    practice, as it is very fast and Carmichael numbers are very rare. E.g. 
    there only exist 646 such numbers below 10^9.
    """
    if n < 4: return n in (2, 3)
    for _ in range(repeat): 
        a = 2 + randint(0, n-4)
        if pow(a, n-1, n) != 1: return False 
    return True 


def miller_rabin(n: int, repeat: int = 5) -> bool:
    """Check if n is a prime number via Miller-Rabin primality test.

    For an odd number n, n−1 is even and we can factor out all powers of 2. We 
    can write: n−1 = 2^s⋅d, with d odd. This allows us to factorize the 
    equation of Fermat's little theorem:

    a^(n−1) ≡ 1 mod n ⟺ a^(2^s⋅d−1) ≡ 0 mod n
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−1)⋅d)−1) ≡ 0 mod n
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−2)⋅d)+1)(a^(2^(s−2)⋅d)−1) ≡ 0 mod n
                      ⋮
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−2)⋅d)+1)⋯(a^d+1)(a^d−1) ≡ 0 mod n

    If n is prime, then n has to divide one of these factors. And in the Miller-
    Rabin primality test we check exactly that statement, which is a more 
    stricter version of the statement of the Fermat test. For a base 2 ≤ a ≤ n−2
    we check if either 
    1) a^d ≡ 1 mod n holds or
    2) a^(2^r⋅d) ≡ −1 mod n holds for some 0 ≤ r ≤ s−1.

    If we found a base a which doesn't satisfy any of the above equalities, than 
    we found a witness for the compositeness of n. In this case we have proven 
    that n is not a prime number. Similar to the Fermat test, it is also possible 
    that the set of equations is satisfied for a composite number. In that case 
    the base a is called a "strong liar". If a base a satisfies the equations (one 
    of them), n is only strong probable prime. However, there are no numbers like 
    the Carmichael numbers, where all non-trivial bases lie. In fact it is 
    possible to show, that at most 14 of the bases can be strong liars. If n is 
    composite, we have a probability of ≥75% that a random base will tell us that 
    it is composite. By doing multiple iterations, choosing different random bases, 
    we can tell with very high probability if the number is truly prime or if it 
    is composite.
    """
    if n < 4: return n in (2, 3)
    if n <= 1 or n&1 == 0: return False
    s, d = 0, n-1
    while d&1 == 0:
        s += 1
        d >>= 1
    # if ∀ j ∈ [0, s-1],  a^d !≡ 1 (mod n) and a^((2^j)*d) !≡ -1 (mod n), 
    # then n is not prime and a is called a "strong witness" to compositeness for n.
    # if ∃ j ∈ [0, s-1], a^d ≡ 1 (mod n) or a^((2^j)*d) ≡ -1 (mod n), 
    # then n is said to be a "strong pseudo-prime" to the base a, and a is called a "strong liar" to primality for n.
    for _ in range(repeat):
        a = randint(2, n-2) # pick a ∈ [2, n-2]
        v = pow(a, d, n) 
        if v != 1 and v != n-1:
            for j in range(1, s): 
                v = pow(v, 2, n)
                if v == n-1: break 
            if v != n-1: return False 
    return True


def miller_rabin_d(n: int) -> bool: 
    """Check if n is a prime number via deterministic Miller-Rabin test.

    Miller showed that it is possible to make the algorithm deterministic by 
    only checking all bases ≤ O(lg(n)^2). Bach later gave a concrete bound, it 
    is only necessary to test all bases a ≤ 2lg(n)^2. It turns out, for testing 
    a 32 bit integer it is only necessary to check the first 4 prime bases: 
    2, 3, 5 and 7. The smallest composite number that fails this test is 
    3,215,031,751=151⋅751⋅28351. And for testing 64 bit integer it is enough to 
    check the first 12 prime bases: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 
    37."""

    if n < 2: return False 
    s, d = 0, n-1
    while d&1 == 0:
        s += 1
        d >>= 1
    for a in 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37:
        if n == a: return True
        v = pow(a, d, n) 
        if v != 1 and v != n-1:
            for j in range(1, s): 
                v = pow(v, 2, n)
                if v == n-1: break 
            if v != n-1: return False 
    return True


"""
INTEGER FACTORIZATION 
1) trial division 
2) Fermat's factorization method 
3) Pollard's p-1 method
4) Pollard's rho method
"""

"""
TRIAL DIVISION
We divide by each possible divisor d. We notice that it is impossible for 
prime factor of a composite number n to be bigger than √n. Therefore, we 
only need to test the divisors 2 ≤ d ≤ √n, which gives us the prime 
factorization in O(√n).
"""

def factor(n: int) -> List[int]:
    """Return all prime factors of n via trial division."""
    ans = []
    d = 2
    while d*d <= n: 
        while n % d == 0: 
            ans.append(d)
            n //= d
        d += 1
    if n > 1: ans.append(n)
    return ans 

"""
WHEEL FACTORIZATION
Once we know that the number is not divisible by 2, we don't need to check 
every other even number. This leaves us with only 50% of the numbers to check. 
After checking 2, we can simply start with 3 and skip every other number.
"""

def wheel(n: int) -> List[int]: 
    """Wheel factorization"""
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


"""
PRECOMPUTED PRIMES
Extending the wheel factorization with more and more primes will leave exactly 
the primes to check. So a good way of checking is just to precompute all prime 
numbers with the Sieve of Eratosthenes until √n and test them individually.
"""

def precomp(n: int) -> List[int]: 
    """Precompute primes up to sqrt(n) and use them to factorize n."""
    ans = []
    primes = [i for i, x in enumerate(sieve(int(sqrt(n))+1)) if i >= 2 and x]
    for p in : 
        while n % p == 0: 
            ans.append(p)
            n //= p
    if n > 1: ans.append(n)
    return ans 


"""
FERMAT'S FACTORIZATION METHOD
We can write an odd composite number n = p⋅q as the difference of two squares 
n == a^2 − b^2:

                    n == ((p+q)/2)^2 − ((p−q)/2)^2

Fermat's factorization method tries to exploit the fact, by guessing the first 
square a^2, and check if the remaining part b^2 == a^2 − n is also a square 
number. If it is, then we have found the factors a−b and a+b of n.

The algorithm runs in O(|p−q|) time. 
1) This factorization method can be very fast, if the difference between the 
   two factors p and q is small. 
2) Once the factors are far apart, it is very slow. 
Thus, it is rarely used in practice.
"""

def fermat(n: int) -> int: 
    """Return """
    a = ceil(sqrt(n))
    while True: 
        bb = a*a - n 
        b = round(sqrt(bb))
        if b * b == bb: break 
        a += 1
    return a - b


"""
POLLARD'S P-1 METHOD

It is very likely that at least one factor of a number is B-powersmooth for 
small B. B-powersmooth means, that every power d^k of a prime d that divides 
p−1 is at most B. Let a factorization of n be n = p⋅q. If a is coprime to p, 
Fermat's little thoerem states that 

                            a^(p−1) ≡ 1 (mod p). 

This also means that 

                    a^(p−1)^k ≡ a^(k⋅(p−1)) ≡ 1 (mod p).

So for any M with p−1 | M we know that a^M ≡ 1 (mod p). This means that 
a^M − 1 = p⋅r, and because of that also p | gcd(a^M − 1, n). Therefore, if p−1 
for a factor p of n divides M, we can extract a factor using Euclid's algorithm.
It is clear, that the smallest M that is a multiple of every B-powersmooth 
number is lcm(1, 2 ,3 ,4 , …, B). Or alternatively M = ∏(prime q≤B) q^⌊log_q(B)⌋
Notice, if p−1 divides M for all prime factors p of n, then gcd(aM−1,n) will 
just be n. In this case we don't receive a factor. Therefore we will try to 
perform the gcd multiple time, while we compute M.

Unfortunately, some composite numbers don't have B-powersmooth factors for 
small B. 
"""

def pminus1(n: int) -> int:
    """Return """
    B = 10
    g = 1
    primes = [i for i, x in enumerate(sieve(1000000)) if i >= 2 and x]
    while B <= 1000000 and g < n: 
        a = randint(2, n-2)
        g = gcd(a, n)
        if g > 1: return g
        for p in primes: 
            if p < B: 
                p_power = 1
                while p_power * p <= B: p_power *= p 
                a = pow(a, p_power, n)
                g = gcd(a-1, n)
                if 1 < g < n: return g 
        B *= 2
    return 1 


"""
POLLARD'S RHO METHOD

Let the prime factorization from a number be n == p⋅q. The algorithm look at a 
pseudo-random sequence {x, f(x), f(f(x)), …} where f is a polynomial function, 
usually f(x) = (x^2+1) mod n. Since all the values are in the range [0, p) this 
sequence will begin to cycle sooner or later. The "birthday paradox" actually 
suggests, that the expected number of elements is O(√p) until the repetition 
starts. If p is smaller than √n, the repetition will start very likely in O(√√n).

There is a cycle in the sequence iff there are two indices s, t with 
xs ≡ xt mod p. This equation can be rewritten as xs−xt ≡ 0 mod p which is the 
same as p | gcd(xs−xt, n). Therefore, if we find two indices s and t with 
g = gcd(xs−xt, n) > 1, we have found a cycle and also a factor g of n. 
"""
def rho(n: int, start: int = 1, c: int = 1) -> int: 
    """Floyd's algorithm (tortoise & hare algorithm)
    This algorithm finds a cycle by using two pointer. These pointers move over 
    the sequence at different speeds. In each iteration the first pointer 
    advances to the next element, but the second pointer advances two elements. 
    It's not hard to see, that if there exists a cycle, the second pointer will 
    make at least one full cycle and then meet the first pointer during the 
    next few cycle loops. If the cycle length is λ and the μ is the first index 
    at which the cycle starts, then the algorithm will run in O(λ+μ) time."""
    fn = lambda x: (x*x + c) % n
    x = y = start
    g = 1
    while g == 1: 
        x = fn(x)
        y = fn(fn(y))
        g = gcd(abs(x - y), n)
    return g 


def brent(n: int, start: int = 1, c: int = 1) -> int:
    """Brent's algorithm uses two pointer, which are advanced in powers of two. 
    As soon as 2^i is greater than λ and μ, we will find the cycle. Brent's 
    algorithm runs in linear time, but is usually faster than Floyd's algorithm, 
    since it uses less evaluations of the function.
    """
    fn = lambda x: (x*x + c) % n
    x = start
    g = q = l = 1
    m = 128 
    while g == 1: 
        y = x
        for _ in range(1, l): x = fn(x)
        for k in range(0, l, m): 
            if g != 1: break 
            xx = x
            for i in range(m, l-k): 
                x = fn(x)
                q = q * abs(y-x) % n
            g = gcd(q, n)
        l *= 2
    if g == n: 
        while True: 
            xx = fn(xx)
            g = gcd(abs(xx-y), n)
            if g != 1: break 
    return g