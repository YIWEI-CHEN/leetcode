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


class FinalSolution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '[': ']',
            '{': '}',
            '(': ')',
        }
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                top = stack.pop() if stack else None
                if top is None or mapping[top] != c:
                    return False
        return not stack


if __name__ == '__main__':
    s = '])'
    e = False
    ans = FinalSolution().isValid(s)
    print(ans == e)
