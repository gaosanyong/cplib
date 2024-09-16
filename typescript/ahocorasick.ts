interface TrieNode {
    child : Record<string, TrieNode>,
    output: TrieNode | null,
    parent: TrieNode | null,
    suffix: TrieNode | null,
    word? : string
}


class AhoCorasick {
    public root: TrieNode;

    constructor() {
        this.root = {
            child : {},
            output: null,
            parent: null,
            suffix: null
        };
    }

    build(patterns: string[]) {
        for (const pattern of patterns) {
            let node = this.root;
            for (const ch of pattern) {
                if (!(ch in node.child))
                    node.child[ch] = {
                        child: {},
                        output: null,
                        parent: node,
                        suffix: null
                    }
                node = node.child[ch];
            }
            node.word = pattern
        }
        const queue: TrieNode[] = [this.root]
        while (queue.length)
            for (let sz = queue.length; sz; --sz) {
                let node = queue.shift();
                if (node) {
                    for (const [ch, child] of Object.entries(node.child)) {
                        let suffix = node.suffix;
                        while (suffix && !(ch in suffix.child)) suffix = suffix.suffix;
                        if (suffix) {
                            child.suffix = suffix.child[ch];
                            if (child.suffix.word) child.output = child.suffix;
                            else child.output = child.suffix;
                        } else {
                            child.output = null;
                            child.suffix = this.root;
                        }
                        queue.push(child);
                    }
                }
            }
    }

    match(text: string) {
        const ans: Record<string, number[]> = {};
        let node = this.root;
        for (const [i, ch] of text.split('').entries()) {
            while (!(ch in node.child) && node.suffix) node = node.suffix;
            if (ch in node.child) node = node.child[ch];
            if (node.word) {
                const pattern = node.word;
                if (!(pattern in ans)) ans[pattern] = [];
                ans[pattern].push(i-pattern.length+1);
            }
        }
        return ans;
    }
}


if (typeof require !== 'undefined' && require.main === module) {
    const trie = new AhoCorasick();
    trie.build(["abc", "aaaaa", "bcdef"]);
    console.log(trie.match("aaaaaaabcdef"));
}
