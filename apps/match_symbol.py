# -*- encoding: utf-8 -*-
'''
@File    :   match_symbol.py
@Time    :   2024/09/06 10:27:36
@Author  :   zhangyiming
@Version :   1.0
@Desc    :   None
'''

from pythonds.baisc import Stack



def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
