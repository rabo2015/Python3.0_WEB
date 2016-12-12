#!/usr/bin/python
#coding: utf-8
#圆的面积和周长计算
import math
from pip._vendor.distlib.compat import raw_input
radiusString=raw_input("Enter the radius of your cirecle:")
radiusInteger=int(radiusString)

circumference=2*math.pi*radiusInteger
area=math.pi*(radiusInteger**2)


print("周长： ",circumference,",面积： ",area)


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

