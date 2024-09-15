class StringUtils {
    public static int kmp(String pattern, String text) {
        int n = pattern.length();
        List<Integer> lps = new ArrayList<>();
        lps.add(0);
        for (int i = 1, k = 0; i < n; ++i) {
            while (k > 0 && pattern.charAt(k) != pattern.charAt(i)) k = lps.get(k-1);
            if (pattern.charAt(k) == pattern.charAt(i)) ++k;
            lps.add(k);
        }
        for (int i = 0, k = 0; i < text.length(); ++i) {
            while (k > 0 && pattern.charAt(k) != pattern.charAt(i)) k = lps.get(k-1);
            if (pattern.charAt(k) == text.charAt(i)) ++k;
            if (k == n) return i-n+1;
        }
        return -1;
    }

    public static List<Integer> kmp_all(String pattern, String text) {
        int n = pattern.length();
        List<Integer> lps = new ArrayList<>();
        lps.add(0);
        for (int i = 1, k = 0; i < n; ++i) {
            while (k > 0 && pattern.charAt(k) != pattern.charAt(i)) k = lps.get(k-1);
            if (pattern.charAt(k) == pattern.charAt(i)) ++k;
            lps.add(k);
        }
        List<Integer> ans = new ArrayList();
        for (int i = 0, k = 0; i < text.length(); ++i) {
            while (k > 0 && (k == n || pattern.charAt(k) != text.charAt(i))) k = lps.get(k-1);
            if (pattern.charAt(k) == text.charAt(i)) ++k;
            if (k == n) ans.add(i-n+1);
        }
        return ans;
    }

    public static int[] z_algo(String s) {
        int n = s.length();
        int[] ans = new int[n];
        for (int i = 1, ii = 0, lo = 0, hi = 0; i < n; ++i) {
            if (i <= hi) ii = i - lo;
            if (i + ans[ii] <= hi) ans[i] = ans[ii];
            else {
                lo = i;
                hi = Math.max(hi, i);
                while (hi < n && s.charAt(hi) == s.charAt(hi-lo)) ++hi;
                ans[i] = hi - lo;
                --hi;
            }
        }
        return ans;
    }
}
