import java.lang.Math; 

class SegTreeLazy {
    private int n = 0; 
    private int[] tree, lazy; 

    private void build(int[] arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo]; 
        else {
            int mid = lo + (hi-lo)/2; 
            build(arr, 2*k+1, lo, mid); 
            build(arr, 2*k+2, mid, hi); 
            tree[k] = Math.min(tree[2*k+1], tree[2*k+2]); 
        }
    }

    public SegTreeLazy(int[] arr) {
        n = arr.length; 
        tree = new int[4*n]; 
        lazy = new int[4*n]; 
        build(arr, 0, 0, n); 
    }

    public void update(int qlo, int qhi, int delta, int k, int lo, int hi) {
        if (hi == 0) hi = n; 
        if (lazy[k] > 0) {
            tree[k] += lazy[k]; 
            if (lo+1 < hi) {
                lazy[2*k+1] += lazy[k]; 
                lazy[2*k+2] += lazy[k]; 
            }
            lazy[k] = 0; 
        }
        if (lo < hi && qlo < hi && lo < qhi) {
            if (qlo <= lo && hi <= qhi) {
                tree[k] += delta; 
                if (lo+1 < hi) {
                    lazy[2*k+1] += delta; 
                    lazy[2*k+2] += delta; 
                }
            } else {
                int mid = lo + (hi - lo)/2; 
                update(qlo, qhi, delta, 2*k+1, lo, mid); 
                update(qlo, qhi, delta, 2*k+2, mid, hi); 
                tree[k] = Math.min(tree[2*k+1], tree[2*k+2]); 
            }
        }
    }

    public int query(int qlo, int qhi, int k, int lo, int hi) {
        if (hi == 0) hi = n; 
        if (lazy[k] > 0) {
            tree[k] += lazy[k]; 
            if (lo+1 < hi) {
                lazy[2*k+1] += lazy[k]; 
                lazy[2*k+2] += lazy[k]; 
            }
            lazy[k] = 0; 
        }
        if (qhi <= lo || hi <= qlo) return Integer.MAX_VALUE; 
        if (qlo <= lo && hi <= qhi) return tree[k]; 
        int mid = lo + (hi-lo)/2; 
        return Math.min(query(qlo, qhi, 2*k+1, lo, mid), query(qlo, qhi, 2*k+2, mid, hi)); 
    }
}