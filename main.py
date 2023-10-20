import methods 
import streamlit as st

st.title("Методы для поиска корня и минимума функции")
f_x = st.text_input("*Введите функцию* ***f(x)***","x**3-10")
st.latex(methods.sympify(f_x))
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Введите начало отрезка a", value=1.0)   
with col2:
    b = st.number_input("Введите конец отрезка b", value=4.0)
met = st.selectbox('Выберите метод',
                         ('Метод бисекции для поиска корня', 
                          'Метод хорд для поиска корня', 
                          'Метод золотого сечения для поиска минимумов'),
                          index=None,
                          placeholder = "...")   
butt = st.button("Вычислить", type="primary", use_container_width = True)

if butt:
    if met == 'Метод бисекции для поиска корня':
        x_b = methods.bisection(f_x, a, b, methods.eps)
        st.write("Корень уравнения методом бисекции:", x_b)
    elif met == 'Метод хорд для поиска корня':
        x_c = methods.chord(f_x, a, b, methods.eps)
        st.write("Корень уравнения методом бисекции:", x_c)
    elif met == 'Метод золотого сечения для поиска минимумов':
        y_gr, x_gr = methods.golden_ratio(f_x, a, b, methods.eps)
        st.write("Минимальное значение функции при:", x_gr)

#построение графика функции
fig, ax = methods.plt.subplots()
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
x = methods.np.linspace(a, b, 70)
y = eval(f_x)
ax.grid()
ax.plot(x, y, marker ='o', markersize = 3, markerfacecolor ='red')
fig
