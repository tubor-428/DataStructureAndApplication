# -*- encoding: utf-8 -*-
'''
@File    :   divide_by2.py
@Time    :   2024/09/06 17:18:18
@Author  :   zhangyiming
@Version :   1.0
@Desc    :   None
'''

from pythonds.basic import Stack


def divideBy2(decNumber):
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    
    return binString


if __name__ == "__main__":
    decNumber = 110
    print(divideBy2(decNumber))
    