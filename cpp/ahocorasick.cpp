#include <iostream>
#include <ostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode *child[26] = {nullptr};
    TrieNode *output = nullptr;
    TrieNode *parent = nullptr;
    TrieNode *suffix = nullptr;
    string word;
    ~TrieNode() { for (auto& node : child) delete node; }
};


class AhoCorasick {
public:
    TrieNode *root = new TrieNode();

    ~AhoCorasick() { delete root; }

    void build(vector<string> patterns) {
        for (auto& pattern : patterns) {
            TrieNode *node = root;
            for (auto& ch : pattern) {
                int c = ch - 'a';
                if (!node->child[c]) {
                    node->child[c] = new TrieNode();
                    node->child[c]->parent = node;
                }
                node = node->child[c];
            }
            node->word = pattern;
        }
        queue<TrieNode*> q; q.push(root);
        while (q.size())
            for (int sz = q.size(); sz; --sz) {
                TrieNode *node = q.front(); q.pop();
                for (int i = 0; i < 26; ++i) {
                    TrieNode *child = node->child[i], *suffix = node->suffix;
                    if (child) {
                        while (suffix && suffix->child[i] == nullptr)
                            suffix = suffix->suffix;
                        if (suffix) {
                            child->suffix = suffix->child[i];
                            if (child->suffix->word != "") child->output = child->suffix;
                            else child->output =child->suffix->output;
                        } else {
                            child->output = nullptr;
                            child->suffix = root;
                        }
                        q.push(child);
                    }
                }
            }
    }

    unordered_map<string, vector<int>> match(string text) {
        unordered_map<string, vector<int>> ans;
        TrieNode *node = root;
        for (int i = 0; i < text.size(); ++i) {
            char ch = text[i];
            int c = ch - 'a';
            while (!node->child[c] && node->suffix) node = node->suffix;
            if (node->child[c]) node = node->child[c];
            for (TrieNode *output = node; output; output = output->output)
                if (!output->word.empty()) {
                    string pattern = output->word;
                    ans[pattern].push_back(i-pattern.size()+1);
                }
        }
        return ans;
    }
};


int main() {
    AhoCorasick *trie = new AhoCorasick();
    vector<string> words = {"abc", "aaaaa", "bcdef"};
    trie->build(words);
    unordered_map<string, vector<int>> ans = trie->match("aaaaaaabcdef");
    for (auto& [k, v] : ans) {
        cout << k << " : ";
        for (auto& x : v)
            cout << x << " ";
        cout << endl;
    }
    return 0;
}
