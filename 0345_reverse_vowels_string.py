class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        new_s = [c for c in s]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
                continue
            if s[r] not in vowels:
                r -= 1
                continue
            new_s[l], new_s[r] = new_s[r], new_s[l]
            l, r = l + 1, r - 1
        return ''.join(new_s)


class FinalSolution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = [c for c in s]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1
        return ''.join(s)


if __name__ == '__main__':
    s = 'hello'
    expected = 'holle'
    a = FinalSolution().reverseVowels(s)
    print(a)
    print(a == expected)
