# -*- coding:utf-8 -*-
#使用filter函数计算100以内的素数，并打印出来
def num(N):
    for i in range(2,N):
        if N%i == 0:
            break
    else:
        return 'test'

L=list(filter(num,range(1,100)))
print(L)
