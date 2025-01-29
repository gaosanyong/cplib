#include <algorithm>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class UnionFind {
    /*Union-Find implemented via array*/
public: 
    vector<int> parent, rank; 
    UnionFind(int n) {
        parent.resize(n); 
        iota(begin(parent), end(parent), 0); 
        rank.resize(n); 
        fill(rank.begin(), rank.end(), 1); 
    } 
    
    int find(int p) {
        /* find with path compression */
        if (parent[p] != p) 
            parent[p] = find(parent[p]); 
        return parent[p]; 
    }
    
    bool connect(int p, int q) {
        /* union with rank */
        int prt = find(p), qrt = find(q); 
        if (prt == qrt) return false; 
        if (rank[prt] > rank[qrt]) swap(prt, qrt);
        parent[prt] = qrt; 
        rank[qrt] += rank[prt]; 
        return true; 
    }
};


class UnionFindDict {
    /*Union-Find implemented via dictionary*/
public: 
    unordered_map<string, string> parent; 
    unordered_map<string, int> rank; 
    
    string find(string p) {
        if (!parent.count(p)) parent[p] = p, rank[p] = 1; 
        else if (p != parent[p]) 
            parent[p] = find(parent[p]); 
        return parent[p]; 
    }
    
    bool connect(string p, string q) {
        string prt = find(p), qrt = find(q); 
        if (prt == qrt) return false; 
        if (rank[prt] > rank[qrt]) swap(prt, qrt); 
        parent[prt] = qrt; 
        rank[qrt] += rank[prt]; 
        return true; 
    }
}; 
