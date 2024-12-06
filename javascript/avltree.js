class AVLTreeNode {
    constructor(key, value, left=null, right=null, height=1) {
        this.key = key;
        this.value = value;
        this.left = left;
        this.right = right;
        this.height = height;
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
class AVLTree {

    constructor(obj) {
        /**
         * @property {AVLTreeNode} root - root of AVL tree.
         * @property {number} size - size of AVL tree.
         */
        this.compare = obj.compare;
        this.root = null;
        this.size = 0;
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
     * @param {number} key - the key those ceiling is to be found.
     * @returns the AVLTreeNode with the least key greater than or equal to the
     *          given key (null if no such key).
     */
    ceiling(key) {
        let ans = null;
        for (let node = this.root; node; )
            if (this.compare(key, node.key) <= 0) {
                ans = node;
                node = node.left;
            } else node = node.right;
        return ans;
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
     * @param {number} key - the key whose floor is to be found.
     * @returns the AVLTreeNode with the greatest key less than or equal to the
     *          given key (null if no such key).
     */
    floor(key) {
        let ans = null;
        for (let node = this.root; node; )
            if (this.compare(key, node.key) < 0) node = node.left;
            else {
                ans = node;
                node = node.right;
            }
        return ans;
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
     * @param {AVLTreeNode} node - the node to start the search.
     * @returns the node associated with the maximum key (null if empty).
     */
    maximum(node=this.root) {
        while (node && node.right) node = node.right;
        return node;
    }

    /**
     * @param {AVLTreeNode} node - the node to start the search.
     * @returns the node associated with the minimum key (null if empty).
     */
    minimum(node=this.root) {
        while (node && node.left) node = node.left;
        return node;
    }

    /**
     * @param {number} key - the key to which the value is to be found.
     * @returns the value to which the specified key is mapped, or null if this
     *          tree contains no mapping for the key.
     */
    search(key) {
        let node = this.root;
        while (node && node.key != key) {
            if (this.compare(key, node.key) < 0) node = node.left;
            else node = node.right;
        }
        return node;
    }

    /**
     * @returns a string representation of this tree.
     */
    toString() {
        return "{" + this.#traverse().map(x => `${x.key}: ${x.value}`).join(", ") + "}";
    }

    /**
     * @returns an array of key-value pairs in the tree.
     */
    traverse() {
        return this.#traverse().map(x => [x.key, x.value]);
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
        if (!node) return node;
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


if (typeof require !== "undefined" && require.main === module) {
    const keys = [];
    const tree = new AVLTree({ compare : (x, y) => x-y });
    for (let i = 0; i < 1000; ++i) {
        const k = Math.floor(1000*Math.random());
        const v = Math.floor(1000*Math.random());
        keys.push(k);
        tree.insert(k, v);
    }

    function traverse(node) {
        if (node) {
            traverse(node.left);
            process.stdout.write(node.key.toString() + " ");
            traverse(node.right);
        }
    }

    console.log("Tree after insertion:");
    traverse(tree.root);
    console.log("");
    console.log("Tree size is ", tree.size);
    console.log("Tree height is:", tree.height(tree.root));

    const result = tree.search(30);
    if (result) console.log("Node found");
    else console.log("Node not found");

    for (const k of keys)
        tree.delete(k);
    console.log("Tree size is ", tree.size);
    console.log("Tree after deletion:");
    traverse(tree.root);
}
