import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import streamlit as st

if __name__ == "__main__":
    st.title("Методы для поиска корня и минимума функции")
    f_x = st.text_input("*Введите функцию* ***f(x)***","x**3-10")
    st.latex(sympify(f_x))
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Введите начало отрезка a", value=1)   
    with col2:
        b = st.number_input("Введите конец отрезка b", value=4)
    methods = st.selectbox('Выберите метод',
                         ('Метод бисекции для поиска корня', 
                          'Метод хорд для поиска корня', 
                          'Метод золотого сечения для поиска минимумов'),
                          index=None,
                          placeholder = "...")   
    butt = st.button("Вычислить", type="primary", use_container_width = True)



eps = 0.0001
def f(f_x, x):
    return eval(f_x)


def bisection(a, b, eps): 
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


def chord(a, b, eps):
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


def golden_ratio(a, b, eps):
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

if butt:
    if methods == 'Метод бисекции для поиска корня':
        x_b = bisection(a, b, eps)
        st.write("Корень уравнения методом бисекции:", x_b)
    elif methods == 'Метод хорд для поиска корня':
        x_c = chord(a, b, eps)
        st.write("Корень уравнения методом бисекции:", x_c)
    elif methods == 'Метод золотого сечения для поиска минимумов':
        y_gr, x_gr = golden_ratio(a, b, eps)
        st.write("Минимальное значение функции при:", x_gr)

#построение графика функции
fig, ax = plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(a, b, 70)
y = eval(f_x)
ax.grid()
ax.plot(x, y, marker ='o', markersize = 3, markerfacecolor ='red')
fig



