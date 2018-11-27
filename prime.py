#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:58:07 2018

@author: lchris
This programm is better for bigger intervalls.
"""
x=3
a=0
b=100
i=0
primes=[2]
lenght=len(primes)
divisible=False 
for x in range(a,b):
    while i<=lenght:
       s=primes[i]
       if (x%s==0):
           divisible=True
           
    if divisible==False:
        primes.append(x)
        if x in range(a,b):
            print(x)
    i=i+1
x=x+1
                
