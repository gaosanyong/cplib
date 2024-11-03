"""
NAME
    trie - trie data structure 

DESCRIPTION 
    This module implements a trie data structure via nested dictionaries. 

    * Trie  trie class for storing and searching strings

CLASSES
    class Trie()
     |   Return a trie instance
     |
     |   Methods defined here: 
     |
     |   insert(self, word) 
     |       insert word into trie 
     |
     |   search(self, word)
     |       Return True if word is found on the trie 
     |
     |   prefix(self, word)
     |       Return True if prefix is found on the trie
"""

class Trie:
    """Trie implemented as nested dictionaries."""

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        """Insert the word onto the trie"""
        node = self.root
        for ch in word: node = node.setdefault(ch, {})
        node['$'] = word

    def prefix(self, word: str) -> bool: 
        """Return True if prefix is found on the trie"""
        node = self.root 
        for ch in prefix: 
            if ch not in node: return False 
            node = node[ch] 
        return True 

    def search(self, word: str) -> bool:
        """Return True if word is found on the trie"""
        node = self.root
        for ch in word:
            if ch not in node: return False 
            node = node[ch]
        return '$' in node
