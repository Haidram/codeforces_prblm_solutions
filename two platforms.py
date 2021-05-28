def find_points(arr,dic,starting,ending,plat_size):
    max_t = 0
    for i in range(starting,ending+1):
        count = 0
        for j in range(i,i+plat_size+1):
            if j <= ending:
                count += dic[arr[j]]
                print(dic[arr[j]])
        max_t = max(max_t,count)
    return max_t

def max_points_saved(a, x_arr):
    k = a[1]
    x_arr.sort()
    if x_arr[a[0]-1]-x_arr[0] <= 2*k + 1:
        return a[0]
    else:
        dict_num = {}
        for i in x_arr:
            if i not in dict_num:
                dict_num[i] = 0
            dict_num[i] += 1
        n = len(dict_num)
        print(dict_num)
        mxpt = 0
        start = k
        end = (n-1)-(k+1)
        ref_int = list(set(x_arr))
        for j in range(start,end+1):
            crpt1 = find_points(ref_int,dict_num,0,j,k)
            crpt2 = find_points(ref_int,dict_num,j+1,n-1,k)
            mxpt = max(mxpt,crpt1+crpt2)
        return mxpt
        

t = int(input())
for i in range(t):
    a = list(map(int,input().strip().split()))[:2]
    x_arr = list(map(int,input().strip().split()))[:a[0]]
    y_arr = list(map(int,input().strip().split()))[:a[0]]
    print(max_points_saved(a, x_arr))
