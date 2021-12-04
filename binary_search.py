"""
NAME
	binary_search - binary search template 

DESCRIPTION
	This module implements the many version of binary search. 

	* bisect             binary search the only true occurrence
	* bisect_left        binary search the left-most occurrence
	* bisect_rigth       binary search the right-most occurrence
	* bisect_first_true  binary search the first true occurrence
	* bisect_last_true   binary search the last true occurrence

FUNCTIONS
	bisect(arr, x)
		Return the index of x if found or -1 if not. 

	bisect_left(arr, x)
		Return the index where to insert x into arr. 
		The return value i is such that all e in arr[:i] have e < x, and all e 
		in arr[i:] have e >= x. 

	bisect_right(arr, x)
		Return the index where to insert x into arr.
		The return value i is such that all e in arr[:i] have e <= x, and all 
		e in arr[i:] have e > x.

	bisect_first_true(arr, x)
		Return the first index where a predicate is evaluated to True.

	bisect_last_true(arr, x)
		Return the last index where a predicate is evaluated to True.
"""

def bisect(arr, x):
	"""Binary search the only true occurrence."""
	lo, hi = 0, len(arr)-1 # left close & right close 
	while lo <= hi: 
		mid = lo + hi >> 1
		if arr[mid] == x: return mid
		if arr[mid] < x: lo = mid + 1 
		else: hi = mid - 1
	return -1 


def bisect_left(arr, x): 
	"""Binary search array to find (left-most) x."""
	lo, hi = 0, len(arr)
	while lo < hi:
		mid = lo + hi >> 1
		if arr[mid] < x: lo = mid + 1
		else: hi = mid
	return lo 


def bisect_right(arr, x): 
	"""Binary search array to find (right-most) x."""
	lo, hi = 0, len(arr)
	while lo < hi: 
		mid = lo + hi >> 1
		if arr[mid] <= x: lo = mid + 1
		else: hi = mid 
	return lo


def bisect_first_true(arr): 
	"""Binary search for first True occurrence."""
	lo, hi = 0, len(arr)
	while lo < hi: 
		mid = lo + hi >> 1
		if arr[mid]: hi = mid
		else: lo = mid + 1
	return lo 


def bisect_last_true(arr): 
	"""Binary search for last True occurrence."""
	lo, hi = -1, len(arr)-1
	while lo < hi: 
		mid = lo + hi + 1 >> 1
		if arr[mid]: lo = mid 
		else: hi = mid - 1
	return lo