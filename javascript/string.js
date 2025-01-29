function kmp(pattern, text) {
    const lps = [0];
    for (let i = 1, k = 0, n = pattern.length; i < n; ++i) {
        while (k && pattern[k] !== pattern[i]) k = lps[k-1];
        if (pattern[k] === pattern[i]) ++k;
        lps.push(k);
    }
    const ans = [];
    for (let i = 0, k = 0, n = pattern.length; i < text.length; ++i) {
        while (k && pattern[k] !== text[i]) k = lps[k-1];
        if (pattern[k] === text[i]) ++k;
        if (k === n) return i-n+1;
    }
    return -1;
}

function kmp_all(pattern, text) {
    const lps = [0];
    for (let i = 1, k = 0, n = pattern.length; i < n; ++i) {
        while (k && pattern[k] !== pattern[i]) k = lps[k-1];
        if (pattern[k] === pattern[i]) ++k;
        lps.push(k);
    }
    const ans = [];
    for (let i = 0, k = 0, n = pattern.length; i < text.length; ++i) {
        while (k && (k === n || pattern[k] !== text[i])) k = lps[k-1];
        if (pattern[k] === text[i]) ++k;
        if (k === n) ans.push(i-n+1);
    }
    return ans;
}

function manacher(s) {
    const ss = "#" + s.split("").join("#") + "#";
    const n = ss.length;
    const hlen = Array(n).fill(0);
    let center = 0, right = 0;
    for (let i = 0; i < n; ++i) {
        if (i < right) hlen[i] = Math.min(right-i, hlen[2*center-i]);
        while (0 <= i-1-hlen[i] && i+1+hlen[i] < n && ss[i-1-hlen[i]] === ss[i+1+hlen[i]]) ++hlen[i];
        if (right < i+hlen[i]) [center, right] = [i, i+hlen[i]];
    }
    let i = hlen.indexOf(Math.max(...hlen));
    return s.substring(Math.floor((i-hlen[i])/2), Math.floor((i+hlen[i])/2));
}

function z_algo(s) {
    const n = s.length;
    const ans = Array(n).fill(0);
    for (let i = 1, ii = 0, lo = 0, hi = 0; i < n; ++i) {
        if (i <= hi) ii = i - lo;
        if (i + ans[ii] <= hi) ans[i]= ans[ii];
        else {
            lo = i;
            hi = Math.max(hi, i);
            while (hi < n && s[hi] === s[hi-lo]) ++hi;
            ans[i] = hi - lo;
            --hi;
        }
    }
    return ans;
}
