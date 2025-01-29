#include <vector>

using namespace std;

class SegTree {
    int n; 
    vector<int> tree; 
    void build(vector<int>& arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo]; 
        else {
            int mid = lo + (hi-lo)/2; 
            build(arr, 2*k+1, lo, mid); 
            build(arr, 2*k+2, mid, hi); 
            tree[k] = min(tree[2*k+1], tree[2*k+2]); 
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
        if (lo+1 == hi) tree[k] = val; 
        else {
            int mid = lo + (hi-lo)/2; 
            if (i < mid) update(i, val, 2*k+1, lo, mid); 
            else update(i, val, 2*k+2, mid, hi); 
            tree[k] = min(tree[2*k+1], tree[2*k+2]); 
        }
    }

    int query(int qlo, int qhi, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n; 
        if (qhi <= lo || hi <= qlo) return INT_MAX; 
        if (qlo <= lo && hi <= qhi) return tree[k]; 
        int mid = lo + (hi-lo)/2; 
        return min(query(qlo, qhi, 2*k+1, lo, mid), query(qlo, qhi, 2*k+2, mid, hi)); 
    }
}; 


class LazySegTreeMin {
    int n = 0; 
    vector<int> lazy;
    vector<int> tree; 
    void build(vector<int>& arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo]; 
        else {
            int mid = lo + (hi-lo)/2; 
            build(arr, 2*k+1, lo, mid); 
            build(arr, 2*k+2, mid, hi); 
            tree[k] = min(tree[2*k+1], tree[2*k+2]); 
        }
    }
public: 
    LazySegTreeMin(vector<int> arr) {
        n = arr.size(); 
        lazy.resize(4*n);
        tree.resize(4*n); 
        build(arr, 0, 0, n); 
    }

    void update(int qlo, int qhi, int delta, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n; 
        if (lazy[k]) {
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
                tree[k] = min(tree[2*k+1], tree[2*k+2]); 
            }
        }
    }

    int query(int qlo, int qhi, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n; 
        if (lazy[k]) {
            tree[k] += lazy[k]; 
            if (lo+1 < hi) {
                lazy[2*k+1] += lazy[k]; 
                lazy[2*k+2] += lazy[k]; 
            }
            lazy[k] = 0; 
        }
        if (qhi <= lo || hi <= qlo) return INT_MAX; 
        if (qlo <= lo && hi <= qhi) return tree[k]; 
        int mid = lo + (hi-lo)/2; 
        return min(query(qlo, qhi, 2*k+1, lo, mid), query(qlo, qhi, 2*k+2, mid, hi)); 
    }
}; 


class LazySegTreeSum {
    int n = 0;
    vector<int> lazy;
    vector<int> tree;
    void build(vector<int>& arr, int k, int lo, int hi) {
        if (lo+1 == hi) tree[k] = arr[lo];
        else {
            int mid = lo + (hi-lo)/2;
            build(arr, 2*k+1, lo, mid);
            build(arr, 2*k+2, mid, hi);
            tree[k] = tree[2*k+1] + tree[2*k+2];
        }
    }
public:
    LazySegTreeSum(vector<int> arr) {
        n = arr.size();
        lazy.resize(4*n);
        tree.resize(4*n);
        build(arr, 0, 0, n);
    }

    void update(int qlo, int qhi, int delta, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n;
        if (lazy[k]) {
            tree[k] += (hi-lo)*lazy[k];
            if (lo+1 < hi) {
                lazy[2*k+1] += lazy[k];
                lazy[2*k+2] += lazy[k];
            }
            lazy[k] = 0;
        }
        if (lo < hi && qlo < hi && lo < qhi) {
            if (qlo <= lo && hi <= qhi) {
                tree[k] += (hi-lo)*delta;
                if (lo+1 < hi) {
                    lazy[2*k+1] += delta;
                    lazy[2*k+2] += delta;
                }
            } else {
                int mid = lo + (hi-lo)/2;
                update(qlo, qhi, delta, 2*k+1, lo, mid);
                update(qlo, qhi, delta, 2*k+2, mid, hi);
                tree[k] = tree[2*k+1] + tree[2*k+2];
            }
        }
    }

    int query(int qlo, int qhi, int k = 0, int lo = 0, int hi = 0) {
        if (hi == 0) hi = n;
        if (lazy[k]) {
            tree[k] += (hi-lo)*lazy[k];
            if (lo+1 < hi) {
                lazy[2*k+1] += lazy[k];
                lazy[2*k+2] += lazy[k];
            }
            lazy[k] = 0;
        }
        if (qhi <= lo || hi <= qlo) return 0;
        if (qlo <= lo && hi <= qhi) return tree[k];
        int mid = lo + (hi-lo)/2;
        return query(qlo, qhi, 2*k+1, lo, mid) + query(qlo, qhi, 2*k+2, mid, hi);
    }
};
