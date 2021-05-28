def findAns(s):
    alice = 0
    import re
    record = re.findall(r"[1]+",s)
    arr = []
    for i in record:
        arr.append(len(i))
    arr.sort()
    arr.reverse()
    j = 0
    while j < len(arr):
        alice += arr[j]
        j += 2
    return alice
            
t = int(input())
for i in range(t):
    s = input()
    result = findAns(s)
    print(result)
