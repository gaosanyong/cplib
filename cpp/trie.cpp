#include <string>

using namespace std;

struct TrieNode {
    TrieNode* child[26] = {nullptr};
    string word;
    ~TrieNode() { for (auto& node : child) delete node; }
};

class Trie {
public: 
    TrieNode* root = nullptr; 

    Trie() { root = new TrieNode(); }

    ~Trie() { delete root; }

    void insert(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            int c = ch - 'a';
            if (!node->child[c]) node->child[c] = new TrieNode();
            node = node->child[c];
        }
        node->word = word;
    }

    bool prefix(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            int c = ch - 'a';
            if (!node->child[c]) return false;
            node = node->child[c];
        }
        return true; 
    }

    bool search(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            int c = ch - 'a';
            if (!node->child[c]) return false;
            node = node->child[c];
        }
        return node->word != "";
    }
};
