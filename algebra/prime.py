"""
NAME 
    prime - miscellaneous cp algorithms

DESCRIPTION
    This module implements a few cp algorithms. 
    
    * sieve of eratosthenes
    * linear sieve
    * primality tests
    * integer factorization

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
"""

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

def is_prime(x: int) -> bool: 
    """Check if x is a prime number via trial division."""
    if x <= 1: return False 
    if x == 2: return True 
    if x % 2 == 0: return False 
    for d in range(3, int(sqrt(x))+1, 2): 
        if x % d == 0: return False
    return True 


def fermat(x: int, repeat: int = 5) -> bool: 
    """Check if x is a prime number via Fermat primality test.

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


def miller_rabin(x: int, repeat: int = 5) -> bool:
    """Check if x is a prime number via Miller-Rabin primality test.

    For an odd number x, x−1 is even and we can factor out all powers of 2. We 
    can write: x−1 = 2^s⋅d, with d odd. This allows us to factorize the 
    equation of Fermat's little theorem:

    a^(x−1) ≡ 1 mod x ⟺ a^(2^s⋅d−1) ≡ 0 mod x
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−1)⋅d)−1) ≡ 0 mod x
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−2)⋅d)+1)(a^(2^(s−2)⋅d)−1) ≡ 0 mod x
                      ⋮
                      ⟺(a^(2^(s−1)⋅d)+1)(a^(2^(s−2)⋅d)+1)⋯(a^d+1)(a^d−1) ≡ 0 mod x

    If x is prime, then x has to divide one of these factors. And in the Miller-
    Rabin primality test we check exactly that statement, which is a more 
    stricter version of the statement of the Fermat test. For a base 2 ≤ a ≤ x−2
    we check if either 
    1) a^d ≡ 1 mod x holds or
    2) a^(2^r⋅d) ≡ −1 mod x holds for some 0 ≤ r ≤ s−1.

    If we found a base a which doesn't satisfy any of the above equalities, than 
    we found a witness for the compositeness of x. In this case we have proven 
    that x is not a prime number. Similar to the Fermat test, it is also possible 
    that the set of equations is satisfied for a composite number. In that case 
    the base a is called a "strong liar". If a base a satisfies the equations (one 
    of them), x is only strong probable prime. However, there are no numbers like 
    the Carmichael numbers, where all non-trivial bases lie. In fact it is 
    possible to show, that at most 14 of the bases can be strong liars. If x is 
    composite, we have a probability of ≥75% that a random base will tell us that 
    it is composite. By doing multiple iterations, choosing different random bases, 
    we can tell with very high probability if the number is truly prime or if it 
    is composite.
    """
    if x < 4: return x in (2, 3)
    if x <= 1 or x&1 == 0: return False
    s, d = 0, x-1
    while d&1 == 0:
        s += 1
        d >>= 1
    # if ∀ j ∈ [0, s-1],  a^d !≡ 1 (mod x) and a^((2^j)*d) !≡ -1 (mod x), 
    # then x is not prime and a is called a "strong witness" to compositeness for x.
    # if ∃ j ∈ [0, s-1], a^d ≡ 1 (mod x) or a^((2^j)*d) ≡ -1 (mod x), 
    # then x is said to be a "strong pseudo-prime" to the base a, and a is called a "strong liar" to primality for x.
    for _ in range(repeat):
        a = randint(2, x-2) # pick a ∈ [2, x-2]
        v = pow(a, d, x) 
        if v != 1 and v != x-1:
            for j in range(1, s): 
                v = pow(v, 2, x)
                if v == x-1: break 
            if v != x-1: return False 
    return True


def miller_rabin_d(x: int) -> bool: 
    """Check if x is a prime number via deterministic Miller-Rabin test.

    Miller showed that it is possible to make the algorithm deterministic by 
    only checking all bases ≤ O(lg(n)^2). Bach later gave a concrete bound, it 
    is only necessary to test all bases a ≤ 2lg(n)^2. It turns out, for testing 
    a 32 bit integer it is only necessary to check the first 4 prime bases: 
    2, 3, 5 and 7. The smallest composite number that fails this test is 
    3,215,031,751=151⋅751⋅28351. And for testing 64 bit integer it is enough to 
    check the first 12 prime bases: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 
    37."""

    if x < 2: return False 
    s, d = 0, x-1
    while d&1 == 0:
        s += 1
        d >>= 1
    for a in 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37:
        if x == a: return True
        v = pow(a, d, x) 
        if v != 1 and v != x-1:
            for j in range(1, s): 
                v = pow(v, 2, x)
                if v == x-1: break 
            if v != x-1: return False 
    return True