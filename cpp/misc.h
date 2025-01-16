constexpr
auto pow(long long x, int p, int mod) noexcept {
    /* Compute x**p % mod via binary exponentiation */
    long long ans = 1;
    for (; p; p >>= 1) {
        if (p & 1) ans = ans * x % mod;
        x = x * x % mod;
    }
    return ans; 
}; 
