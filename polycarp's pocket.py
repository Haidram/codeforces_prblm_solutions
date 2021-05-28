def findAns(a,n):
    ele_dict = {}
    for i in a:
        if i not in ele_dict:
            ele_dict[i] = 0
        ele_dict[i] += 1
    max_el = ele_dict[i]
    for j in ele_dict.values():
        if j > max_el:
            max_el = j
    return max_el

n = int(input())
a = list(map(int,input().strip().split()))[:n]
result = findAns(a,n)
print(result)
