"""
NAME - fundamentals 

DESCRIPTION
	This module implements below algorithms:	
	* binary exponentiation
	* Euclidean algorithms for computing the greatest common divisor
	* extended Euclidean algorithm
	* linear Diophantine equations
	* Fibonacci Numbers 
		o closed-form solution
		o fast doubling method

FUNCTIONS
	binpow(x, n, m)
		Return x**n % m.

	gcd(x, y)
		Return greatest common divisor via Euclidean algo.

	lcm(x, y)
		Return least common multiple.

	euclidean(x, y)
		Return greatest common divisor and coefficients via extended Euclidean algo.

	fib_formula0(n)
		Return nth Fibonacci number using formula.

	fib_formula1(n)
		Return nth Fibonacci number using formula.

	fib_fdm(n)
		Return nth and (n+1)st Fibonacci numbers via "fast doubling method". 
"""


"""
BINARY EXPONENTIATION

Binary exponentiation calculates x**n % m in O(logN).
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

Euclidean algorithm calculates greatest common divisor in O(log(min(M, N))).
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

Extended Euclidean algorithm calculates greatest common divisor 
and returns coefficients to arrive at it in O(log(min(M, N))). 
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

def fib_formula0(n): 
	"""Return nth Fibonacci number using formula."""
	return (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n) / sqrt(5)


def fib_formula1(n): 
	"""Return nth Fibonacci number using formula."""
	return round(((1+sqrt(5))/2)**n/sqrt(5))


def fib_fdm(n: int) -> Tuple[int]: 
	"""
	Return nth and (n+1)st Fibonacci numbers via "fast doubling method". 
	F(2*k) = F(k) * (2*F(k+1) - F(k))
	F(2*k + 1) = F(k) * F(k) + F(k+1) * F(k+1)
	"""
	if n == 0: return (0, 1)
	x, y = fibonacci(n//2)
	xx = x*(2*y - x)
	yy = x*x + y*y
	return (yy, xx+yy) if n&1 else (xx, yy)