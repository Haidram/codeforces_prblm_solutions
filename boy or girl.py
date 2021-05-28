s = ""
s = input()

a = [0]*26
count = 0

for i in range(len(s)):
    a[ord(s[i])-ord('a')] += 1

for j in range(26):
    if a[j] != 0:
        count +=1
        
if count%2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
