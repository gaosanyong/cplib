template<class T>
class Fenwick {
    /*Fenwick tree with prefix sum query*/
    vector<T> nums; 
public: 
    Fenwick(int n) {
        nums.resize(n+1); 
    }

    void update(int k, T x) {
        /*Add kth element with value x.*/
        for (++k; k < nums.size(); k += k & -k) 
            nums[k] += x; 
    }

    T query(int k) {
        /*Return prefix sum of nums[0] ... nums[k] (inclusive).*/
        T ans = 0; 
        for (++k; k; k -= k & -k) 
            ans += nums[k]; 
        return ans; 
    }
}; 