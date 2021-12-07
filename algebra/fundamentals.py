"""
NAME 
	fundamentals - miscellaneous cp algorithms

DESCRIPTION
	This module implements a few cp algorithms. 
	
	* binary exponentiation
	* Euclidean algorithms for computing the greatest common divisor
	* extended Euclidean algorithm
	* linear Diophantine equations
	* Fibonacci Numbers 

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


"""
BINARY EXPONENTIATION
Binary exponentiation is an O(logN) algo to compute x**n % m.
"""
from typing import List

def binpow(x: int, n: int, m: int) -> int: 
	"""Return x**n % m."""
	ans = 1
	while n:
		if n & 1: ans = ans * x % m
		x = x * x % m
		n >>= 1
	return ans 


"""
EUCLIDEAN ALGORITHM FOR COMPUTING THE GREATEST COMMON DIVISOR
Euclidean algorithm is an O(log(min(M, N))) algo to compute greatest common 
divisor.
"""

def gcd(x: int, y: int) -> int:
	"""Return gcd via Euclidean algo."""
	while y: x, y = y, x%y
	return abs(x)


def lcm(x: int, y: int) -> int:
	"""Return least common multiple."""
	if x == 0 or y == 0: return 0
	return abs(x*y)//gcd(x, y)


"""
EXTENDED EUCLIDEAN ALGORITHM
"""

def euclidean(x: int, y: int) -> List[int]: 
	"""Return greatest common divisor and coefficients such that 
	   a * x + b * y == gcd(x, y)
	   via extended Euclidean algo."""
	a = bb = 1
	b = aa = 0
	while y: 
		q = int(x / y) 
		a, aa = aa, a - q*aa 
		b, bb = bb, b - q*bb 
		x, y = y, x - q*y 
	return x, a, b


"""
LINEAR DIOPHANTINE EQUATIONS (a * x + b * y == c)

1) finding one solution
2) finding all solutions
3) finding the number of solutions and the solutions themselves in a given interval
4) finding a solution with minimum value of x+y
"""

"""
FIBONACCI NUMBERS

Cassini's identity: F(n-1)*F(n+1) - F(n)*F(n) = (-1)**n
the "addition" rule: F(n+k) = F(k)*F(n+1) + F(k-1)*F(n) or F(2*n) = F(n)*(F(n-1) + F(n+1))
GCD identity: gcd(F(m), F(n)) = F(gcd(m, n))

Zeckendorf's theorem: 
Any natural number n can be uniquely represented as a sum of Fibonacci numbers
n = F(k1) + F(k2) + … + F(kr)
such that k1 ≥ k2+2, k2 ≥ k3+2, …, kr ≥ 2 (i.e.: the representation cannot use two consecutive Fibonacci numbers).
"""

def fibonacci(n): 
	"""Return nth Fibonacci number."""
	return (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n) / sqrt(5)


def fibonacci(n): 
	return round(((1+sqrt(5))/2)**n/sqrt(5))


def fibonacci(n: int) -> List[int]: 
	"""
	Return F(n) and F(n+1) as a pair via "fast doubling method". 
	F(2*k) = F(k) * (2*F(k+1) - F(k))
	F(2*k + 1) = F(k) * F(k) + F(k+1) * F(k+1)
	"""
	if n == 0: return [0, 1]
	x, y = fibonacci(n >> 1)
	xx = x * (2*y - x)
	yy = x*x + y*y
	return [yy, xx+yy] if n&1 else [xx, yy]


def choose(n: int, k: int) -> int:
	"""Return binomial coefficient of n choose k."""
	ans = 1
	for i in range(min(k, n-k)):
		ans *= n-i
		ans //= i+1
	return ans 


def catalan(n: int) -> int: 
	"""Return nth Catalan number."""
	ans = 1
	for i in range(n): 
		ans *= 2*n - i
		ans //= i+1
	return ans//(n+1)