def findways(inputNum):
    x = inputNum[0]
    y = inputNum[1]
    answer = 0
    numInt = abs(x-y)
    if numInt == 0:
        answer = 0
    elif numInt <= 10:
        answer = 1
    elif numInt%10 == 0:
        answer = int(numInt/10)
    else:
        answer = int(numInt/10) + 1
    return answer

num = int(input())
noOfways = 0
for i in range(num):
    a = []
    a = list(map(int,input().strip().split()))[:2]
    noOfways = findways(a)
    print(noOfways)
