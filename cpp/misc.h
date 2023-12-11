constexpr 
auto pow(long base, int exp, int mod) noexcept {
    /* Compute base^exp % mod via binary exponentiation */
    long ans = 1; 
    for (; exp; exp >>= 1) {
        if (exp & 1) ans = ans * base % mod; 
        base = base * base % mod; 
    }
    return ans; 
}; 
