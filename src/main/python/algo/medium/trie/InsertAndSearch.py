from src.main.python.algo.medium.trie.model import Node


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, str):
        current = self.root
        for c in str:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.end = True

    def exist(self, str):
        current = self.root
        for c in str:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.end


trie = Trie()
trie.insert("sour")
trie.insert("sobh")
trie.insert("sobi")
print("--------")
print(trie.exist("sobh"))
print(trie.exist("raghav"))
