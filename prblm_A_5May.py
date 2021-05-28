def solve(n,char_str):
    checked = []
    checking = char_str[0]
    for i in char_str:
        if i != checking:
            if i in checked:
                return 'NO'
            checked.append(checking)
            checking = i
    return 'YES'
        

t = int(input())
for i in range(t):
    n = int(input())
    char_str = input()
    print(solve(n,char_str))
