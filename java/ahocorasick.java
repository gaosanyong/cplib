import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Random;
import java.util.Stack;

class TrieNode {
    public TrieNode[] child = new TrieNode[26];
    public TrieNode output = null;
    public TrieNode parent = null;
    public TrieNode suffix = null;
    public String word;
}


public class AhoCorasick {
    public TrieNode root = new TrieNode();

    public void build(String[] patterns) {
        for (var pattern : patterns) {
            TrieNode node = root;
            for (var ch : pattern.toCharArray()) {
                int c = (int) (ch - 'a');
                if (node.child[c] == null) {
                    node.child[c] = new TrieNode();
                    node.child[c].parent = node;
                }
                node = node.child[c];
            }
            node.word = pattern;
        }
        Queue<TrieNode> q = new LinkedList<>(); q.add(root);
        while (!q.isEmpty())
            for (int sz = q.size(); sz > 0; --sz) {
                TrieNode node = q.poll();
                for (int i = 0; i < 26; ++i) {
                    TrieNode child = node.child[i], suffix = node.suffix;
                    if (child != null) {
                        while (suffix != null && suffix.child[i] == null)
                            suffix = suffix.suffix;
                        if (suffix != null) {
                            child.suffix = suffix.child[i];
                            if (child.suffix.word != null) child.output =child.suffix;
                            else child.output = child.suffix.output;
                        } else {
                            child.output = null;
                            child.suffix = root;
                        }
                        q.add(child);
                    }
                }
            }
    }

    public Map<String, List<Integer>> match(String text) {
        Map<String, List<Integer>> ans = new HashMap<>();
        TrieNode node = root;
        for (int i = 0; i < text.length(); ++i) {
            char ch = text.charAt(i);
            int c = (int) (ch - 'a');
            while (node.child[c] == null && node.suffix != null)
                node = node.suffix;
            if (node.child[c] != null) node = node.child[c];
            for (TrieNode output = node; output != null; output = output.output)
                if (output.word != null) {
                    String pattern = output.word;
                    if (!ans.containsKey(pattern))
                        ans.put(pattern, new ArrayList<>());
                    ans.get(pattern).add(i-pattern.length()+1);
                }
        }
        return ans;
    }

    public static void main(String[] args) {
        AhoCorasick trie = new AhoCorasick();
        List<String> words = new ArrayList<>(Arrays.asList("abc", "aaaaa", "bcdef"));
        trie.build(words);
        Map<String, List<Integer>> ans = trie.match("aaaaaaabcdef");
        for (var k : ans.keySet()) {
            System.out.print(k + " : ");
            for (var v : ans.get(k))
                System.out.print(v + " ");
            System.out.println();
        }
    }
}
