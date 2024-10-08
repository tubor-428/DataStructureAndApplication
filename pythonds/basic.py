# -*- encoding: utf-8 -*-
'''
@File    :   baisc.py
@Time    :   2024/09/06 10:24:50
@Author  :   zhangyiming
@Version :   1.0
@Desc    :   None
'''

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


# 另一种实现
class Stack2:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
