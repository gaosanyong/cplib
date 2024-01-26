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
