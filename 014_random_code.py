#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用于生成随机数的模块：random
#函数chr()返回对应的ASCII字符，与ord()作用相反。

import random

#在1-100之间生成随机数
num = random.randint(1,100)


#随机生成一个大写字母,ASCII码值65-90对应的是A-Z
cap = chr(random.randint(65,90))

#随机生成一个小写字母,ASCII码值97-122对应的是a-z
low = cap = chr(random.randint(97,122))


#下面定义一个验证码生成的函数
def verification_code():
    num = random.randint(100,1000)
    capa = chr(random.randint(65,90))
    capb = chr(random.randint(65,90))
    low = chr(random.randint(97,122))
    vercode = capa + str(num) + capb + low
    return vercode
    

#第二种定义
def ver():
    ver = []
    for i in range(6):
        if i == random.randint(1,9):
            ver.append(random.randint(1,9))
        else:
            temp = random.randint(65,90)
            ver.append(chr(temp))
    code = ''.join(ver)
    return code
    
    
print '验证码：%s' % verification_code()
print '验证码：', ver()


#第三种定义（推荐做法）
'''
randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
random.randrange ([start,] stop [,step])
参数
    start -- 指定范围内的开始值，包含在范围内。
    stop -- 指定范围内的结束值，不包含在范围内。
    step -- 指定递增基数。

random模块中randrange()和randint()不同的是前者可以指定一个基数，默认为1

'''

checkcode = ""

for i in range(6):
    current = random.randrange(0,9,2)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)

print checkcode
