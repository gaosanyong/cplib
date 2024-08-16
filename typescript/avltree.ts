class TreeNode {
    public key: number;
    public value: number;
    public left: TreeNode | null;
    public right: TreeNode | null;
    public height: number;

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
    public root: TreeNode | null;
    public size: number;

    constructor() {
        /**
         * @property {TreeNode} root - root of AVL tree.
         * @property {number} size - size of AVL tree.
         */
        this.root = null;
        this.size = 0;
    }

    /**
     * @param {TreeNode} node - the subtree whose balance is to be calculated.
     * @returns balance of the subtree rooted at node.
     */
    balance(node) {
        if (!node) return 0;
        return this.height(node.left) - this.height(node.right);
    }

    /**
     * @param {number} key - the key those ceiling is to be found.
     * @returns the TreeNode with the least key greater than or equal to the
     *          given key (null if no such key).
     */
    ceilingEntry(key) {
        let ans = null;
        for (let node = this.root; node; )
            if (node.key < key) node = node.right;
            else {
                ans = node;
                node = node.left;
            }
        return ans;
    }

    /**
     * @returns an array of key-value pairs in the tree.
     */
    entrySet() {
        return this.#traverse().map(x => [x.key, x.value]);
    }

    /**
     * @returns the node associated with the least key (null if empty).
     */
    firstEntry() {
        return this.#firstEntry(this.root);
    }

    /**
     * @param {number} key - the key whose floor is to be found.
     * @returns the TreeNode with the greatest key less than or equal to the
     *          given key (null if no such key).
     */
    floorEntry(key) {
        let ans = null;
        for (let node = this.root; node; )
            if (key < node.key) node = node.left;
            else {
                ans = node;
                node = node.right;
            }
        return ans;
    }

    /**
     * @param {number} key - the key to which the value is to be found.
     * @returns the value to which the specified key is mapped, or null if this
     *          tree contains no mapping for the key.
     */
    get(key) {
        return this.#get(this.root, key);
    }

    /**
     * @param {number} node - the TreeNode whose height is of interest.
     * @returns the height of the subtree rooted at given node.
     */
    height(node) {
        return node ? node.height : 0;
    }

    /**
     * Associates the specified value with the specified key in this tree.
     * @param {number} key - the key to be put to the tree.
     * @param {number} value - the value to be put to the tree.
     * @returns void
     */
    put(key, value=0) {
        this.root = this.#put(this.root, key, value);
    }

    /**
     * Removes the mapping for this key from this tree if present.
     * @param {number} key - the key to be removed from the tree.
     * @returns void
     */
    remove(key) {
        this.root = this.#remove(this.root, key);
    }

    /**
     * @returns a string representation of this tree.
     */
    toString() {
        return "{" + this.#traverse().map(x => `${x.key}: ${x.value}`).join(", ") + "}";
    }

    /**
     * @private
     * @returns the subtree node associated with the least key (null if empty).
     */
    #firstEntry(node) {
        while (node && node.left) node = node.left;
        return node;
    }

    /**
     * @private
     * @param {TreeNode} node - the subtree where the search happens.
     * @param {number} key - the key to which the value is to be found.
     * @returns the value to which the specified key is mapped, or null if this
     *          subtree contains no mapping for the key.
     */
    #get(node, key) {
        if (!node) return null;
        if (node.key === key) return node.value;
        if (node.key < key) return this.#get(node.right, key);
        return this.#get(node.left, key);
    }

    /**
     * @private
     * @param {TreeNode} node - the tree node for left rotation.
     * @returns the tree node after left rotation.
     */
    #left_rotate(node) {
        let y = node.right, T2 = y.left;
        y.left = node;
        node.right = T2;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        y.height = 1 + Math.max(this.height(y.left), this.height(y.right));
        return y;
    }

    /**
     * @private
     * @param {TreeNode} node - the subtree to which the key-value pair is to be inserted.
     * @param {number} key - the key to be inserted.
     * @param {number} value - the value to be inserted.
     * @returns the tree node after the key-value pair is inserted into the subtree.
     */
    #put(node, key, value) {
        if (!node) {
            ++this.size;
            return new TreeNode(key, value);
        } else if (key < node.key) node.left = this.#put(node.left, key, value);
        else if (key > node.key) node.right = this.#put(node.right, key, value);
        else {
            node.value = value;
            return node;
        }
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        let bal = this.balance(node);
        if (bal > 1 && key < node.left.key)
            return this.#right_rotate(node);
        if (bal < -1 && key > node.right.key)
            return this.#left_rotate(node);
        if (bal > 1 && key > node.left.key) {
            node.left = this.#left_rotate(node.left);
            return this.#right_rotate(node);
        }
        if (bal < -1 && key < node.right.key) {
            node.right = this.#right_rotate(node.right);
            return this.#left_rotate(node);
        }
        return node;
    }

    /**
     * @private
     * @param {TreeNode} node - the subtree to remove the key.
     * @param {number} key - the key to be removed from the subtree.
     * @return tree node after given key is removed.
     */
    #remove(node, key) {
        if (!node) return node;
        if (key < node.key) node.left = this.#remove(node.left, key);
        else if (key > node.key) node.right = this.#remove(node.right, key);
        else {
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
            let temp = this.#firstEntry(node.right);
            node.key = temp.key;
            node.value = temp.value;
            node.right = this.#remove(node.right, temp.key);
        }
        if (!node) return node;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        let bal = this.balance(node);
        if (bal > 1 && this.balance(node.left) > 0)
            return this.#right_rotate(node);
        if (bal < -1 && this.balance(node.right) < 0)
            return this.#left_rotate(node);
        if (bal > 1 && this.balance(node.left) < 0) {
            node.left = this.#left_rotate(node.left);
            return this.#right_rotate(node);
        }
        if (bal < -1 && this.balance(node.right) > 0) {
            node.right = this.#right_rotate(node.right);
            return this.#left_rotate(node);
        }
        return node;
    }

    /**
     * @private
     * @param {TreeNode} node - the tree node for right rotation.
     * @returns the tree node after right rotation.
     */
    #right_rotate(node) {
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


if (typeof require !== 'undefined' && require.main === module) {
    const keys = [];
    const tree = new AVLTree();
    for (let i = 0; i < 1000; ++i) {
        const k = Math.floor(Math.random()*1000);
        const v = Math.floor(Math.random()*1000);
        keys.push(k);
        tree.put(k, v);
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

    const result = tree.get(30);
    if (result) console.log("Node found");
    else console.log("Node not found");

    for (const k of keys)
        tree.remove(k);
    console.log("Tree size is ", tree.size);
    console.log("Tree after deletion:");
    traverse(tree.root);
}
