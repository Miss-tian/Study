# -*- coding: utf-8 -*-
#导入math库，方便数学运算
import math

#素数是只能被1和本身整除的数，2~N-1的其他数是不能被整除的
def num(N):
    for i in (2,N):
        if N%i == 0:
            #如果N对i求余等于0，说明N不是素数，返回不是素数的数
            return N 
        break
    
L=list(filter(num,range(1,100)))

print(L)

