"""
NAME 
	factorization - integer factorization algorithms

DESCRIPTION
	This module implements a few integer factorization algorithms. 
	
	* trial division
	  + wheel factorization
	  + precomputed primes 
	* Fermat's factorizatoin method
	* Pollard's p-1 method
	* Pollard's rho algorithm
	  + Brent's algorithm

FUNCTIONS
	binpow(x, n, m)
		Return x**n % m.

	gcd(x, y)
		Return greatest common divisor via Euclidean algo.

	lcm(x, y)
		Return least common multiple.

	choose(n, k)
		Return binomial coefficient of n choose k.

	Catalan(n)
		Return nth Catalan number.
"""

from math import ceil, gcd, sqrt
from prime import sieve
from random import randint

"""
TRIAL DIVISION
We divide by each possible divisor d. We notice that it is impossible for 
prime factor of a composite number n to be bigger than √n. Therefore, we 
only need to test the divisors 2 ≤ d ≤ √n, which gives us the prime 
factorization in O(√n).
"""

def factor(n):
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

def wheel(n): 
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

def precomp(n): 
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

def fermat(n): 
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

def pminus1(n):
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
def rho(n, start=1, c=1): 
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


def brent(n, start=1, c=1):
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