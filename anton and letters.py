s = ""
s = input().strip("{}")
s = s.replace(',','')
s = s.replace(' ','')
s = set(s)
print(len(s))
