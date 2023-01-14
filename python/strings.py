"""
NAME
    strings - string-related algorithms

DESCRIPTION
    This module implements string-relatd algorithms.

    * kmp          string matching via Knuth-Moore-Pratt algo
    * boyer_moore  string matching via Boyer-Moore algo
    * rabin_karp   string matching via Rabin-Karp algo
    * manacher     longest palindromic substring via Manacher's algo
    * z_algo       length of substrings also prefixes via Z algo

FUNCTIONS
    
    kmp(pattern, text)
        Return location of 1st occurrence of pattern in text.
        
    kmp_all(pattern, text)
        Return locations of all occurrences of pattern in text.

    boyer_moore(pattern, text)
        Return true if pattern is found in text.

    rabin_karp(pattern, text)
        Return true if pattern is found in text.

    manacher(s)
        Return the longest palindromic substring.

    z_algo(s)
        Return lengths of substrings that are also prefix strings.
"""

def kmp(pattern, text):
    """Knuth-Moore-Pratt algo
    Return location of 1st occurrence of pattern in text."""
    lps = [0] # longest proper prefix also suffix 
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    k = 0
    for i, ch in enumerate(text): 
        while k and pattern[k] != ch: k = lps[k-1]
        if pattern[k] == ch: k += 1
        if k == len(pattern): return i - len(pattern) + 1
    return -1 


def kmp_all(pattern, text):
    """Knuth-Moore-Pratt algo
    Return locations of all occurrences of pattern in text."""
    ans = []
    lps = [0] # longest proper prefix also suffix 
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    k = 0
    for i, ch in enumerate(text): 
        while k and pattern[k] != ch: k = lps[k-1]
        if pattern[k] == ch: k += 1
        if k == len(pattern): 
            ans.append(i-len(pattern)+1)
            k = lps[k-1]
            while k and pattern[k] != ch: k = lps[k-1]
    return []


def boyer_moore(pattern, text):
    """Boyer-Moore algo
    Return true if pattern is found in text."""
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
    """Rabin-Karp algo (Monte Carlo version)
    Return true if pattern is found in text."""
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
    """Manacher's algo.
    Return the longest palindromic substring."""
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


def z_algo(s: str) -> List[int]: 
    """Z-algorithm
    Return lengths of substrings that are also prefix strings."""
    ans = [0] * len(s)
    lo = hi = ii = 0 
    for i in range(1, len(s)): 
        if i <= hi: ii = i - lo 
        if i + ans[ii] <= hi: ans[i] = ans[ii]
        else: 
            lo, hi = i, max(hi, i)
            while hi < len(s) and s[hi] == s[hi-lo]: hi += 1
            ans[i] = hi - lo 
            hi -= 1
    return ans 