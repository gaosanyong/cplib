class TrieNode {
    TrieNode[] child = new TrieNode[26]; 
    String word; 
}

public class Trie {
    public TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (var ch : word.toCharArray()) {
            int c = ch - 'a';
            if (node.child[c] == null)
                node.child[c] = new TrieNode();
            node = node.child[c];
        }
        node.word = word;
    }

    public boolean prefix(String word) {
        TrieNode node = root;
        for (var ch : word.toCharArray()) {
            int c = ch - 'a';
            if (node.child[c] == null) return false;
            node = node.child[c];
        }
        return true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (var ch : word.toCharArray()) {
            int c = ch - 'a';
            if (node.child[c] == null) return false;
            node = node.child[c];
        }
        return node.word != null;
    }
}
