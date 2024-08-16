/*A Fenwick tree or binary indexed tree (BIT) is a data structure that can
efficiently update values and calculate prefix sums in an array of values.*/

class Fenwick {
    private nums: number[];
    
    constructor(n) {
        this.nums = Array(n+1).fill(0); 
    }
    
    add(k, delta) {
        for (++k; k < this.nums.length; k += k & -k)
            this.nums[k] += delta; 
    }
    
    query(k) {
        let ans = 0; 
        for (++k; k; k -= k & -k) 
            ans += this.nums[k]; 
        return ans; 
    }
}
