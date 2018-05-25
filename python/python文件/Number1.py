#从键盘输入一个数，验证是否为质数

y = int(input('Enter number:'))
x = y//2
while x > 1:
    if y % x == 0:
        print(y,'has factor',x)
        break
    x -= 1
else:
    print(y,'is prime')
