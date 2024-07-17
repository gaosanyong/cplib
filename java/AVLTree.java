import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Stack;

class TreeNode {
    public int key, value, height;
    public TreeNode left, right;

    public TreeNode(int key, int value) {
        this.key = key;
        this.value = value;
        this.left = null;
        this.right = null;
        this.height = 1;
    }
}


public class AVLTree {
    public TreeNode root = null;
    public int sz = 0;

    public void delete(int key) {
        root = delete(root, key);
    }

    public void insert(int key, int value) {
        root = insert(root, key, value);
    }

    public TreeNode search(int key) {
        return search(root, key);
    }

    public int balance(TreeNode node) {
        if (node == null) return 0;
        return height(node.left) - height(node.right);
    }

    public int height(TreeNode node) {
        if (node == null) return 0;
        return node.height;
    }

    public int size() {
        return sz;
    }

    private TreeNode delete(TreeNode node, int key) {
        if (node == null) return node;
        if (key < node.key) node.left = delete(node.left, key);
        else if (key > node.key) node.right = delete(node.right, key);
        else {
            if (node.left == null) {
                TreeNode temp = node.right;
                node = null;
                --sz;
                return temp;
            }
            if (node.right == null) {
                TreeNode temp = node.left;
                node = null;
                --sz;
                return temp;
            }
            TreeNode temp = minimum(node.right);
            node.key = temp.key;
            node.right = delete(node.right, temp.key);
        }
        if (node == null) return node;
        node.height = 1 + Math.max(height(node.left), height(node.right));
        int bal = balance(node);
        if (bal > 1 && balance(node.left) > 0)
            return right_rotate(node);
        if (bal < -1 && balance(node.right) < 0)
            return left_rotate(node);
        if (bal > 1 && balance(node.left) < 0) {
            node.left = left_rotate(node.left);
            return right_rotate(node);
        }
        if (bal < -1 && balance(node.right) > 0) {
            node.right = right_rotate(node.right);
            return left_rotate(node);
        }
        return node;
    }

    private TreeNode insert(TreeNode node, int key, int value) {
        if (node == null) {
            ++sz;
            return new TreeNode(key, value);
        } else if (key < node.key) node.left = insert(node.left, key, value);
        else if (key > node.key) node.right = insert(node.right, key, value);
        else {
            node.value = value;
            return node;
        }
        node.height = 1 + Math.max(height(node.left), height(node.right));
        int bal = balance(node);
        if (bal > 1 && key < node.left.key)
            return right_rotate(node);
        if (bal < -1 && key > node.right.key)
            return left_rotate(node);
        if (bal > 1 && key > node.left.key) {
            node.left = left_rotate(node.left);
            return right_rotate(node);
        }
        if (bal < -1 && key < node.right.key) {
            node.right = right_rotate(node.right);
            return left_rotate(node);
        }
        return node;
    }

    private TreeNode search(TreeNode node, int key) {
        if (node == null || node.key == key) return node;
        if (node.key < key) return search(node.right, key);
        return search(node.left, key);
    }

    private TreeNode left_rotate(TreeNode node) {
        TreeNode y = node.right, T2 = y.left;
        y.left = node;
        node.right = T2;
        node.height = 1 + Math.max(height(node.left), height(node.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));
        return y;
    }

    private TreeNode right_rotate(TreeNode node) {
        TreeNode y = node.left, T3 = y.right;
        y.right = node;
        node.left = T3;
        node.height = 1 + Math.max(height(node.left), height(node.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));
        return y;
    }

    private TreeNode minimum(TreeNode node) {
        while (node != null && node.left != null) node = node.left;
        return node;
    }

    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        Random rand = new Random();
        List<Integer> keys = new ArrayList();
        for (int i = 0; i < 1000; ++i) {
            int k = rand.nextInt(1000);
            int v = rand.nextInt(1000);
            keys.add(k);
            tree.insert(k, v);
        }
        System.out.println("Tree after insertion: ");
        tree.traverse(tree.root);
        System.out.println("");
        System.out.println("Tree size is " + tree.size());
        System.out.println("Tree height is " + tree.height(tree.root));

        TreeNode result = tree.search(30);
        if (result != null)
            System.out.println("Node found");
        else
            System.out.println("Node not found");

        for (int k : keys)
            tree.delete(k);
        System.out.println("Tree size is " + tree.size());
        System.out.println("Tree after deletion: ");
        tree.traverse(tree.root);
    }

    private static void traverse(TreeNode node) {
        if (node != null) {
            traverse(node.left);
            System.out.print(node.key + " ");
            traverse(node.right);
        }
    }
}
