def check_sum(n,s):
    net = 0
    for i in str(n):
        net += int(i)
    if net<=s:
        return True
    else:
        return False

def find_ans(n,s):
    count = 0
    done = check_sum(n,s)
    start = 1
    str_n = str(n)
    checking = str_n[0]
    while not done:
        if s <= int(checking):
            count = 10**(len(str(n))) - n
            break
        if n%(10**start) == 0  :
            start += 1
            continue
        num = (10**start) - n%(10**start)
        n += num
        count += num
        start += 1
        done = check_sum(n,s)
        
    return count

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:2]
    n = arr[0]
    s = arr[1]
    result = find_ans(n,s)
    print(result)
