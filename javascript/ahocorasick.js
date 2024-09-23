class AhoCorasick {
    constructor() {
        this.root = {
            output: null,
            parent: null,
            suffix: null
        };
    }

    build(patterns) {
        for (const pattern of patterns) {
            let node = this.root;
            for (const ch of pattern) {
                if (!(ch in node))
                    node[ch] = {
                        output: null,
                        parent: node,
                        suffix: null
                    }
                node = node[ch];
            }
            node["$"] = pattern
        }
        const queue = [this.root]
        const forbidden = new Set(["parent", "output", "suffix", "$"])
        while (queue.length)
            for (let sz = queue.length; sz; --sz) {
                let node = queue.shift();
                for (const [ch, child] of Object.entries(node))
                    if (!forbidden.has(ch)) {
                        let suffix = node["suffix"];
                        while (suffix && !(ch in suffix)) suffix = suffix["suffix"];
                        if (suffix) {
                            child["suffix"] = suffix[ch];
                            if ("$" in child["suffix"]) child["output"] = child["suffix"];
                            else child["output"] = child["suffix"];
                        } else {
                            child["output"] = null;
                            child["suffix"] = this.root;
                        }
                        queue.push(child);
                    }
            }
    }

    match(text) {
        const ans = {};
        let node = this.root;
        for (const [i, ch] of text.split('').entries()) {
            while (!(ch in node) && node["suffix"]) node = node["suffix"];
            if (ch in node) node = node[ch];
            for (let output = node; output; output = output["output"])
                if ("$" in output) {
                    const pattern = output["$"];
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
