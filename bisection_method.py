import matplotlib.pyplot as plt
import numpy as np


'''Метод бисекции для поиска корней заданной функции
   f: заданная функция
   [a, b]: заданный отрезок
   eps: заданная точность
'''
def bisection(f, a, b, eps):
    if f(a) * f(b) > 0:
         return "Решений нет"
         
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
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