def printString(inputstr):
    a = ""
    for ele in inputstr:
        a += ele
    return a

def tooLongstring(inputString):
    if len(inputString) > 10:
        print(inputString[0] + str(len(inputString)-2) + inputString[-1])
    else:
        print(printString(inputString))

num = int(input())
for i in range(num):
    char = []
    char += input()
    tooLongstring(char)
