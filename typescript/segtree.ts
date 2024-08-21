class SegTree {
    private n: number;
    private tree: number[];

    constructor(arr: number[]) {
        this.n = arr.length;
        this.tree = Array(4*this.n).fill(0);
        this.build(arr, 0, 0, this.n);
    }

    build(arr: number[], k: number, lo: number, hi: number): void {
        if (lo+1 == hi) this.tree[k] = arr[lo];
        else {
            const mid = lo + Math.floor((hi-lo)/2);
            this.build(arr, 2*k+1, lo, mid);
            this.build(arr, 2*k+2, mid, hi);
            this.tree[k] = Math.min(this.tree[2*k+1], this.tree[2*k+2]);
        }
    }

    update(i: number, val: number, k=0, lo=0, hi=0): void {
        if (hi == 0) hi = this.n;
        if (lo+1 == hi) this.tree[k] = val;
        else {
            const mid = lo + Math.floor((hi-lo)/2);
            if (i < mid) this.update(i, val, 2*k+1, lo, mid);
            else this.update(i, val, 2*k+2, mid, hi);
            this.tree[k] = Math.min(this.tree[2*k+1], this.tree[2*k+2]);
        }
    }

    query(qlo: number, qhi: number, k=0, lo=0, hi=0): number {
        if (hi == 0) hi = this.n;
        if (qhi <= lo || hi <= qlo) return Infinity;
        if (qlo <= lo && hi <= qhi) return this.tree[k];
        const mid = lo + Math.floor((hi-lo)/2);
        return Math.min(this.query(qlo, qhi, 2*k+1, lo, mid), this.query(qlo, qhi, 2*k+2, mid, hi));
    }
}
