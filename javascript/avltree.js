class TreeNode {
    constructor(key, value, left=null, right=null, height=1) {
        this.key = key;
        this.value = value;
        this.left = left;
        this.right = right;
        this.height = height;
    }
}


class AVLTree {
    /*The AVL tree, named after its inventors Georgy Adelson-Velsky and
    Evgenii Landis, in their 1962 paper “An algorithm for the organization of
    information”, is a self-balancing Binary Search Tree (BST) where the
    difference between heights of left and right subtrees for any node cannot be
    more than one.*/
    constructor(root=null) {
        this.root = root;
        this.size = 0;
    }

    balance(node) {
        if (!node) return 0;
        return this.height(node.left) - this.height(node.right);
    }

    delete(key) {
        this.root = this.#delete(this.root, key);
    }

    height(node) {
        if (!node) return 0;
        return node.height;
    }

    insert(key, value=0) {
        this.root = this.#insert(this.root, key, value);
    }

    search(key) {
        return this.#search(this.root, key);
    }

    #delete(node, key) {
        if (!node) return node;
        if (key < node.key) node.left = this.#delete(node.left, key);
        else if (key > node.key) node.right = this.#delete(node.right, key);
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
            let temp = this.minimum(node.right);
            node.key = temp.key;
            node.right = this.#delete(node.right, temp.key);
        }
        if (!node) return node;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        let bal = this.balance(node);
        if (bal > 1 && this.balance(node.left) > 0)
            return this.right_rotate(node);
        if (bal < -1 && this.balance(node.right) < 0)
            return this.left_rotate(node);
        if (bal > 1 && this.balance(node.left) < 0) {
            node.left = this.left_rotate(node.left);
            return this.right_rotate(node);
        }
        if (bal < -1 && this.balance(node.right) > 0) {
            node.right = this.right_rotate(node.right);
            return this.left_rotate(node);
        }
        return node;
    }

    #insert(node, key, value) {
        if (!node) {
            ++this.size;
            return new TreeNode(key, value);
        } else if (key < node.key) node.left = this.#insert(node.left, key, value);
        else if (key > node.key) node.right = this.#insert(node.right, key, value);
        else {
            node.value = value;
            return node;
        }
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        let bal = this.balance(node);
        if (bal > 1 && key < node.left.key)
            return this.right_rotate(node);
        if (bal < -1 && key > node.right.key)
            return this.left_rotate(node);
        if (bal > 1 && key > node.left.key) {
            node.left = this.left_rotate(node.left);
            return this.right_rotate(node);
        }
        if (bal < -1 && key < node.right.key) {
            node.right = this.right_rotate(node.right);
            return this.left_rotate(node);
        }
        return node;
    }

    #search(node, key) {
        if (!node || node.key === key) return node;
        if (node.key < key) return this.#search(node.right, key);
        return this.#search(node.left, key);
    }

    left_rotate(node) {
        let y = node.right, T2 = y.left;
        y.left = node;
        node.right = T2;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        y.height = 1 + Math.max(this.height(y.left), this.height(y.right));
        return y;
    }

    right_rotate(node) {
        let y = node.left, T3 = y.right;
        y.right = node;
        node.left = T3;
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
        y.height = 1 + Math.max(this.height(y.left), this.height(y.right));
        return y;
    }

    minimum(node) {
        while (node && node.left) node = node.left;
        return node;
    }
}

if (typeof require !== 'undefined' && require.main === module) {
    const keys = [];
    const tree = new AVLTree();
    for (let i = 0; i < 1000; ++i) {
        const k = Math.floor(Math.random()*1000);
        const v = Math.floor(Math.random()*1000);
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
