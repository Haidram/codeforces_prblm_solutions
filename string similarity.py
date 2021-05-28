def findNum(s,n):
    ans = ""
    for i in range(n):
        ans += s[i+i]
    return ans    

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    result = findNum(s,n)
    print(result)
