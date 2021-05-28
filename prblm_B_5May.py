def solve(n):
    char_len = len(str(n))
    char = str(n)
    if char_len == 1:
        return n
    elif char_len == 2:
        arr = [str(char[0])]*char_len
        check = int("".join(arr))
        if check > n:
            temp = int(char[0])
            count = temp + 8
            return count
        else:
            return (int(char[0]) + 9)
    else:
        arr = [str(char[0])]*char_len
        check = int("".join(arr))
        if check > n:
            temp = int(char[0])
            temp1 = (char_len-2)*9
            count = temp + temp1 + 8
            return count
        else:
            temp = int(char[0])
            temp1 = (char_len-2)*9
            count = temp + temp1 + 9
            return count

t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))
