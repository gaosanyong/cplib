"""
NAME
    strings - string-related algorithms

DESCRIPTION
    This module implements string-relatd algorithms.

    * AhoCorasick  string matching via Aho-Corasick algo
    * kmp          string matching via Knuth-Moore-Pratt algo
    * boyer_moore  string matching via Boyer-Moore algo
    * rabin_karp   string matching via Rabin-Karp algo
    * manacher     longest palindromic substring via Manacher's algo
    * z_algo       length of substrings also prefixes via Z algo

FUNCTIONS

    AhoCorasick
        build(patterns)
            Build Aho-Corasick automata with patterns.
        match(text)
            Return locations of matchings in text.

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

from collections import defaultdict, deque
from typing import List

class AhoCorasick:
    def __init__(self):
        self.root = {"output" : None, "parent" : None, "suffix" : None}

    def build(self, patterns: List[str]):
        for pattern in patterns:
            node = self.root
            for ch in pattern:
                if ch not in node: node[ch] = {"output" : None, "parent" : node, "suffix" : None}
                node = node[ch]
            node["$"] = pattern
        parent = None
        queue = deque([self.root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for ch, child in node.items():
                    if ch not in ("parent", "output", "suffix", "$"):
                        suffix = node["suffix"]
                        while suffix and ch not in suffix: suffix = suffix["suffix"]
                        if suffix:
                            child["suffix"] = suffix[ch]
                            if "$" in child["suffix"]: child["output"] = child["suffix"]
                            else: child["output"] = child["suffix"]["output"]
                        else:
                            child["output"] = None
                            child["suffix"] = self.root
                        queue.append(child)

    def match(self, text: str):
        ans = defaultdict(list)
        node = self.root
        for i, ch in enumerate(text):
            while ch not in node and node["suffix"]: node = node["suffix"]
            if ch in node: node = node[ch]
            output = node
            while output:
                if "$" in output:
                    pattern = output["$"]
                    ans[pattern].append(i-len(pattern)+1)
                output = output.output
        return ans


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
    k = 0
    lps = [0] # longest proper prefix also suffix
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    k = 0
    ans = []
    for i, ch in enumerate(text): 
        while k and (k == len(pattern) or pattern[k] != ch): k = lps[k-1]
        if pattern[k] == ch: k += 1
        if k == len(pattern): ans.append(i-len(pattern)+1)
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
        while 0 <= i-1-hlen[i] and i+1+hlen[i] < n and ss[i-1-hlen[i]] == ss[i+1+hlen[i]]: hlen[i] += 1
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
