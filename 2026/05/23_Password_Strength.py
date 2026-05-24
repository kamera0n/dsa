import string
class Solution:
    def passwordStrength(self, password: str) -> int:
        # We take the set of the values and loop through applying strength
        res = 0
        for char in set(password):
            if char in string.ascii_lowercase:
                res += 1
            elif char in string.ascii_uppercase:
                res += 2
            elif char in "0123456789":
                res += 3
            elif char in "!@#$":
                res += 5
        return res