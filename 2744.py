class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        swords = set(words)
        count = 0
        for word in words:
            if word == word[::-1]:
                pass
            elif word[::-1] in swords:
                count += 1
        return count//2
