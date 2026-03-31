class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        3 choices
        Insert a character
        Delete a character
        Replace a character

        We can only operate on word1 and not word2
        
        monkeys
        money

        remove k
        remove s
        answer 2

        neatcdee
        neetcode
        answer 3

        replace a with e
        remove last e
        replace d with o

        what are we inserting into word1?
        what are we replacing into word2?

        I would assume a letter from word2

        Additionally, we can keep track of two pointers, i and j
        But then what would the state be? I want to believe it could just be i and j, but 
        we can either add, remove, or replace, So would the state be three dimensions?
        It won't, since the state at i, j already stores the result of all three operations

        So dp[(i, j)] will be the min of 
        - dp[(i + 1, j)] delete
        - dp[(i, j + 1)] insert (think about monky and monkey, where i = 4 and j = 4. If we insert
        word2[4] into word1[4], then the words are the same and only j increments)
        - dp[(i + 1, j + 1)] replace

        base case:
        if word1 and word2 are empty, the minDistance is 0 since no operations are needed

        if the letters are the same, we don't really do anything
        if letters at i, j do not match, we go through the 3 operations and return the min from each
        """
        dp = {}

        def dfs(i: int, j: int) -> int:
            if i == len(word1) and j == len(word2):
                return 0
            # insert characters at j until len of word1 is len of word2 
            if i == len(word1):
                return len(word2) - j
            # delete rest of characters in word1 to be the same as word2
            if j == len(word2):
                return len(word1) - i

            if (i, j) in dp:
                return dp[(i, j)]

            min_dist = 0
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                delete = dfs(i + 1, j)
                insert = dfs(i, j + 1)
                replace = dfs(i + 1, j + 1)
                dp[(i, j)] = 1 + min(delete, insert, replace)
            
            return dp[(i, j)]
        
        return dfs(0, 0)


