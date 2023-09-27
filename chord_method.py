import matplotlib.pyplot as plt
import numpy as np


'''Метод хорд для поиска корня заданной функции
   f: заданная функция
   [a, b]: заданный отрезок
   eps: заданная точность
'''
def chord(f, a, b, eps):
    if f(a) * f(b) > 0:
        return "Решения нет, либо оно не единственно"
    c = a - f(a)*(b - a) / (f(b) - f(a))      
    while abs(f(c)) > eps:
        #если f(a)*f(c)<0 то корень расположен на отрезке [a, с]
        if f(a) * f(c) < 0:
            b = c
        #иначе, на отрезке [с, b]
        else:
            a = c
        c = a - f(a)*(b - a) / (f(b) - f(a))
    return c
     

def function(x):
    #задаем функцию
    return x**3 - x + 1

x = chord(function, -2, -1, 0.001)
print(f"Корень уравнения x = {x}")
#построение графика функции
fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(-2, -1, 70)
y = x**3 - x + 1
ax.grid()
ax.plot(x, y, marker ='o', markersize = 3, markerfacecolor ='red')
plt.show()