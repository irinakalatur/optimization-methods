import matplotlib.pyplot as plt
import numpy as np


'''Метод золотого сечения для поиска минимумов заданной функции
   f: заданная функция
   [a, b]: заданный отрезок
   eps: заданная точность
'''
def golden_ratio(f, a, b, eps):
    while (b - a) / 2 > eps:
        #разбиваем отрезок двумя точками x1 и x2 
        x1 = a + (b - a) * (3 - 5**0.5) / 2
        x2 = a + (b - a) * (5**0.5 - 1) / 2
        #если f(x1) < f(x2), то минимум достигается на отрезке [a, x1]
        if f(x1) < f(x2):
            b = x2
        #иначе, минимум достигается на отрезке [x1, b]
        else:
            a = x1
        c = (a + b) / 2 #положение глобального минимума
    return f(c), c
     

def function(x):
    #задаем функцию (x-1)^2*sin(x)
    return np.sin(x) * (x - 1) ** 2

y, x = golden_ratio(function, -2, 0, 0.001)
print(f"Минимальное значение функции y = {y} при x = {x}")
#построение графика функции
fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(-2, 0, 70)
y = np.sin(x) * (x - 1) ** 2
ax.grid()
ax.plot(x, y, marker ='o', markersize = 3, markerfacecolor ='red')
plt.show()