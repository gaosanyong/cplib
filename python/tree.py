class TreeNode:
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BalancedTree:
    """A self-balancing binary search tree (BST) is any node-based binary search
    tree that automatically keeps its height (maximal number of levels below the
    root) small in the face of arbitrary item insertions and deletions. These
    operations when designed for a self-balancing binary search tree, contain
    precautionary measures against boundlessly increasing tree height, so that
    these abstract data structures receive the attribute "self-balancing"."""
    def __init__(self):
        self.root = self.nil = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + ", ".join(map(lambda x: str(x.key), self._traverse())) + "}"

    def ceiling(self, key):
        ans = None
        node = self.root
        while node != self.nil:
            if key <= node.key:
                ans = node
                node = node.left
            else: node = node.right
        return ans

    def floor(self, key):
        ans = None
        node = self.root
        while node != self.nil:
            if key < node.key: node = node.left
            else:
                ans = node
                node = node.right
        return ans

    def maximum(self):
        return self._maximum(self, self.root)

    def minimum(self):
        return self._minimum(self, self.root)

    def search(self, key):
        node = self.root
        while node and key != node.key:
            if key < node.key: node = node.left
            else: node = node.right
        return node

    def _maximum(self, node):
        while node != self.nil and node.right: node = node.right
        return node

    def _minimum(self, node):
        while node != self.nil and node.left: node = node.left
        return node

    def _traverse(self):
        ans = []
        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node)
                node = node.right
        return ans


class AVLTreeNode(TreeNode):
    def __init__(self, key, value=0, left=None, right=None, height=0):
        super().__init__(key, value, left, right)
        self.height = height

class AVLTree(BalancedTree):
    """The AVL tree, named after its inventors Georgy Adelson-Velsky and
    Evgenii Landis, in their 1962 paper “An algorithm for the organization of
    information”, is a self-balancing Binary Search Tree (BST) where the
    difference between heights of left and right subtrees for any node cannot be
    more than one."""
    def __init__(self):
        super().__init__()
        self.root = self.nil = None

    def balance(self, node):
        if node: return self.height(node.left) - self.height(node.right)
        return 0

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def height(self, node):
        if node: return node.height
        return 0

    def insert(self, key, value=0):
        self.root = self._insert(self.root, key, value)

    def _delete(self, node, key):
        if not node: return node
        if key < node.key: node.left = self._delete(node.left, key)
        elif key == node.key:
            if not node.left:
                temp = node.right
                node = None
                self.size -= 1
                return temp
            if not node.right:
                temp = node.left
                node = None
                self.size -= 1
                return temp
            temp = self._minimum(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        else: node.right = self._delete(node.right, key)
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            bal = self.balance(node)
            if bal > 1 and self.balance(node.left) > 0:
                return self.rightRotate(node)
            if bal < -1 and self.balance(node.right) < 0:
                return self.leftRotate(node)
            if bal > 1 and self.balance(node.left) < 0:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
            if bal < -1 and self.balance(node.right) > 0:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        return node

    def _insert(self, node, key, value):
        if not node:
            self.size += 1
            return AVLTreeNode(key, value)
        elif key < node.key: node.left = self._insert(node.left, key, value)
        elif key == node.key:
            node.value = value
            return node
        else: node.right = self._insert(node.right, key, value)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)
        if bal > 1 and key < node.left.key:
            return self.rightRotate(node)
        if bal < -1 and key > node.right.key:
            return self.leftRotate(node)
        if bal > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if bal < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def leftRotate(self, node):
        y = node.right
        T2 = y.left
        y.left = node
        node.right = T2
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def rightRotate(self, node):
        y = node.left
        T3 = y.right
        y.right = node
        node.left = T3
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y


if __name__ == "__main__":
    from random import randint
    keys = []
    tree = AVLTree()
    for _ in range(1000):
        k = randint(0, 1000)
        v = randint(0, 1000)
        keys.append(k)
        tree.insert(k, v)

    print("Tree after insertion:")
    print(tree)
    print("")
    print("Tree size is ", len(tree))
    print("Tree height is ", tree.height(tree.root))

    result = tree.search(30)
    if result: print("Node found")
    else: print("Node not found")

    for k in keys: tree.delete(k)
    print("Tree size is ", len(tree))
    print("Tree after deletion:")
    print(tree)
