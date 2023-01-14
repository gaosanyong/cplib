class SegTree {
    int n; 
    vector<int> tree; 
    void build(vector<int>& arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo]; 
        else {
            int mid = lo + (hi-lo)/2; 
            build(arr, 2*k+1, lo, mid); 
            build(arr, 2*k+2, mid, hi); 
            tree[k] = max(tree[2*k+1], tree[2*k+2]); 
        }
    }
public: 
    SegTree(vector<int> arr) {
        n = arr.size(); 
        tree.resize(4*n); 
        build(arr, 0, 0, n); 
    }

    void update(int i, int val, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n; 
        if (lo+1 == hi) {
            tree[k] = val; 
        } else {
            int mid = lo + (hi-lo)/2; 
            if (i < mid) update(i, val, 2*k+1, lo, mid); 
            else update(i, val, 2*k+2, mid, hi); 
            tree[k] = max(tree[2*k+1], tree[2*k+2]); 
        }
    }

    int query(int qlo, int qhi, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n; 
        if (qhi <= lo || hi <= qlo) return INT_MIN; 
        if (qlo <= lo && hi <= qhi) return tree[k]; 
        int mid = lo + (hi-lo)/2; 
        return max(query(qlo, qhi, 2*k+1, lo, mid), query(qlo, qhi, 2*k+2, mid, hi)); 
    }
}; 