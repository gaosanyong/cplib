function kmp_all(pattern, text) {
    const lps = [0];
    for (let i = 1, k = 0, n = pattern.length; i < n; ++i) {
        while (k && pattern[k] != pattern[i]) k = lps[k-1];
        if (pattern[k] === pattern[i]) ++k;
        lps.push(k);
    }
    const ans = [];
    for (let i = 0, k = 0, n = pattern.length; i < text.length; ++i) {
        while (k && (k == n || pattern[k] != text[i])) k = lps[k-1];
        if (pattern[k] === text[i]) ++k;
        if (k == n) ans.push(i-n+1);
    }
    return ans;
}
