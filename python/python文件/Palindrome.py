'''
利用filter()筛选出回数：

思路：①首先了解什么是回数：从左往右和从右往左读都是一样的数，称为回数
      ②联想到切片的步进，就很好解决这个问题了
      ③怎样让随机数变成字符串

'''

# -*- coding:utf-8 -*-
#定义一个函数，使两个字符串相等

def is_palindrome(n):
    #将传进来的数字变成字符，一遍应用字符串的切片功能
    L1=str(n)
    L2=L1[::-1]
    return L2 == L1

output = filter(is_palindrome,range(1,1000))
print('1~1000的回数有:',list(output))
if list(filter(is_palindrome,range(1,200))) == [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]:
    print('测试成功!')
else:
    print('测试失败!')
