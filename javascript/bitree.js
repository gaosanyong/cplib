/**
 * @author Ye Gao
 * @description Binary tree traversal.
 * @license MIT License
 * @name bitree.js
 * @see {@link https://github.com/gaosanyong/cplib} for further information.
 * @version 0.0.1
 */

class TreeNode {
    constructor(value, left=null, right=null) {
        this.val = value; 
        this.left = left; 
        this.right = right; 
    }
}

/**
 * Traverse binary tree in breadth-first order.
 * @param {TreeNode} root, root of the binary tree
 * @return {Array} array of tree nodes.
 */
function bfs(root) {
    const ans = [];
    const queue = [root];
    while (queue.length) {
        const node = queue.shift();
        if (node) {
            ans.push(node);
            queue.push(node.left);
            queue.push(node.right);
        }
    }
    return ans;
}

/**
 * Traverse binary tree in pre-order.
 * @param {TreeNode} root, root of the binary tree
 * @return {Array} array of tree nodes.
 */
function preorder(root) {
    const ans = [], stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (node) {
            ans.push(node);
            stack.push(node.right);
            stack.push(node.left);
        }
    }
    return ans;
}

/**
 * Traverse binary tree in in-order.
 * @param {TreeNode} root, root of the binary tree
 * @return {Array} array of tree nodes.
 */
function inorder(root) {
    const ans = [], stack = [];
    let node = root;
    while (node || stack.length)
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

/**
 * Traverse binary tree in post-order.
 * @param {TreeNode} root, root of the binary tree
 * @return {Array} array of tree nodes.
 */
function postorder(root) {
    const ans = [], stack = [];
    let node = root, prev = null;
    while (node || stack.length)
        if (node) {
            stack.push(node);
            node = node.left;
        } else {
            node = stack[stack.length-1];
            if (node.right && node.right != prev) node = node.right;
            else {
                ans.push(node);
                stack.pop();
                prev = node;
                node = null;
            }
        }
    return ans;
}

