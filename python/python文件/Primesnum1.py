# -*- coding:utf-8 -*-

#使用埃氏筛法计算素数

#构造一个从3开始的奇数序列

def _odd_iter():
    n=1
    while True:
        n = n + 2
        yield n

#定义一个筛选函数

def _not_divisible(n):
    return lambda x: x % n >0

#定义一个生成器，不断返回下一个素数

def primes():
    yield 2
    # 初始化序列
    it = _odd_iter()
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        # 构造新序列
        it = filter(_not_divisible(n),it)

# 打印100以内的素数：
for n in primes():
    if n < 100:
        print(n,end=' ')
    else:
        break
