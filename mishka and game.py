n = int(input())
m_win = 0
c_win = 0
for i in range(n):
    a = list(map(int,input().strip().split()))[:2]
    m = a[0]
    c = a[1]
    if m > c:
        m_win += 1
    elif c > m:
        c_win += 1
if m_win > c_win:
    print("Mishka")
elif c_win > m_win:
    print("Chris")
else:
    print("Friendship is magic!^^")
