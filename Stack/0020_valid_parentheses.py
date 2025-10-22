"""
Valid Parentheses

Easy

Links:
1. NeetCode 150: https://neetcode.io/problems/valid-parentheses
2. LeetCode: https://leetcode.com/problems/valid-parentheses/


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
A string is considered valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '[': ']',
            '{': '}',
            '(': ')',
        }
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if mapping[top] != c:
                    return False
        return True if len(stack) == 0 else False


class StackSolution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    Recommended Solution
    """
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    s = '])'
    e = False
    ans = StackSolution().isValid(s)
    print(ans == e)
