class StringUtils {
    public List<Integer> kmp_all(String pattern, String text) {
        List<Integer> lps = new ArrayList();
        lps.add(0);
        for (int i = 1, k = 0, n = pattern.length(); i < n; ++i) {
            while (k > 0 && pattern.charAt(k) != pattern.charAt(i)) k = lps.get(k-1);
            if (pattern.charAt(k) == pattern.charAt(i))++k;
            lps.add(k);
        }
        List<Integer> ans = new ArrayList();
        for (int i = 0, k = 0, n = pattern.length(); i < text.length(); ++i) {
            while (k > 0 && (k == n || pattern.charAt(k) != text.charAt(i))) k = lps.get(k-1);
            if (pattern.charAt(k) == text.charAt(i)) ++k;
            if (k == n) ans.add(i-n+1);
        }
        return ans;
    }
}
