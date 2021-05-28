s = ""
n = input()
s = input()
count = 0
for i in range(len(s)-1):
    if ord(s[i])-ord(s[i+1]) == 0:
        count += 1
    
print(count)
