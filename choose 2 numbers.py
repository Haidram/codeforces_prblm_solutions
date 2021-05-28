def findNum(arr1, arr2):
    arr1.sort()
    arr2.sort()
    return arr1[-1], arr2[-1]

n = int(input())
a = list(map(int,input().strip().split()))[:n]
m = int(input())
b = list(map(int,input().strip().split()))[:m]
ans_a, ans_b = findNum(a,b)
print("{} {}".format(ans_a, ans_b))
