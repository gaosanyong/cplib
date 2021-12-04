struct TrieNode {
    TrieNode* child[26] = {nullptr};
    bool is_word = false;
    
    ~TrieNode() {
        for (auto& node : child) delete node; 
    }
};


class Trie {
    TrieNode* root; 
public: 
    Trie() { root = new TrieNode(); }

    ~Trie() { delete root; }

    void insert(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            if (!node->child[ch - 'a']) node->child[ch - 'a'] = new TrieNode(); 
            node = node->child[ch - 'a'];
        }
        node->is_word = true; 
    }

    bool prefix(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            node = node->child[ch - 'a']; 
            if (!node) return false; 
        }
        return true; 
    }

    bool search(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            node = node->children[ch - 'a']; 
            if (!node) return false; 
        }
        return node->is_word; 
    }
}