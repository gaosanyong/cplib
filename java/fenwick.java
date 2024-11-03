class Fenwick {
    /*Fenwick tree for prefix sum query*/
    private int[] nums; 

    public Fenwick(int n) {
        nums = new int[n+1]; 
    }

    /*Update tree upon adding delta to kth element.*/
    public void add(int k, int delta) {
        for (++k; k < nums.length; k += k & -k)
            nums[k] += delta; 
    }

    /*Return the prefix sum up to kth index (inclusive).*/
    public long query(int k) {
        long ans = 0; 
        for (++k; k > 0; k -= k & -k) 
            ans += nums[k]; 
        return ans; 
    }
}
