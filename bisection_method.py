import matplotlib.pyplot as plt
import numpy as np


'''Метод бисекции для поиска корней заданной функции
   f: заданная функция
   [a, b]: заданный отрезок
   eps: заданная точность
'''
def bisection(f, a, b, eps):
    if f(a) * f(b) > 0:
        return "Решения нет, либо оно не единственно"      
    while (b - a) / 2 > eps:
        c = (a + b) / 2 #находим середину отрезка
        if f(c) == 0: #если выполняется условие, решение найдено
            return c
        #если f(a)*f(c)<0 то корень расположен на отрезке [a, с]
        elif f(a) * f(c) < 0:
            b = c
        #иначе, на отрезке [с, b]
        else:
            a = c
    return c
     

def function(x):
    #задаем функцию
    return x**3 - 10

x = bisection(function, 1, 4, 0.00000001)
print(f"Корень уравнения x = {x}")
#построение графика функции
fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(1, 4, 100)
y = x**3 - 10
ax.plot(x, y)
plt.show()