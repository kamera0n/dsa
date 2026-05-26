class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Can take the set, put to lowercase and set again, if there's a diff then we have our answer
        # Lol I did not read the q right
        return len(set(word)) - len(set(word.lower()))