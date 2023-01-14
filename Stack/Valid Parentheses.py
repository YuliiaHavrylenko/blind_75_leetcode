# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Input: s = "()"
# Output: true
#
# Input: s = "()[]{}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True

#Solution with stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeHash = {")": "(", "]": "[", "}": "{"}

        for b in s:
            if b in closeHash:
                if stack and stack[-1] == closeHash[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False