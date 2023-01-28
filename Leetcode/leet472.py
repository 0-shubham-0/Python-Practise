class Solution:
    def findAllConcatenatedWordsInADict(words):
        def dfs(w, i):
            n = len(w)
            if i == n: # we found a path from 0 to n using words from words_set (its not the word itself) -> concatenated word
                res.append(w)
                return
             # catdog
            for j in range(i, n+1):
                if w[i:j] in words_set and (i > 0 or j != n):
                    # visited.add(j)
                    dfs(w, j)
        words_set = set(words)
        res = []
        for w in words:
            # visited = {0}
            dfs(w, 0) # checks if there's a path from 0 to n - 1 in
        print(res)

words = ["cat","dog","catdog"]
Solution.findAllConcatenatedWordsInADict(words)