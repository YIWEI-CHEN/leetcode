"""
Generate Parentheses

Medium

Links:
1. NeetCode 150: https://neetcode.io/problems/generate-parentheses
2. LeetCode: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

"""
from typing import List

class BacktrackingSolution:
    """Backtracking Solution
    1. Core Idea - Backtracking:
    The solution uses backtracking to build valid parentheses combinations character by character. It maintains two counters:
        - openN: Number of opening parentheses `(` added so far
        - closedN: Number of closing parentheses `)` added so far
        
    Example Walkthrough (n=2)
    Starting with backtrack(0, 0):

    1. Add ( → backtrack(1, 0) with stack = ['(']
        - Add ( → backtrack(2, 0) with stack = ['(', '(']
            - Add ) → backtrack(2, 1) with stack = ['(', '(', ')']
                - Add ) → backtrack(2, 2) with stack = ['(', '(', ')', ')']
                    - Base case reached: add "(())" to results
        - Add ) → backtrack(1, 1) with stack = ['(', ')']
            - Add ( → backtrack(2, 1) with stack = ['(', ')', '(']
                - Add ) → backtrack(2, 2) with stack = ['(', ')', '(', ')']
                    - Base case reached: add "()()" to results
    2. Result: ["(())", "()()"]
    
    Time Complexity: O(4^n / sqrt(n)) - nth Catalan Number, representing the number of valid parentheses combinations
    Space Complexity: O(n) - Recursion Stack, The recursion stack depth and the stack list both grow to at most 2n in size
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openN, closedN):
            # Base case: If we've used exactly n opening and n closing parentheses
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            # Add opening parenthesis if we haven't used all n
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN) # Add valid combination to results
                stack.pop() # Backtrack: remove the opening parenthesis
    
            # Add closing parenthesis if it won't make the string invalid
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1) # Recurse with one more closing
                stack.pop() # Backtrack: remove the closing parenthesis

        backtrack(0, 0)
        return res