s = ""
for i in range(2):
    s += input()
s = list(s)
t = s.copy()
t.reverse()
if s == t:
    print("YES")
else:
    print("NO")
