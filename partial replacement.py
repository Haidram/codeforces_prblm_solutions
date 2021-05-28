def change(str_val, char_val, index_val):
    new_val = list(str_val)
    new_val[index_val] = char_val
    return "".join(new_val)


def do_it(arr, s):
    n = arr[0]
    k = arr[1]
    count = 0
    if n == 1:
        return 1
    else:
        for j in range(n):
            if s[j] == '*':
                s = change(s,'x',j)
                count += 1
                break
        i = j+k
        while i>j:
            if i<n:
                if s[i] == '*':
                    s = change(s,'x',i)
                    count += 1
                    j = i
                    i = j+k
                else:
                    i-=1
            else:
                i-=1
        return count
            


t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:2]
    s = input()
    print(do_it(arr, s))
