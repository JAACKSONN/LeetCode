class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
            
        

    def search(self, word: str) -> bool:
        def dfs(curr, j):
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                elif word[i] in curr.children:
                    curr = curr.children[word[i]]
                else:
                    return False
            return curr.end
        return dfs(self.root, 0)
            
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)