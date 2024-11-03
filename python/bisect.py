"""
NAME
    bisect - binary search template 

DESCRIPTION
    This module implements the many version of binary search. 

    * bisect             binary search for        any occurrence
    * bisect_left        binary search for  left-most occurrence
    * bisect_rigth       binary search for right-most occurrence
    * bisect_first_true  binary search for first true occurrence
    * bisect_last_true   binary search for  last true occurrence

FUNCTIONS
    bisect(arr, x)
        Return a location where the value is x.

    bisect_left(arr, x)
        Return insertion point i for x so that all numbers to the right >= x.
        The return value i is such that all e in arr[:i] have e < x, and all e 
        in arr[i:] have e >= x. 

    bisect_right(arr, x)
        Return insertion point i for x so that all numbers to the right > x.
        The return value i is such that all e in arr[:i] have e <= x, and all 
        e in arr[i:] have e > x.

    bisect_first_true(arr, x)
        Binary the first location where number is evaluated to true.

    bisect_last_true(arr, x)
        Binary the last location where number is evaluated to true.
"""

def bisect(arr, x):
    """Return a location where the value is x."""
    lo, hi = 0, len(arr)-1 
    while lo <= hi: 
        mid = lo + hi >> 1
        if arr[mid] == x: return mid
        if arr[mid] < x: lo = mid + 1 
        else: hi = mid - 1
    return -1 


def bisect_left(arr, x): 
    """Return insertion point i for x so that all numbers to the right >= x."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + hi >> 1
        if arr[mid] < x: lo = mid + 1
        else: hi = mid
    return lo 


def bisect_right(arr, x): 
    """Return insertion point i for x so that all numbers to the right > x."""
    lo, hi = 0, len(arr)
    while lo < hi: 
        mid = lo + hi >> 1
        if arr[mid] <= x: lo = mid + 1
        else: hi = mid 
    return lo


def bisect_first_true(arr): 
    """Binary the first location where number is evaluated to true."""
    lo, hi = 0, len(arr)
    while lo < hi: 
        mid = lo + hi >> 1
        if arr[mid]: hi = mid
        else: lo = mid + 1
    return lo 


def bisect_last_true(arr): 
    """Binary the last location where number is evaluated to true."""
    lo, hi = -1, len(arr)-1 # last true at -1 for all false array
    while lo < hi: 
        mid = lo + hi + 1 >> 1
        if arr[mid]: lo = mid 
        else: hi = mid - 1
    return lo
