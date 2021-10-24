# https://leetcode.com/problems/word-search-ii/
from src.main.python.algo.medium.trie.model import Node


class Trie:
    def __init__(self, mat):
        self.mat = mat
        self.res = {}
        self.root = {'/': Node()}

    def insert(self, arr):
        for word in arr:
            current = self.root['/']
            for c in word:
                if c not in current.children: current.children[c] = Node()
                current = current.children[c]
            current.end = True
            self.res[word] = current

    def find(self, children, i, j, visited):
        h = len(mat)
        w = len(mat[0])
        if -1 < i < h and -1 < j < w and (i, j) not in visited:
            if mat[i][j] in children:
                visited.add((i, j))
                node = children[mat[i][j]]
                self.find(node.children, i + 1, j, visited)
                self.find(node.children, i, j + 1, visited)
                self.find(node.children, i - 1, j, visited)
                self.find(node.children, i, j - 1, visited)
                node.found = node.end

    def search(self):
        node = self.root['/']
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                self.find(node.children, i, j, set())
        return [k for k, v in filter(lambda n: n[1].found, self.res.items())]


mat = [["o", "a", "a", "n"],
       ["e", "t", "a", "e"],
       ["i", "h", "k", "r"],
       ["i", "f", "l", "v"]]
arr = ["oath", "pea", "eat", "rain", "hklf", "hf"]

trie = Trie(mat)
trie.insert(arr)
print(trie.search())
