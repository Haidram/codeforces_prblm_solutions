def solve(a, n):
    count = max_count = 1

    for i in range(1,n):
        if a[i] >= a[i-1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count

    return max_count


n = int(input())
a = list(map(int,input().strip().split()))[:n]
print(solve(a, n))
