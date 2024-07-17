class TreeNode:
    def __init__(self, key, value=0, left=None, right=None, height=1):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.height = height


class AVLTree:
    """The AVL tree, named after its inventors Georgy Adelson-Velsky and
    Evgenii Landis, in their 1962 paper “An algorithm for the organization of
    information”, is a self-balancing Binary Search Tree (BST) where the
    difference between heights of left and right subtrees for any node cannot be
    more than one."""
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def balance(self, node):
        if not node: return 0
        return self.height(node.left) - self.height(node.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def height(self, node):
        if not node: return 0
        return node.height

    def insert(self, key, value=0):
        self.root = self._insert(self.root, key, value)

    def search(self, key):
        return self._search(self.root, key)

    def _delete(self, node, key):
        if not node: return node
        if key < node.key: node.left = self._delete(node.left, key)
        elif key > node.key: node.right = self._delete(node.right, key)
        else:
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
            temp = self.minimum(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        if not node: return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)
        if bal > 1 and self.balance(node.left) > 0:
            return self.right_rotate(node)
        if bal < -1 and self.balance(node.right) < 0:
            return self.left_rotate(node)
        if bal > 1 and self.balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if bal < -1 and self.balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def _insert(self, node, key, value):
        if not node:
            self.size += 1
            return TreeNode(key, value)
        elif key < node.key: node.left = self._insert(node.left, key, value)
        elif key > node.key: node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)
        if bal > 1 and key < node.left.key:
            return self.right_rotate(node)
        if bal < -1 and key > node.right.key:
            return self.left_rotate(node)
        if bal > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if bal < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def _search(self, node, key):
        if not node or node.key == key: return node
        if node.key < key:
            return self._search(node.right, key)
        return self._search(node.left, key)

    def left_rotate(self, node):
        y = node.right
        T2 = y.left
        y.left = node
        node.right = T2
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def right_rotate(self, node):
        y = node.left
        T3 = y.right
        y.right = node
        node.left = T3
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def minimum(self, node):
        while node and node.left: node = node.left
        return node


if __name__ == "__main__":
    from random import randint
    keys = []
    tree = AVLTree()
    for _ in range(1000):
        k = randint(0, 1000)
        v = randint(0, 1000)
        keys.append(k)
        tree.insert(k, v)

    def traverse(node):
        if node:
            traverse(node.left)
            print(node.key, end=" ")
            traverse(node.right)

    print("Tree after insertion:")
    traverse(tree.root)
    print("")
    print("Tree size is ", len(tree))
    print("Tree height is ", tree.height(tree.root))

    result = tree.search(30)
    if result: print("Node found")
    else: print("Node not found")

    for k in keys:
        tree.delete(k)
    print("Tree size is ", len(tree))
    print("Tree after deletion:")
    traverse(tree.root)
