# -*- encoding: utf-8 -*-
'''
@File    :   match_symbol_2.py
@Time    :   2024/09/06 13:51:35
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
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
    
def matches(open, close):
    opens = "([{"
    closers = "}])"
    
    return opens.index(open) == closers.index(close)

