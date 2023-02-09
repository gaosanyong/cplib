"""
NAME - theoretic 

DESCRIPTION 
        This module implements below algorithms:
        * Euler's totient function
        * Number of divisors/sum of divisors

FUNCTIONS
    totient(n)
        Return Euler's totient function ϕ(n).

    totient_upto(n)
        Return all Euler's totient function values upto n.

    totient_upto2(n)
        Return all Euler's totient function values up to n.

    num_of_divisors(n)
        Return number of divisors of given number.

    sum_of_divisors(n)
        Return sum of divisors of given number.
"""

"""
EULER'S TOTIENT FUNCTION

Euler's totient function ϕ(n) counts the number of integers between 1 and n 
inclusive, which are coprime to n. 

Properties 
* If p is a prime number, then ϕ(p) = p−1.
* If p is a prime number and k ≥ 1, then there are exactly p^k/p numbers 
  between 1 and p^k that are divisible by p, which gives us 
  ϕ(p^k) = p^k − p^(k−1).
* If a and b are coprime, then ϕ(ab) = ϕ(a)⋅ϕ(b).
* In a and b are not coprime, then ϕ(ab) = ϕ(a)⋅ϕ(b)⋅d/ϕ(d) where d = gcd(a,b).

Thus, we can compute ϕ(n) through the factorization of n. If 
n = p1^a1⋅p2^a2⋯pk^ak, where pi is a prime factor of n, then 
ϕ(n) = n⋅(1−1/p1)⋅(1−1/p2)⋯(1−1/pk).

Divisor sum property 
∑ϕ(d) = n, where the sum is over all positive divisors d of n.

Euler's theorem | a^ϕ(m) ≡ 1 (mod m) if a and m are coprime.
Fermat's little theorem | a^(m−1) ≡ 1 (mod m) if m is prime.

Applications
This allows computing x^n mod m for very big n
a^n ≡ a^(n mod ϕ(m)) (mod m) if a and m are coprime.
"""

from collections import Counter
from math import sqrt 
from typing import List

def totient(n: int) -> int: 
    """Return Euler's totient function ϕ(n)."""
    ans = n 
    for p in range(2, int(sqrt(n))+1): 
        if n % p == 0: 
            while n % p == 0: n //= p
            ans -= ans//p 
    if n > 1: ans -= ans//n 
    return ans 


def totient_upto(n: int) -> List[int]: 
    """Return all Euler's totient function values upto n in O(Nlog(logN))."""
    ans = list(range(n+1))
    for x in range(2, n+1): 
        if ans[x] == x: 
            for xx in range(x, n+1, x): 
                ans[xx] -= ans[xx]//x 
    return ans 


def totient_upto2(n: int) -> List[int]: 
    """Return all Euler's totient function values upto n 
    using "divisor sum property" in O(NlogN)."""
    ans = [0, 1] + list(range(1, n))
    for x in range(2, n+1): 
        for xx in range(2*x, n+1, x): 
            ans[xx] -= ans[x]
    return ans 


"""
NUMBER OF DIVISORS 
If the prime factorization of n is p1^e1⋅p2^e2⋯pk^ek, where pi are distinct 
prime numbers, then the number of divisors is d(n) = (e1+1)⋅(e2+1)⋯(ek+1)
"""

def num_of_divisors(n: int) -> int: 
    """Return number of divisors of given number."""
    freq = Counter()
    for x in range(2, int(sqrt(n))+1): 
        while n % x == 0: 
            freq[x] += 1
            n //= x
    if n > 1: freq[n] += 1
    ans = 1
    for x in freq.values(): 
        ans *= 1 + x
    return ans 


"""
SUM OF DIVISORS 
If the prime factorization of n is p1^e1⋅p2^e2⋯pk^ek, where pi are distinct 
prime numbers, then the sum of divisors is 
σ(n)=(p1^(e1+1)−1)/(p1−1)⋅(p2^(e2+1)−1)/(p2−1)⋯(pk^(ek+1)−1)/(pk−1)
"""

def sum_of_divisors(n: int) -> int: 
    """Return sum of divisors of given number."""
    freq = Counter()
    for x in range(2, int(sqrt(n))+1): 
        while n % x == 0: 
            freq[x] += 1
            n //= x
    if n > 1: freq[n] += 1
    ans = 1
    for k, v in freq.items(): 
        ans *= (k**(v+1) - 1) // (k - 1)
    return ans 