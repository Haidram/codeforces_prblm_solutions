def even_num_on_even_pos(n,num):
    for i in range(n):
        if (i+1)%2 == 0 and int(num[i])%2 == 0:
            return True
    return False

def odd_num_on_odd_pos(n,num):
    for i in range(n):
        if (i+1)%2 == 1 and int(num[i])%2 == 1:
            return True
    return False

def who_win(n, num):
    if n%2 == 0:
        if even_num_on_even_pos(n,num):
            return 2
        else:
            return 1
    else:
        if odd_num_on_odd_pos(n,num):
            return 1
        else:
            return 2


t = int(input())
for i in range(t):
    n = int(input())
    num = input()
    print(who_win(n, num))
