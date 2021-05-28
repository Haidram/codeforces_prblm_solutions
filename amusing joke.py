s1 = input()
s2 = input()
s3 = input()
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)
a1 = [0]*26
a2 = [0]*26
if l1+l2 != l3:
    print("NO")
else:
    for i in range(l1):
        a1[ord(s1[i])-ord('A')] += 1
    for j in range(l2):
        a1[ord(s2[j])-ord('A')] += 1
    for k in range(l3):
        a2[ord(s3[k])-ord('A')] += 1
    flag = 0
    n = 0
    while flag == 0 and n < 26:
        if a1[n] != a2[n]:
            flag = 1
        n += 1
    if flag == 0:
        print("YES")
    else:
        print("NO")
