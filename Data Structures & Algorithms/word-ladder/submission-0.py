class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        ladder_len = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ladder_len
                # e.g. all neis of cat would be those of the patterns
                # [*at, c*t, ca*]. So neis could be hat, cut, car, etc.
                # since these differ by a single letter. If any of the neis
                # are the endWord, or have a nei that is the endWord, we 
                # know we have reached the ladder length
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            ladder_len += 1
        return 0