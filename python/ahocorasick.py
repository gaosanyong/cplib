from collections import defaultdict, deque
from typing import List

class AhoCorasick:
    def __init__(self):
        self.root = {"output" : None, "parent" : None, "suffix" : None}

    def build(self, patterns: List[str]):
        for pattern in patterns:
            node = self.root
            for ch in pattern:
                if ch not in node: node[ch] = {"output" : None, "parent" : node, "suffix" : None}
                node = node[ch]
            node["$"] = pattern
        queue = deque([self.root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for ch, child in node.items():
                    if ch not in ("parent", "output", "suffix", "$"):
                        suffix = node["suffix"]
                        while suffix and ch not in suffix: suffix = suffix["suffix"]
                        if suffix:
                            child["suffix"] = suffix[ch]
                            if "$" in child["suffix"]: child["output"] = child["suffix"]
                            else: child["output"] = child["suffix"]["output"]
                        else:
                            child["output"] = None
                            child["suffix"] = self.root
                        queue.append(child)

    def match(self, text: str):
        ans = defaultdict(list)
        node = self.root
        for i, ch in enumerate(text):
            while ch not in node and node["suffix"]: node = node["suffix"]
            if ch in node: node = node[ch]
            if "$" in node:
                pattern = node["$"]
                ans[pattern].append(i-len(pattern)+1)
        return ans


if __name__ == "__main__":
    trie = AhoCorasick()
    trie.build(["abc", "aaaaa", "bcdef"])
    print(trie.match("aaaaaaabcdef"))
