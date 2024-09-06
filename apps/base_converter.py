# -*- encoding: utf-8 -*-
'''
@File    :   base_converter.py
@Time    :   2024/09/06 17:30:27
@Author  :   zhangyiming
@Version :   1.0
@Desc    :   None
'''

from pythonds.basic import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString


if __name__ == "__main__":
    decNumber = 110
    base = 16
    
    print(baseConverter(decNumber, base))
