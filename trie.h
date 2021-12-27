struct TrieNode {
    TrieNode* children[26] = {nullptr};
    bool is_word = false;
    
    ~TrieNode() { for (auto& node : children) delete node; }
};


class Trie {
public: 
    TrieNode* root = nullptr; 

    Trie() { root = new TrieNode(); }

    ~Trie() { delete root; }

    void insert(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            if (!node->children[ch-'a']) node->children[ch-'a'] = new TrieNode(); 
            node = node->children[ch-'a'];
        }
        node->is_word = true; 
    }

    bool prefix(string word) {
        TrieNode* node = root; 
        for (auto& ch : word) {
            node = node->children[ch-'a']; 
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