/**
 * A self-balancing binary search tree (BST) is any node-based binary search
 * tree that automatically keeps its height (maximal number of levels below the
 * root) small in the face of arbitrary item insertions and deletions. These
 * operations when designed for a self-balancing binary search tree, contain
 * precautionary measures against boundlessly increasing tree height, so that
 * these abstract data structures receive the attribute "self-balancing".
 * @class
 * @constructor
 * @public
 */
class TreeNode {
    constructor(key, value=0, left=null, right=null) {
        this.key = key;
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

class BalancedTree {
    constructor(obj) {
        this.compare = obj.compare;
        this.root = this.nil = null;
        this.size = 0;
    }

    /**
     * @param {number} key - the key those ceiling is to be found.
     * @returns the AVLTreeNode with the least key greater than or equal to the
     *          given key (null if no such key).
     */
    ceiling(key) {
        let ans = null;
        for (let node = this.root; node !== this.nil; )
            if (this.compare(key, node.key) <= 0) {
                ans = node;
                node = node.left;
            } else node = node.right;
        return ans;
    }

    /**
     * @param {number} key - the key whose floor is to be found.
     * @returns the AVLTreeNode with the greatest key less than or equal to the
     *          given key (null if no such key).
     */
    floor(key) {
        let ans = null;
        for (let node = this.root; node !== this.nil; )
            if (this.compare(key, node.key) < 0) node = node.left;
            else {
                ans = node;
                node = node.right;
            }
        return ans;
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

    /**
     * @returns a string representation of this tree.
     */
    toString() {
        return "{" + this.#traverse()
            .filter(x => x != this.nil)
            // .map(x => `${x.key}: ${x.value}`)
            .map(x => `${x.key}`)
            .join(", ") + "}";
    }

    /**
     * @private
     * @returns the outcome of in-order traveral of the tree.
     */
    #traverse() {
        const ans = [], stack = [];
        let node = this.root;
        while (stack.length || node)
            if (node) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                ans.push(node);
                node = node.right;
            }
        return ans;
    }
}


/**
 * The AVL tree, named after its inventors Georgy Adelson-Velsky and Evgenii
 * Landis, in their 1962 paper "An algorithm for the organization of
 * information", is a self-balancing Binary Search Tree (BST) where the
 * difference between heights of left and right subtrees for any node cannot be
 * more than one.
 * @class
 * @constructor
 * @public
 */
class AVLTreeNode extends TreeNode {
    constructor(key, value, left=null, right=null, height=1) {
        super(key, value, left, right);
        this.height = height;
    }
}

class AVLTree extends BalancedTree {

    constructor(obj) {
        /**
         * @property {AVLTreeNode} root - root of AVL tree.
         * @property {number} size - size of AVL tree.
         */
        super(obj);
        this.nil = this.root = null;
    }

    /**
     * @param {AVLTreeNode} node - the subtree whose balance is to be calculated.
     * @returns balance of the subtree rooted at node.
     */
    balance(node) {
        if (!node) return 0;
        return this.height(node.left) - this.height(node.right);
    }

    /**
     * Deletes the mapping for this key from this tree if present.
     * @param {number} key - the key to be deleted from the tree.
     * @returns void
     */
    delete(key) {
        this.root = this.#delete(this.root, key);
    }

    /**
     * @param {number} node - the AVLTreeNode whose height is of interest.
     * @returns the height of the subtree rooted at given node.
     */
    height(node) {
        return node ? node.height : 0;
    }

    /**
     * Associates the specified value with the specified key in this tree.
     * @param {number} key - the key to be inserted to the tree.
     * @param {number} value - the value to be inserted to the tree.
     * @returns void
     */
    insert(key, value=0) {
        this.root = this.#insert(this.root, key, value);
    }

    /**
     * @private
     * @param {AVLTreeNode} node - the subtree to delete the key.
     * @param {number} key - the key to be deleted from the subtree.
     * @return tree node after given key is deleted.
     */
    #delete(node, key) {
        if (!node) return node;
        if (this.compare(key, node.key) < 0) node.left = this.#delete(node.left, key);
        else if (this.compare(key, node.key) === 0) {
            if (!node.left) {
                let temp = node.right;
                node = null;
                --this.size;
                return temp;
            }
            if (!node.right) {
                let temp = node.left;
                node = null;
                --this.size;
                return temp;
            }
            let temp = this.minimum(node.right);
            node.key = temp.key;
            node.value = temp.value;
            node.right = this.#delete(node.right, temp.key);
        } else node.right = this.#delete(node.right, key);
        if (node) {
            node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
            let bal = this.balance(node);
            if (bal > 1 && this.balance(node.left) > 0)
                return this.#rightRotate(node);
            if (bal < -1 && this.balance(node.right) < 0)
                return this.#leftRotate(node);
            if (bal > 1 && this.balance(node.left) < 0) {
                node.left = this.#leftRotate(node.left);
                return this.#rightRotate(node);
            }
            if (bal < -1 && this.balance(node.right) > 0) {
                node.right = this.#rightRotate(node.right);
                return this.#leftRotate(node);
            }
        }
        return node;
    }

