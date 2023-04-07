import java.lang.Math; 

class SegTree {
    private int n; 
    private int[] tree; 

    private void build(int[] arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo]; 
        else {
            int mid = lo + (hi-lo)/2; 
            build(arr, 2*k+1, lo, mid); 
            build(arr, 2*k+2, mid, hi); 
            tree[k] = Math.min(tree[2*k+1], tree[2*k+2]); 
        }
    }

    public SegTree(int[] arr) {
        n = arr.length; 
        tree = new int[4*n]; 
        build(arr, 0, 0, n); 
    }

    public void update(int i, int val) {
        update(i, val, 0, 0, n); 
    }

    private void update(int i, int val, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = val; 
        else {
            int mid = lo + (hi-lo)/2; 
            if (i < mid) update(i, val, 2*k+1, lo, mid); 
            else update(i, val, 2*k+2, mid, hi); 
            tree[k] = Math.min(tree[2*k+1], tree[2*k+2]); 
        }
    }

    public int query(int qlo, int qhi) {
        return query(qlo, qhi, 0, 0, n); 
    }

    private int query(int qlo, int qhi, int k = 0, int lo = 0, int hi = 0) {
        if (qhi <= lo || hi <= qlo) return Integer.MAX_VALUE; 
        if (qlo <= lo && hi <= qhi) return tree[k]; 
        int mid = lo + (hi-lo)/2; 
        return Math.min(query(qlo, qhi, 2*k+1, lo, mid), query(qlo, qhi, 2*k+2, mid, hi)); 
    }
}