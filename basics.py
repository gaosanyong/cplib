"""
NAME 
	basics - miscellaneous cp algorithms

DESCRIPTION
	This module implements a few cp algorithms. 

	* binpow  - binary exponentiation 
	* gcd     - greatest common divisor via Euclidean algo
	* lcm     - least common multiplier 
	* choose  - binomial coefficient 
	* catalan - Catalan number 

FUNCTIONS
	binpow(x, n, m)
		Return x**n % m.

	gcd(x, y)
		Return greatest common divisor via Euclidean algo.

	lcm(x, y)
		Return least common multiplier.

	choose(n, k)
		Return binomial coefficient of n choose k.

	Catalan(n)
		Return nth Catalan number.
"""


"""
Binary exponentiation
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
Euclidean algorithm 
Euclidean algorithm is an O(log(min(M, N))) algo to compute greatest common 
divisor.
"""

def gcd(x: int, y: int) -> int:
	"""Return greatest common divisor via Euclidean algo."""
	while y: x, y = y, x%y
	return abs(x)


def lcm(x: int, y: int) -> int:
	"""Return least common multiple."""
	if x == 0 or y == 0: return 0
	return abs(x*y)//gcd(x, y)


def _euclidean(x: int, y: int) -> List[int]: 
	"""Return greatest common divisor and coefficients via extended Euclidean algo."""
	a = bb = 1
	b = aa = 0
	while y: 
		q = int(x / y) 
		a, aa = aa, a - q*aa 
		b, bb = bb, b - q*bb 
		x, y = y, x - q*y 
	return x, a, b


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