    /**
     * @private
     * @param {AVLTreeNode} node - the subtree to which the key-value pair is to be inserted.
     * @param {number} key - the key to be inserted.
     * @param {number} value - the value to be inserted.
     * @returns the tree node after the key-value pair is inserted into the subtree.
     */
    #insert(node, key, value) {
        if (!node) {
            ++this.size;
            return new AVLTreeNode(key, value);
        }
        if (this.compare(key, node.key) < 0) node.left = this.#insert(node.left, key, value);
        else if (this.compare(key, node.key) === 0) {
            node.value = value;
            return node;
        } else node.right = this.#insert(node.right, key, value);
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        let bal = this.balance(node);
        if (bal > 1 && this.compare(key, node.left.key) < 0)
            return this.#rightRotate(node);
        if (bal < -1 && this.compare(key, node.right.key) > 0)
            return this.#leftRotate(node);
        if (bal > 1 && this.compare(key, node.left.key) > 0) {
            node.left = this.#leftRotate(node.left);
            return this.#rightRotate(node);
        }
        if (bal < -1 && this.compare(key, node.right.key) < 0) {
            node.right = this.#rightRotate(node.right);
            return this.#leftRotate(node);
        }
        return node;
    }

    /**
     * @private
     * @param {AVLTreeNode} node - the tree node for left rotation.
     * @returns the tree node after left rotation.
     */
    #leftRotate(node) {
        let y = node.right, T2 = y.left;
        y.left = node;
        node.right = T2;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        y.height = 1 + Math.max(this.height(y.left), this.height(y.right));
        return y;
    }

    /**
     * @private
     * @param {AVLTreeNode} node - the tree node for right rotation.
     * @returns the tree node after right rotation.
     */
    #rightRotate(node) {
        let y = node.left, T3 = y.right;
        y.right = node;
        node.left = T3;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        y.height = 1 + Math.max(this.height(y.left), this.height(y.right));
        return y;
    }
}


/**
 * The red-black tree, introduced by Leonidas J Guibas and Robert Sedgewick, in
 * their 1978 paper "A dichromatic framework for balanced trees",  is a self-
 * balancing binary search tree data structure noted for fast storage and
 * retrieval of ordered information. The nodes in a red-black tree hold an extra
 * "color" bit, often drawn as red and black, which help ensure that the tree is
 * always approximately balanced..
 * @class
 * @constructor
 * @public
 */
class RBTreeNode extends TreeNode {
    constructor(key, value=0, color="black", left=null, right=null, parent=null) {
        super(key, value, left, right);
        this.color = color;
        this.parent = parent;
    }

    isRed() {
        return this.color === "red";
    }
}

class RBTree extends BalancedTree {
    constructor(obj) {
        super(obj);
        this.nil = this.root = new RBTreeNode(0);
    }

    /**
     * @param {number} key - the key to be deleted from the subtree.
     */
    delete(key) {
        let node = this.root;
        while (node !== this.nil)
            if (this.compare(key, node.key) < 0) node = node.left;
            else if (this.compare(key, node.key) === 0) break;
            else node = node.right;
        if (node != this.nil) {
            --this.size;
            let color = node.color, x, y = node;
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
    }

    /**
     * @param {number} key - the key to be inserted.
     * @param {number} value - the value to be inserted.
     */
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
                const y = z.parent.parent.right;
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
                const y = z.parent.parent.left;
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

    /**
     * @private
     * @param {RBTreeNode} node - the tree node for left rotation.
     */
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

    /**
     * @private
     * @param {RBTreeNode} node - the tree node for right rotation.
     */
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

    #transplant(u, v) {
        if (u.parent === this.nil) this.root = v;
        else if (u === u.parent.left) u.parent.left = v;
        else u.parent.right = v;
        v.parent = u.parent;
    }
}

if (typeof require !== "undefined" && require.main === module) {

    function check(tree) {
        const keys = [];
        for (let i = 0; i < 1000; ++i) {
            const k = Math.floor(1000*Math.random());
            const v = Math.floor(1000*Math.random());
            keys.push(k);
            tree.insert(k, v);
        }

        console.log("Tree after insertion:");
        console.log(tree.toString());
        console.log("");
        console.log("Tree size is ", tree.size);

        const result = tree.search(30);
        if (result) console.log("Node found");
        else console.log("Node not found");

        for (const k of keys)
            tree.delete(k);
        console.log("Tree size is ", tree.size);
        console.log("Tree after deletion:");
        console.log(tree.toString());
    }

    console.log("AVL Tree output:");
    check(new AVLTree({compare : (x, y) => x-y}));

    console.log("Red-Black Tree output:");
    check(new RBTree({compare : (x, y) => x-y}));
}
