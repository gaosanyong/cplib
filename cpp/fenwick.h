class Fenwick {
    /*Fenwick tree for prefix sum query*/
    vector<int> nums; 
public: 
    Fenwick(int n) {
        nums.resize(n+1); 
    }
    
    /*Update tree upon adding delta to kth element.*/
    void add(int k, int delta) {
        for (++k; k < nums.size(); k += k & -k) 
            nums[k] += delta; 
    }

    /*Return the prefix sum up to kth index (inclusive).*/
    long query(int k) {
        long ans = 0; 
        for (++k; k; k -= k & -k) 
            ans += nums[k]; 
        return ans; 
    }
}; 
