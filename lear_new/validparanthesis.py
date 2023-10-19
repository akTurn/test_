class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chrsTostart = ['(', '{', '[']
        chrsToend = [')', '}', ']']

        for char in s:
            if char in chrsTostart:
                stack.append(char)
            elif char in chrsToend:
                if not stack:
                    return False  # Unmatched closing parenthesis

                top = stack.pop()

                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['):
                    return False  # Mismatched opening and closing parenthesis

        return len(stack) == 0  # True if all parentheses are balanced

solution = Solution()
result = solution.isValid('()[(())]')
print(result)
