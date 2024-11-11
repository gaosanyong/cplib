/**
 * @author Ye Gao
 * @description Union-find algorithm.
 * @license MIT License
 * @name unionfind.js
 * @see {@link https://github.com/gaosanyong/cplib} for further information.
 * @version 0.0.1
 */

class UnionFind {
    constructor(n) {
        this.parent = Array(n).fill(0); 
        this.rank = Array(n).fill(1); 
    }

    find(p) {
        if (p != this.parent[p]) 
            this.parent[p] = find(this.parent[p]); 
        return this.parent[p]; 
    }

    union(p, q) {
        let prt = this.find(p), qrt = find(q);
        if (prt == qrt) return false; 
        if (this.rank[prt] > this.rank[qrt]) [prt, qrt] = [qrt, prt]; 
        this.parent[prt] = qrt; 
        this.rank[qrt] += this.rank[prt]; 
        return true; 
    }
}
