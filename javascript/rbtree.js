class RBTreeNode {
    constructor(key, value=0, color="black", left=null, right=null, parent=null) {
        this.key = key;
        this.value = value;
        this.color = color;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }

    isRed() {
        return this.color === "red";
    }
}

class RBTree {
    constructor(obj) {
        this.compare = obj.compare;
        this.nil = this.root = new RBTreeNode(0);;
        this.size = 0;
    }

    delete(key) {
        let target = null;
        for (let node = this.root; node !== this.nil; )
            if (this.compare(key, node.key) < 0) node = node.left;
            else if (this.compare(key, node.key) === 0) {
                target = node;
                break;
            } else node = node.right;
        if (target) this.#delete(target);
    }

    insert(key, value=0) {
        let parent = this.nil;
        for (let node = this.root; node !== this.nil; ) {
            parent = node;
            if (this.compare(key, node.key) < 0) node = node.left;
            else if (this.compare(key, node.key) === 0) {
                node.value = value;
                return;
            }
            else node = node.right;
        }
        ++this.size;
        const node = new RBTreeNode(key, value, "red", this.nil, this.nil, this.nil);
        node.parent = parent;
        if (parent === this.nil) this.root = node;
        else if (this.compare(key, parent.key) < 0) parent.left = node;
        else parent.right = node;
        this.#insertFixUp(node);
    }

    /**
     * @param {AVLTreeNode} node - the node to start the search.
     * @returns the node associated with the maximum key (null if empty).
     */
    maximum(node=this.root) {
        while (node != this.nil && node.right !== this.nil) node = node.right;
        return node;
    }

    /**
     * @param {AVLTreeNode} node - the node to start the search.
     * @returns the node associated with the minimum key (null if empty).
     */
    minimum(node=this.root) {
        while (node != this.nul && node.left !== this.nil) node = node.left;
        return node;
    }

    /**
     * @param {number} key - the key to which the value is to be found.
     * @returns the value to which the specified key is mapped, or null if this
     *          tree contains no mapping for the key.
     */
    search(key) {
        let node = this.root;
        while (node != this.nil && this.compare(key, node.key) !== 0)
            if (this.compare(key, node.key) < 0) node = node.left;
            else node = node.right;
        return node;
    }

    toString() {
        return "{" + this.#traverse().map(x => `${x.key}: ${x.value}`).join(", ") + "}";
    }

    #delete(node) {
        --this.size;
        let color = node.color;
        let x, y = node;
        if (node.left === this.nil) {
            x = node.right;
            this.#transplant(node, node.right);
        } else if (node.right === this.nil) {
            x = node.left;
            this.#transplant(node, node.left);
        } else {
            y = this.minimum(node.right);
            color = y.color;
            x = y.right;
            if (y.parent === node) x.parent = y;
            else {
                this.#transplant(y, y.right);
                y.right = node.right;
                y.right.parent = y;
            }
            this.#transplant(node, y);
            y.left = node.left;
            y.left.parent = y;
            y.color = node.color;
        }
        if (color === "black") this.#deleteFixUp(x);
    }

    #transplant(u, v) {
        if (u.parent === this.nil) this.root = v;
        else if (u === u.parent.left) u.parent.left = v;
        else u.parent.right = v;
        v.parent = u.parent;
    }

    #deleteFixUp(x) {
        while (x !== this.root && !x.isRed())
            if (x === x.parent.left) {
                let w = x.parent.right;
                if (w.isRed()) {
                    w.color = "black";
                    x.parent.color = "red";
                    this.#leftRotate(x.parent);
                    w = x.parent.right;
                }
                if (!w.left.isRed() && !w.right.isRed()) {
                    w.color = "red";
                    x = x.parent;
                } else {
                    if (!w.right.isRed()) {
                        w.left.color = "black";
                        w.color = "red";
                        this.#rightRotate(w);
                        w = x.parent.right;
                    }
                    w.color = x.parent.color;
                    x.parent.color = "black";
                    w.right.color = "black";
                    this.#leftRotate(x.parent);
                    x = this.root;
                }
            } else {
                let w = x.parent.left;
                if (w.isRed()) {
                    w.color = "black";
                    x.parent.color = "red";
                    this.#rightRotate(x.parent);
                    w = x.parent.left;
                }
                if (!w.right.isRed() && !w.left.isRed()) {
                    w.color = "red";
                    x = x.parent;
                } else {
                    if (!w.left.isRed()) {
                        w.right.color = "black";
                        w.color = "red";
                        this.#leftRotate(w);
                        w = x.parent.left;
                    }
                    w.color = x.parent.color;
                    x.parent.color = "black";
                    w.left.color = "black";
                    this.#rightRotate(x.parent);
                    x = this.root;
                }
            }
        x.color = "black";
    }

    #insertFixUp(z) {
        while (z.parent.isRed())
            if (z.parent === z.parent.parent.left) {
                let y = z.parent.parent.right;
                if (y.isRed()) {
                    z.parent.color = "black";
                    y.color = "black";
                    z.parent.parent.color = "red";
                    z = z.parent.parent;
                } else {
                    if (z === z.parent.right) {
                        z = z.parent;
                        this.#leftRotate(z);
                    }
                    z.parent.color = "black";
                    z.parent.parent.color = "red";
                    this.#rightRotate(z.parent.parent);
                }
            } else {
                let y = z.parent.parent.left;
                if (y.isRed()) {
                    z.parent.color = "black";
                    y.color = "black";
                    z.parent.parent.color = "red";
                    z = z.parent.parent;
                } else {
                    if (z === z.parent.left) {
                        z = z.parent;
                        this.#rightRotate(z);
                    }
                    z.parent.color = "black";
                    z.parent.parent.color = "red";
                    this.#leftRotate(z.parent.parent);
                }
            }
        this.root.color = "black";
    }

    #leftRotate(node) {
        const y = node.right;
        node.right = y.left;
        if (y.left !== this.nil) y.left.parent = node;
        y.parent = node.parent;
        if (node.parent === this.nil) this.root = y;
        else if (node === node.parent.left) node.parent.left = y;
        else node.parent.right = y;
        y.left = node;
        node.parent = y;
    }

    #rightRotate(node) {
        const y = node.left;
        node.left = y.right;
        if (y.right !== this.nil) y.right.parent = node;
        y.parent = node.parent;
        if (node.parent === this.nil) this.root = y;
        else if (node === node.parent.left) node.parent.left = y;
        else node.parent.right = y;
        y.right = node;
        node.parent = y;
    }

    #traverse() {
        const ans = [], stack = [];
        let node = this.root;
        while (stack.length || node)
            if (node) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                if (node != this.nil) ans.push(node);
                node = node.right;
            }
        return ans;
    }
}

if (typeof require !== "undefined" && require.main === module) {
    const keys = [];
    const tree = new RBTree({compare : (x, y) => x-y});
    for (let i = 0; i < 1000; ++i) {
        const k = Math.floor(1000*Math.random());
        const v = Math.floor(1000*Math.random());
        keys.push(k);
        tree.insert(k, v);
    }

    function traverse(node) {
        if (node) {
            traverse(node.left);
            if (node.key > 0) process.stdout.write(node.key.toString() + " ");
            traverse(node.right);
        }
    }

    console.log(tree.toString());
    console.log("Tree after insertion:");
    traverse(tree.root);
    console.log("");
    console.log("Tree size is ", tree.size);

    const result = tree.search(30);
    if (result) console.log("Node found");
    else console.log("Node not found");

    for (const k of keys)
        tree.delete(k);
    console.log("Tree size is ", tree.size);
    console.log("Tree after deletion:");
    traverse(tree.root);
}
