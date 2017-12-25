'''import time
date=time.localtime()
year,month,day=date[:3]
day_month=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%400==0 or (year%4==0 and year%100!=0):
    day_month[1]=29
if month==1:
    print(day)
else:
    print(sum(day_month[:month-1],day))
#上面的代码是计算当前这天是今年的多少天'''

import time
import datetime
def daysBetween(year1,month1,day1,year2,month2,day2):
	from datetime import date
	dif = date(year1,month1,day1)
	dif = dif - date(year2,month2,day2)
	return dif.days
print('欣欣在地球上生活了',daysBetween(2017,11,13,1992,10,20),'天')
print('堂堂在地球上生活了',daysBetween(2017,11,13,1991,11,10),'天')
#print('娟',daysBetween(2017,11,13,1991,3,29))
#print('晓瑄瑄',daysBetween(2017,11,13,1992,10,3))
print('婷婷在地球上生活了',daysBetween(2017,11,13,1994,7,12),'天')
print('宋映在地球上生活了',daysBetween(2017,11,13,1997,3,19),'天')
print('黎黎在地球上生活了',daysBetween(2017,11,13,1990,6,16),'天')

#这段代码是计算两个日期之间差多少天

'''
for n in range(100,1,-1):
	for i in range(2,n):
		if n%i == 0:
			break
		else:
			print(n)
			break
'''
'''for n in range(100,1,-1):
	for i in range(2,n):
		if n%i == 0:
			break
	else:
		print(n)
		break'''
#注意两端代码的分割线，else地方不一样，因此结果就不同

for i in range(100,1000):
    bai,shi,ge = map(int,str(i))
    if bai**3+shi**3+ge**3=i:
        print(i)
#水仙花

for i in range(1,10):
	for j in range(1,i+1):
		print('{0}*{1}={2}'.format(i,j,i*j).ljust(6),end=' ')
	print()

#九九乘法表
