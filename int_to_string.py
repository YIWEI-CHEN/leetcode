def int_to_string(number: int) -> str:
    """
    Return the string representation of an integer without using any library
    function (i.e. using first principles).
    """
    rv = ""
    negative = number < 0
    number = -number if negative else number
    while True:
        c = chr(number % 10 + 48)
        # Slow, but Python string concat is already pretty optimized:
        # https://stackoverflow.com/a/36556380
        rv = f"{c}{rv}"
        number //= 10
        if number <= 0:
            break
    if negative:
        rv = f"-{rv}"
    return rv


if __name__ == '__main__':
    ret = int_to_string(624)
    print(ret)