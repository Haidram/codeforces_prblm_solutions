def get_val(intarr):
    b = ""
    b += intarr[0]
    for j in range(1,len(intarr)-1,2):
        b += intarr[j]
    b += intarr[len(intarr)-1]
    return b

n = int(input())
for i in range(n):
    a = input()
    arr = get_val(a)
    print(arr)
