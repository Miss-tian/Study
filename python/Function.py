import random
import string
import codecs

#常用汉字Unicode编码表
StringBase='\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba'
#转换为汉字
StringBase=''.join(StringBase.split('\\u'))

def getEmail():
    suffix=['.com','.org','.net','.cn']
    characters=string.ascii_letters+string.digits+'_'
    username=''.join((random.choice(characters) for i in range(random.randint(6,12))))
    domain=''.join((random.choice(characters) for i in range(random.randint(3,6))))
    return username+'@'+domain+random.choice(suffix)

def getTelNo():
    return ''.join((str(random.randint(0,9))for i in range(11)))

def getNameOrAddress(flag):
    '''flag=1 表示返回随机姓名，flag=0表示返回随机地址'''
    result=''
    if flag==1:
        #大部分中国人姓名为2~4个汉字
        rangestart,rangeend=2,5
    elif flag==0:
        #假设地址再10~30个汉字之间
        rangestart,rangeend=10,31
    else:
        print('flag must be 1 or 0')
        return ''
    for i in range(rangestart,rangeend):
        result+=random.choice(StringBase)
    return result

def getSex():
    return random.choice(('男','女'))

def getAge():
    return str(random.randint(18,100))
#41
def main(filename):
    #生成一个filename的文件，如果没有就新建，有就覆盖
    with codecs.open(filename,'w','utf8')as fp:
        fp.write('Name,Sex,Age,TelNo,Address,Email\n')
        #随机生成200个人的信息
        for i in range(20):
            name=getNameOrAddress(1)
            sex=getSex()
            age=getAge()
            tel=getTelNo()
            address=getNameOrAddress(1)
            email=getEmail()
            line=','.join([name,sex,age,tel,address,email])+'\n'
            fp.write(line)

def output(filename):
    with codecs.open(filename,'r','utf-8')as fp:
        while True:
            line=fp.readline()
            if not line:
                return
            line=line.split(',')
            for i in line:
                print(i,end=',')
            print()


if __name__=='__main__':
    filename='information.txt'
    main(filename)#生成文件信息
    output(filename)#输出文件信息
    
