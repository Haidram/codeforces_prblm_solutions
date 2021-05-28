s = input()
count = 0
init = "a"
for i in s:
    temp = abs(ord(i) - ord(init))
    count += min(temp,26-temp)
    init = i
print(count)
