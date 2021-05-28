arr = list(map(int,input().strip().split()))[:4]    ##Taking the input
n2 = arr[0]          ##Seperating the numbers
n3 = arr[1]          ##of 2s, 3s, 5s and 6s
n5 = arr[2]
n6 = arr[3]
temp = 0            ##Starting with 0

min_num = min(n2,n5,n6)
temp += min_num*256
n2 -= min_num

min_num = min(n2,n3)
temp += min_num*32
print(temp)
