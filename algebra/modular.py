"""
NAME - modular

DESCRIPTION
    This module implements below algorithms:    
    * modular inverse
    * linear congruence equation 
    * Chinese remainder theorem
    * factorial modulo p 
    * discrete log 
    * primitive root 
    * discrete root 
    * Montgomery multiplication
"""

"""
MODULAR INVERSE 
1) extended Euclidean algorithm
2) binary exponentiation 
3) finding modular inverse for every number modulo m 

A modular inverse of an integer a is an integer x such that a⋅x is congruent to 
1 modular m, i.e. a⋅x ≡ 1 mod m. The modular inverse does not always exist. It 
can be proven that the modular inverse exists iff a and m are coprime.
"""

"""
1) finding modular inverse using extended Euclidean algorithm
Consider the below linear Diophantine equation in two variables x and y:

                            a⋅x + m⋅y = 1 

The equation has a solution iff gcd(a, m) = 1 which is also the condition for 
the modular inverse to exist. This equation can be solved using the extended 
Euclidean algorithm. If we take modulo m of both sides, the equation becomes 
a⋅x ≡ 1 mod m. Thus, the modular inverse of a is x.
"""

from fundamentals import euclidean

g, x, _ = euclidean(a, m) # if g == 1, x is legit

"""
2) finding modular inverse using binary exponentiation
Using Euler's theorem, the following congruence is true if a and m are coprimes:

a^ϕ(m) ≡ 1 mod m

where ϕ(m) is Euler's totient function. If m is a prime number, this simplifies 
to Fermat's little theorem:

a^(m−1) ≡ 1 mod m. 

Multiply both sides of the above equations by a^−1, and we get:
* For an arbitrary (but coprime) modulus m: a^(ϕ(m)−1) ≡ a^−1 mod m
* For a prime modulus m: a^(m−2) ≡ a^−1 mod m
Thus, we can find the modular inverse using the binary exponentiation algorithm.

In the case when m is not prime, we need to calculate Euler totient function, 
which costs O(sqrt(M)). 
"""

from fundamentals import binpow
inv = binpow(a, m-2, m) # Fermat's little theorem

"""
I suggest to use 
1) binary exponentiation algo when m is prime due to its conceptual simplicity;
2) extended Euclidean algo when a and m are coprimes due to its efficiency.
"""

"""
3) finding modular inverse for every number modulo m 
Here, we want to compute the modular inverse for every number in the range 
[1, m−1] where m is prime with time complexity O(m). Then for i > 1 the 
following equation is valid:

inv[i] = −⌊m/i⌋⋅inv[m % i] % m
"""

inv = [1]*m
for i in range(2, m): 
    inv[i] = m - m//i * inv[m % i] % m # modular inverse for all


"""
LINEAR CONGRUENCE EQUATOIN 

Given equation 

                            a⋅x = b (mod n) 

where x is unknown, we aim to find a solution in interval [0, n−1]. 

1) Solution by finding the inverse element
If a and n are coprime, then we can get a unique solution as 

                           x = b⋅a^−1 (mod n)

If a and n are not coprime, then a solution may not exist. Let g = gcd(a, n). 
* If b is not divisible by g, there is no solution. 
* If g divides b, there are exactly g solutions. 

By dividing both sides of the equation by g, we receive a new equation:

                           a′⋅x = b′ (mod n′)

in which a′ and n′ are coprime. This solution will also be a solution of the 
original equation. In addition, the original equation has exactly g solutions
like below 

                  xi = (x′ + i⋅n′) (mod n) for i = 0 … g−1

2) Solution with the Extended Euclidean Algorithm
We can rewrite the linear congruence to the below linear Diophantine equation:

                              a⋅x + n⋅k = b,

where x and k are unknown integers. This can be solved by extended Euclidean 
algorithm. 
"""


"""
FACTORIAL MODULO p
In this section, we develop an approach to efficiently calculate n! % p, 
without taking all the multiple factors of p into account that appear in the factorial. 

Algorithm
Let's write this factorial explicitly.

 n! % p = 1⋅2⋅3⋅...⋅(p-2)⋅(p-1)⋅p⋅(p+1)⋅(p+2)⋅...⋅(2p-1)⋅2p⋅(2p+1)⋅...⋅(p^2-1)⋅p^2⋅(p^2+1)⋅...⋅n (mod p)
        = 1⋅2⋅3⋅...⋅(p-2)⋅(p-1)⋅1⋅1⋅2⋅...⋅(p-1)⋅1⋅1⋅2⋅...⋅(p-1)⋅1⋅1⋅2⋅...⋅(n mod p) (mod p)
        = (1⋅2⋅3⋅...⋅(p-2)⋅(p-1)⋅1)^⌊n/p⌋⋅(1⋅2⋅...⋅(n mod p)) (mod p)

It is clear that factorial is divided into ⌊n/p⌋ blocks of same length and a 
remaining block. The main part is just (p-1)! ≡ -1 (mod p) per Wilson theorem. 
Since we have exactly ⌊n/p⌋ such blocks, we only need to look at the parity of 
the exponent and multiply by -1 if the parity is odd. Alternatively, we can 
subtract the current result from p. The remaining part is a modified factorial, 
i.e. ⌊n/p⌋! % p.
"""

def factmod(n: int, p: int) -> int: 
    """Return n % p in O(p + logp(n))."""
    fact = [1]*p
    for i in range(1, p): fact[i] = fact[i-1] * i % p 
    ans = 1
    while n > 1: 
        if n//p & 1: ans = p - ans 
        ans = ans * fact[n % p] % p 
        n //= p
    return ans 

"""
MULTIPLICITY OF p
If we want to compute a Binomial coefficient modulo p, then we additionally 
need the multiplicity of the p in n, i.e. the number of times p occurs in the 
prime factorization of n (not n!), or number of times we erased p during the computation 
of the modified factorial. Legendre's formula gives us a way to compute this in 
O(logpn) time. The formula gives the multiplicity 𝜈p as: 𝜈p(n!) = Σ⌊n/p^i⌋
"""

def factmult(n: int, p: int) -> int: 
    ans = 0
    while n: 
        n //= p
        ans += n 
    return ans 