# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:24:58 2020

@author: Anand Jebakumar
"""

import numpy as np

class AddGate():
    def __init__(self):
        pass
        
    def forward(self,x,y):
        return x+y
    
    def backward(self,dz):
        dx = dz*1.0
        dy = dz*1.0
        return dx,dy
    
class MultiplyGate():
    def __init__(self):
        pass
        
    def forward(self,x,y):
        self.x = x # need to store these values for backrprop
        self.y = y
        return x*y
    
    def backward(self,dz):
        dx = dz*self.y
        dy = dz*self.x
        return dx,dy
    
w = 2.
x = 3.
b = 4.

# create gate objects
multiply = MultiplyGate()
add = AddGate()

# forward pass
wx = multiply.forward(w,x)
wx_b = add.forward(wx,b)
print(wx_b)

# backward pass
dwx,db = add.backward(1.0)
dw,dx = multiply.backward(dwx)
print(dw,dx,db)
