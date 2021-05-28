from datetime import date
from datetime import timedelta
inp = input()
arr = inp.split(' ')
date2 = arr[-1].split('/')
date1 = arr[-2].split('/')
d2 = date(int(date2[2]),int(date2[1]),int(date2[0]))
d1 = date(int(date1[2]),int(date1[1]),int(date1[0]))
rem_days = (d2-d1).days
new_date = str(d1 + timedelta(15))
new_d = new_date.split('-')
new_d.reverse()
new_date_1 = '/'.join(new_d)
print("{} {} ${}".format(arr[0]+arr[1],new_date_1,rem_days))


