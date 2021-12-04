"""
NAME
    strings - string-related algorithms

DESCRIPTION
    This module implements string-relatd algorithms.

    * kmp          string matching via Knuth-Moore-Pratt algo
    * boyer_moore  string matching via Boyer-Moore algo
    * rabin_karp   string matching via Rabin-Karp algo
    * manacher     longest palindromic substring via Manacher's algo

FUNCTIONS
    kmp(pattern, text)
        Search pattern within text via KMP algo.

    boyer_moore(pattern, text)
        Search pattern within text via Boyer-Moore algo.

    rabin_karp(pattern, text)
        Search pattern within text via Rabin-Karp algo.

    manacher(s)
        Find longest palindromic substring via Manacher's algo.
"""

def kmp(pattern, text):
    """Search pattern within text via KMP algo."""
    lps = [0]
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    k = 0
    for i in range(len(text)): 
        while k and pattern[k] != text[i]: k = lps[k-1]
        if pattern[k] == text[i]: k += 1
        if k == m: return i - m + 1
    return -1 


def boyer_moore(pattern, text):
    """Search pattern within text via Boyer-Moore algo."""
    m, n = len(pattern), len(text)
    jump = {}
    for i, c in enumerate(pattern): jump[c] = i 

    offset = 0
    while offset < n-m:
        skip = 0
        for j in reversed(range(m)):
            if text[offset+j] != pattern[j]:
                skip = max(1, j - jump.get(pattern[j], -1))
                break 
        if skip == 0: return True
        offset += skip
    return False


def rabin_karp(pattern, text):
    """Search pattern within text via Rabin-Karp algo (Monte Carlo version)."""
    R, Q = 128, 997
    hp = ht = 0 
    rm = 1/R
    for p, t in zip(pattern, text):
        hp = (hp * R + ord(p)) % Q
        ht = (ht * R + ord(t)) % Q 
        rm = rm * R % Q 
    if hp == ht: return True 

    m, n = len(pattern), len(text)
    for i in range(m, n):
        ht = (ht + Q - ord(text[i-m])) % Q
        ht = (ht + ord(text[i])) % Q 
        if ht == hp: return True 

    return False 


def manacher(s: str) -> str:               
    """Find longest palindromic substring via Manacher's algo."""
    ss = "#" + "#".join(s) + "#"
    n = len(ss)
    hlen = [0] * n # half-length
    center = right = 0
    for i in range(n):
        if i < right: hlen[i] = min(right-i, hlen[2*center-i])
        while 0 <= i-1-hlen[i] and i+1+hlen[i] < len(ss) and ss[i-1-hlen[i]] == ss[i+1+hlen[i]]: hlen[i] += 1
        if right < i+hlen[i]: center, right = i, i+hlen[i]
    xx, ii = max((x, i) for i, x in enumerate(hlen))
    return s[(ii-xx)//2 : (ii+xx)//2]