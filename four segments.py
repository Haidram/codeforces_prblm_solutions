def solve(arr):
    a1 = arr[0]
    a2 = arr[1]
    a3 = arr[2]
    a4 = arr[3]
    area1 = min(a1,a2)*min(a3,a4)
    area2 = min(a1,a3)*min(a2,a4)
    area3 = min(a1,a4)*min(a2,a3)
    return max(area1, area2, area3)

t = int(input())
for i in range(t):
    arr = list(map(int,input().strip().split()))[:4]
    print(solve(arr))
