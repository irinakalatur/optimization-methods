import matplotlib.pyplot as plt
import numpy as np


'''Метод Ньютона для поиска корня заданной функции
   f: заданная функция на отрезке [0,1]
   df: производная заданной функции
   x0: начальное приближение (выбирается из условия: f(x0)*df(x0)>0)
   max_iter: максимальное число итераций
   eps: заданная точность
'''
def newton(f, df, x0, max_iter, eps):
    iter = 0 #счетчик итераций
    x_previous = x0 #записываем х0 в предыдущее приближение
    while iter != max_iter:
        x_next = x_previous - f(x_previous) / df(x_previous) #находим следующее приближение
        #проверяем условие сходимости
        if abs(x_next - x_previous) < eps:
            break
        x_previous = x_next
        iter += 1
    return x_next, iter
     

def function(x):
    #задаем функцию
    return x**2 + 4*x - 3


def d_function(x):
    #находим производную заданной функции
    return 3 * x + 4

x, iter = newton(function, d_function, 1, 100, 0.001)
print(f"Корень уравнения x = {x}")
print(f"Количество итераций = {iter}")
#построение графика функции
fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(0, 1, 70)
y = x**3 + 4*x - 3
ax.grid()
ax.plot(x, y, marker ='o', markersize = 3, markerfacecolor ='red')
plt.show()
