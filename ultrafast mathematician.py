a = [0]*2
for i in range(2):
    a[i] = input()
s1 = str(a[0])
s2 = str(a[1])
s = ""
for j in range(len(s1)):
    if s1[j] == s2[j]:
        s += '0'
    else:
        s += '1'
print(s)
