import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Stack;

class TreeNode<K, V> {
    public K key;
    public V value;
    public int height;
    public TreeNode<K, V> left, right;

    public TreeNode(K key, V value) {
        this.key = key;
        this.value = value;
        this.left = null;
        this.right = null;
        this.height = 1;
    }

    public K getKey() {
        return key;
    }

    public V getValue() {
        return value;
    }
}


public class AVLTree<K extends Comparable<K>, V> {
    public TreeNode<K, V> root = null;
    public int sz = 0;

    public int balance(TreeNode<K, V> node) {
        if (node == null) return 0;
        return height(node.left) - height(node.right);
    }

    public boolean isEmpty() {
        return sz == 0;
    }

    public TreeNode<K, V> ceilingEntry(K key) {
        TreeNode<K, V> ans = null;
        for (TreeNode<K, V> node = root; node != null; )
            if (node.key.compareTo(key) < 0) node = node.right;
            else {
                ans = node;
                node = node.left;
            }
        return ans;
    }

    public K ceilingKey(K key) {
        TreeNode<K, V> node = ceilingEntry(key);
        if (node == null) return null;
        return node.getKey();
    }

    public List<TreeNode<K, V>> entrySet() {
        return traverse();
    }

    public TreeNode<K, V> floorEntry(K key) {
        TreeNode<K, V> ans = null;
        for (TreeNode<K, V> node = root; node != null; )
            if (key.compareTo(node.key) < 0) node = node.left;
            else {
                ans = node;
                node = node.right;
            }
        return ans;
    }

    public TreeNode<K, V> firstEntry() {
        return firstEntry(root);
    }

    public K firstKey() {
        TreeNode<K, V> node = firstEntry();
        if (node == null) return null;
        return node.getKey();
    }

    public V get(K key) {
        TreeNode<K, V> node = get(root, key);
        if (node == null) return null;
        return node.getValue();
    }

    public int height(TreeNode<K, V> node) {
        if (node == null) return 0;
        return node.height;
    }

    public void put(K key, V value) {
        root = put(root, key, value);
    }

    public void remove(K key) {
        root = remove(root, key);
    }

    public int size() {
        return sz;
    }

    private TreeNode<K, V> firstEntry(TreeNode<K, V> node) {
        while (node != null && node.left != null) node = node.left;
        return node;
    }

    private TreeNode<K, V> get(TreeNode<K, V> node, K key) {
        if (node == null || node.key == key) return node;
        if (node.key.compareTo(key) < 0) return get(node.right, key);
        return get(node.left, key);
    }

    private TreeNode<K, V> left_rotate(TreeNode<K, V> node) {
        TreeNode<K, V> y = node.right, T2 = y.left;
        y.left = node;
        node.right = T2;
        node.height = 1 + Math.max(height(node.left), height(node.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));
        return y;
    }

    private TreeNode<K, V> put(TreeNode<K, V> node, K key, V value) {
        if (node == null) {
            ++sz;
            return new TreeNode<K, V>(key, value);
        } else if (key.compareTo(node.key) < 0) node.left = put(node.left, key, value);
        else if (node.key.compareTo(key) < 0) node.right = put(node.right, key, value);
        else {
            node.value = value;
            return node;
        }
        node.height = 1 + Math.max(height(node.left), height(node.right));
        int bal = balance(node);
        if (bal > 1 && key.compareTo(node.left.key) < 0)
            return right_rotate(node);
        if (bal < -1 && node.right.key.compareTo(key) < 0)
            return left_rotate(node);
        if (bal > 1 && node.left.key.compareTo(key) < 0) {
            node.left = left_rotate(node.left);
            return right_rotate(node);
        }
        if (bal < -1 && key.compareTo(node.right.key) < 0) {
            node.right = right_rotate(node.right);
            return left_rotate(node);
        }
        return node;
    }

    private TreeNode<K, V> remove(TreeNode<K, V> node, K key) {
        if (node == null) return node;
        if (key.compareTo(node.key) < 0) node.left = remove(node.left, key);
        else if (node.key.compareTo(key) < 0) node.right = remove(node.right, key);
        else {
            if (node.left == null) {
                TreeNode<K, V> temp = node.right;
                node = null;
                --sz;
                return temp;
            }
            if (node.right == null) {
                TreeNode<K, V> temp = node.left;
                node = null;
                --sz;
                return temp;
            }
            TreeNode<K, V> temp = firstEntry(node.right);
            node.key = temp.key;
            node.value = temp.value;
            node.right = remove(node.right, temp.key);
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

    private TreeNode<K, V> right_rotate(TreeNode<K, V> node) {
        TreeNode<K, V> y = node.left, T3 = y.right;
        y.right = node;
        node.left = T3;
        node.height = 1 + Math.max(height(node.left), height(node.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));
        return y;
    }

    private List<TreeNode<K, V>> traverse() {
        List<TreeNode<K, V>> ans = new ArrayList<>();
        Stack<TreeNode<K, V>> stk = new Stack<>();
        TreeNode<K, V> node = root;
        while (!stk.isEmpty() || node != null)
            if (node != null) {
                stk.push(node);
                node = node.left;
            } else {
                node = stk.pop();
                ans.add(node);
                node = node.right;
            }
        return ans;
    }

    public static void main(String[] args) {
        AVLTree<Integer, Integer> tree = new AVLTree<>();
        Random rand = new Random();
        List<Integer> keys = new ArrayList<>();
        for (int i = 0; i < 1000; ++i) {
            int k = rand.nextInt(1000);
            int v = rand.nextInt(1000);
            keys.add(k);
            tree.put(k, v);
        }
        System.out.println("Tree after insertion: ");
        tree.traverse(tree.root);
        System.out.println("");
        System.out.println("Tree size is " + tree.size());
        System.out.println("Tree height is " + tree.height(tree.root));

        Integer result = tree.get(30);
        if (result != null)
            System.out.println("Node found");
        else
            System.out.println("Node not found");

        for (int k : keys)
            tree.remove(k);
        System.out.println("Tree size is " + tree.size());
        System.out.println("Tree after deletion: ");
        tree.traverse(tree.root);
    }

    private static void traverse(TreeNode<Integer, Integer> node) {
        if (node != null) {
            traverse(node.left);
            System.out.print(node.key + " ");
            traverse(node.right);
        }
    }
}
