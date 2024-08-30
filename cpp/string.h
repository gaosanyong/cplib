vector<int> kmp_all(string pattern, string text) {
    vector<int> lps(1);
    for (int i = 1, k = 0, n = pattern.size(); i < n; ++i) {
        while (k && pattern[k] != pattern[i]) k = lps[k-1];
        if (pattern[k] == pattern[i]) ++k;
        lps.push_back(k);
    }
    vector<int> ans;
    for (int i = 0, k = 0, n = pattern.size(); i < text.size(); ++i) {
        while (k && (k == n || pattern[k] != text[i])) k = lps[k-1];
        if (pattern[k] == text[i]) ++k;
        if (k == n) ans.push_back(i - n + 1);
    }
    return ans;
};


vector<int> z_algo(string s) {
    int n = s.size();
    vector<int> ans(n);
    for (int i = 0, ii = 0, lo = 0, hi = 0; i < n; ++i) {
        if (i <= hi) ii = i - lo;
        if (i+ans[ii] <= hi) ans[i] = ans[ii];
        else {
            lo = i;
            hi = max(hi, i);
            while (hi < n && s[hi] == s[hi-lo]) ++hi;
            ans[i] = hi - lo;
            --hi;
        }
    }
    return ans;
}
