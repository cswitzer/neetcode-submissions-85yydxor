class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr.lookup:
                curr = curr.lookup[letter]
            else:
                curr.lookup[letter] = TrieNode()
                curr = curr.lookup[letter]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(word_index: int, root: Optional[TrieNode]):
            curr = root
            for i in range(word_index, len(word)):
                letter = word[i]
                if letter == ".":
                    for trie_node in curr.lookup.values():
                        if dfs(i + 1, trie_node):
                            return True
                    return False
                else:
                    if letter not in curr.lookup:
                        return False
                    curr = curr.lookup[letter]
            return curr.is_end
        return dfs(0, self.root)

            
                
