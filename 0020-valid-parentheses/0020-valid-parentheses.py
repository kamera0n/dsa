class Solution:
    def isValid(self, s: str) -> bool:
        # We want a stack, a first in first out data structure
        # With this stack we pop off a close if it matches top open otherwise error
        stack = []
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            elif bracket in ')}]':
                if not stack:
                    return False
                top = stack.pop()
                if top+bracket not in '()[]{}':
                    return False
                continue
        return not stack