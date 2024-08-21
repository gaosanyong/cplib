class SegTree {
    
    constructor(arr) {
        this.n = arr.length;
        this.tree = Array(4*this.n).fill(0);
        this.build(arr, 0, 0, this.n);
    }

    build(arr, k, lo, hi) {
        if (lo+1 == hi) this.tree[k] = arr[lo];
        else {
            const mid = lo + Math.floor((hi-lo)/2);
            this.build(arr, 2*k+1, lo, mid);
            this.build(arr, 2*k+2, mid, hi);
            this.tree[k] = Math.min(this.tree[2*k+1], this.tree[2*k+2]);
        }
    }

    update(i, val, k=0, lo=0, hi=0) {
        if (hi == 0) hi = this.n;
        if (lo+1 == hi) this.tree[k] = val;
        else {
            const mid = lo + Math.floor((hi-lo)/2);
            if (i < mid) this.update(i, val, 2*k+1, lo, mid);
            else this.update(i, val, 2*k+2, mid, hi);
            this.tree[k] = Math.min(this.tree[2*k+1], this.tree[2*k+2]);
        }
    }

    query(qlo, qhi, k=0, lo=0, hi=0) {
        if (hi == 0) hi = this.n;
        if (qhi <= lo || hi <= qlo) return Infinity;
        if (qlo <= lo && hi <= qhi) return this.tree[k];
        const mid = lo + Math.floor((hi-lo)/2);
        return Math.min(this.query(qlo, qhi, 2*k+1, lo, mid), this.query(qlo, qhi, 2*k+2, mid, hi));
    }
}
