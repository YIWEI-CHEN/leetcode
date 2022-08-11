def odd_composition(n: int, prefix="", min_allowed=1) -> None:
    """
    Print all compositions of a number in odd parts. I.e. for n = 8:
        7 + 1
        5 + 3
        5 + 1 + 1 + 1
        3 + 3 + 1 + 1
        3 + 1 + 1 + 1 + 1 + 1
        1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
    """
    def is_odd(n):
        return n % 2 == 1
    if prefix == "" and is_odd(n):
        print(n)
    for i in range(int((n + 1) / 2)):
        j = i * 2 + 1
        if j <= n - j and j >= min_allowed:
            new_prefix = f"{j} + {prefix}"
            if is_odd(n - j):
                print(f"{new_prefix}{n - j}")
            odd_composition(n - j, new_prefix, j)


if __name__ == '__main__':
    odd_composition(8)
