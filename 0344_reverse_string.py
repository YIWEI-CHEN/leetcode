from typing import List


class SlowSolution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = int(len(s))
        for head, tail in zip(range(l), range(l - 1, 0, -1)):
            if head >= tail:
                break
            tmp = s[head]
            s[head] = s[tail]
            s[tail] = tmp


class RecursiveSolution:
    def reverseString(self, s: List[str]) -> None:
        def swap(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                swap(l + 1, r - 1)
        swap(0, len(s) - 1)


class FinalSolution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


if __name__ == '__main__':
    # s = ["h","e","l","l","o"]
    s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    e = ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
    FinalSolution().reverseString(s)
    print(s)
    print(s == e)