from bisect import insort_left
from itertools import product
class Solution:
    def generateSentences(self, synonymns, text):
        dictionary = {}
        pool = []
        for word1,word2 in synonymns:
            found = -1
            print(pool)
            for i, subpool in enumerate(pool):
                if found >= 0 and (word1 in subpool or word2 in subpool):
                    for word in subpool:
                        dictionary[word] = found
                        if word not in pool[found]:
                            insort_left(pool[found],word)
                elif found<0 and word1 in subpool:
                    dictionary[word2] = i
                    insort_left(subpool, word2)
                    found = i
                elif found<0 and word2 in subpool:
                    dictionary[word1] = i
                    insort_left(subpool, word1)
                    found = i
            if found<0:
                dictionary[word1] = len(pool)
                dictionary[word2] = len(pool)
                pool.append(sorted((word1,word2)))
        print(pool)   
        l = []
        
        for word in text.split(" "):
            if word in dictionary:
                l.append(pool[dictionary[word]])
            else:
                l.append((word,))
        
        return [" ".join(i) for i in product(*l)]

# s = Solution()
# l = s.generateSentences([["a","b"],["b","e"],["d","e"],["c","d"]],"a b")

# print(l)
# print(len(l))
