n = int(input())
s = ""
s = input().lower()
a = [0]*26
count = 0
for i in range(n):
    a[ord(s[i])-ord('a')] += 1
for j in range(26):
    if a[j] > 0:
        count += 1
if count == 26:
    print("YES")
else:
    print("NO")
