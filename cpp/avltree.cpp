#include <algorithm>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

class TreeNode {
public:
    int key, value, height;
    TreeNode *left, *right;

    TreeNode(int key, int value): key(key), value(value) {
        left = right = nullptr;
        height = 1;
    }
};


class AVLTree {
public:
    TreeNode* root = nullptr;
    int sz = 0;

    void erase(int key) {
        root = erase(root, key);
    }

    void insert(int key, int value) {
        root = insert(root, key, value);
    }

    TreeNode* find(int key) {
        return find(root, key);
    }

    int balance(TreeNode* node) {
        if (!node) return 0;
        return height(node->left) - height(node->right);
    }

    int height(TreeNode* node) {
        if (!node) return 0;
        return node->height;
    }

    int size() {
        return sz;
    }

private:
    TreeNode* erase(TreeNode* node, int key) {
        if (!node) return node;
        if (key < node->key) node->left = erase(node->left, key);
        else if (key > node->key) node->right = erase(node->right, key);
        else {
            if (!node->left || !node->right) {
                TreeNode* temp = node->left ? node->left : node->right;
                delete node;
                node = nullptr;
                --sz;
                return temp;
            }
            TreeNode* temp = minimum(node->right);
            node->key = temp->key;
            node->right = erase(node->right, temp->key);
        }
        if (!node) return node;
        node->height = 1 + max(height(node->left), height(node->right));
        int bal = balance(node);
        if (bal > 1 && balance(node->left) > 0)
            return right_rotate(node);
        if (bal < -1 && balance(node->right) < 0)
            return left_rotate(node);
        if (bal > 1 && balance(node->left) < 0) {
            node->left = left_rotate(node->left);
            return right_rotate(node);
        }
        if (bal < -1 && balance(node->right) > 0) {
            node->right = right_rotate(node->right);
            return left_rotate(node);
        }
        return node;
    }

    TreeNode* insert(TreeNode* node, int key, int value) {
        if (!node) {
            ++sz;
            return new TreeNode(key, value);
        } else if (key < node->key) node->left = insert(node->left, key, value);
        else if (key > node->key) node->right = insert(node->right, key, value);
        else {
            node->value = value;
            return node;
        }
        node->height = 1 + max(height(node->left), height(node->right));
        int bal = balance(node);
        if (bal > 1 && key < node->left->key)
            return right_rotate(node);
        if (bal < -1 && key > node->right->key)
            return left_rotate(node);
        if (bal > 1 && key > node->left->key) {
            node->left = left_rotate(node->left);
            return right_rotate(node);
        }
        if (bal < -1 && key < node->right->key) {
            node->right = right_rotate(node->right);
            return left_rotate(node);
        }
        return node;
    }

    TreeNode* find(TreeNode* node, int key) {
        if (!node || node->key == key) return node;
        if (node->key < key) return find(node->right, key);
        return find(node->left, key);
    }

    TreeNode* left_rotate(TreeNode* node) {
        TreeNode *y = node->right, *T2 = y->left;
        y->left = node;
        node->right = T2;
        node->height = 1 + max(height(node->left), height(node->right));
        y->height = 1 + max(height(y->left), height(y->right));
        return y;
    }

    TreeNode* right_rotate(TreeNode* node) {
        TreeNode *y = node->left, *T3 = y->right;
        y->right = node;
        node->left = T3;
        node->height = 1 + max(height(node->left), height(node->right));
        y->height = 1 + max(height(y->left), height(y->right));
        return y;
    }

    TreeNode* minimum(TreeNode* node) {
        while (node && node->left) node = node->left;
        return node;
    }
};


int main(int argc, char *argv[]) {
    vector<int> keys;
    AVLTree* tree = new AVLTree();
    for (int i = 0; i < 1000; ++i) {
        int k = rand() % 1001;
        int v = rand() % 1001;
        keys.push_back(k);
        tree->insert(k, v);
    }

    function<void(TreeNode* node)> traverse = [&](TreeNode* node) {
        if (node) {
            traverse(node->left);
            cout << node->key << " ";
            traverse(node->right);
        }
    };

    cout << "Tree after insertion:" <<endl;
    traverse(tree->root);
    cout << " " << endl;
    cout << "Tree size is " << tree->size() << endl;
    cout << "Tree height is " << tree->height(tree->root) << endl;

    TreeNode* result = tree->find(30);
    if (result) cout << "Node found" << endl;
    else cout << "Node not found" << endl;

    for (auto& k : keys)
        tree->erase(k);
    cout << "Tree size is " << tree->size() << endl;
    cout << "Tree after deletion:" << endl;
    traverse(tree->root);
}
