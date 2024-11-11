/**
 * @author Ye Gao
 * @description Fenwick tree to calculate prefix sum dynamically.
 * @license MIT License
 * @name fenwick.js
 * @see {@link https://github.com/gaosanyong/cplib} for further information.
 * @version 0.0.1
 */

class Fenwick {
    /*A Fenwick tree or binary indexed tree (BIT) is a data structure that can
    efficiently update values and calculate prefix sums in an array of values.*/
    constructor(n) {
        this.nums = Array(n+1).fill(0);
    }

    update(k, delta) {
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
