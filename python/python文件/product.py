#！
def product(*numbers):
    #判断参数是否为空，若为空则抛错；不为空时，则循环相乘并返回结果
    if len(numbers)==0:
        raise TypeError('TypeError')
    else:
        s=1
        for n in numbers:
            s=s*n
        return s
