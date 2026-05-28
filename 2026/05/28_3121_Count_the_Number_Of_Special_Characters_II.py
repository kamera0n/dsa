class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Here I feel like sorting is your friend, ie aA is correctly sorted but Aa is not, so you could compare the sorted string
        # Constant space so I could just use a hashmap to see if both upper and lower of c exist in string, if they do, uhhh
        # I think you stil want to set this bc dupes just confuse things
        # If I take the set, sort the set
        # What if I just loop through, if I see an uppercase before the lowercase then we don't add?
        # So I take the set, then I am putting each letter into 

        # For each letter you either haven't seen it or you have seen it. If you've seen it you've either seen the lower or upper and you're currently looking at the upper or lower, finally you might've seen an upper then lower

        # Note that all occurences of the lowercase need to be first
        # So I loop through, use a hashmap to store the letters,

        """if I see a lowercase letter and:
            c[letter] = 0 (unassigned) -> 1
            c[letter] = 1 (seen lowercases) -> 1
            c[letter] = -1 (seen cap then lower) -> -1"""

        """if I see a uppercase letter and:
            c[letter] = 0 (unassigned) -> -1 (cannot use letter)
            c[letter] = 1 (seen lowercases) -> 2 (success)
            c[letter] = -1 (seen cap then lower) -> -1"""

        letter_hash = [0] * 26
        for letter in word:
            if letter in ascii_lowercase:
                letter_ind = ord(letter)-ord('a')
                if letter_hash[letter_ind] == 0:
                    letter_hash[letter_ind] = 1
                elif letter_hash[letter_ind] == 2:
                    letter_hash[letter_ind] = -1 
            if letter in ascii_uppercase:
                letter_ind = ord(letter)-ord('A')
                if letter_hash[letter_ind] == 0:
                    letter_hash[letter_ind] = -1
                elif letter_hash[letter_ind] == 1:
                    letter_hash[letter_ind] = 2
        #print(letter_hash)
        return letter_hash.count(2)