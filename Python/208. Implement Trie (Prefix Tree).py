class Trie:
    class TrieNode:
        def __init__(self):
            self.arr = [None] * 26
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.arr[idx] is None:
                cur.arr[idx] = self.TrieNode()
            cur = cur.arr[idx]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.arr[idx] is None:
                return False
            cur = cur.arr[idx]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.arr[idx] is None:
                return False
            cur = cur.arr[idx]
        return True
