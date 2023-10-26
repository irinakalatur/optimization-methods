import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify




eps = 0.00000001

def f(f_x, x):
    return eval(f_x)


def bisection(f_x, a, b, eps): 
    if f(f_x, a) * f(f_x, b) > 0:
        return "Решения нет, либо оно не единственно"      
    while (b - a) / 2 > eps:
        c = (a + b) / 2 #находим середину отрезка
        if f(f_x, c) == 0: #если выполняется условие, решение найдено
            return c
        #если f(a)*f(c)<0 то корень расположен на отрезке [a, с]
        elif f(f_x, a) * f(f_x, c) < 0:
            b = c
        #иначе, на отрезке [с, b]
        else:
            a = c
    return c


def chord(f_x, a, b, eps):
    if f(f_x, a) * f(f_x, b) > 0:
        return "Решения нет, либо оно не единственно"
    c = a - f(f_x, a)*(b - a) / (f(f_x, b) - f(f_x, a))      
    while abs(f(f_x, c)) > eps:
        #если f(a)*f(c)<0 то корень расположен на отрезке [a, с]
        if f(f_x, a) * f(f_x, c) < 0:
            b = c
        #иначе, на отрезке [с, b]
        else:
            a = c
        c = a - f(f_x, a)*(b - a) / (f(f_x, b) - f(f_x, a))
    return c


def golden_ratio(f_x, a, b, eps):
    while (b - a) / 2 > eps:
        #разбиваем отрезок двумя точками x1 и x2 
        x1 = a + (b - a) * (3 - 5**0.5) / 2
        x2 = a + (b - a) * (5**0.5 - 1) / 2
        #если f(x1) < f(x2), то минимум достигается на отрезке [a, x1]
        if f(f_x, x1) < f(f_x, x2):
            b = x2
        #иначе, минимум достигается на отрезке [x1, b]
        else:
            a = x1
        c = (a + b) / 2 #положение глобального минимума
    return f(f_x, c), c
