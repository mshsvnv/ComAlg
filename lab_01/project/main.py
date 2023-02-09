import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

def read_from_file(x, y, y_der):                       # функция для считывания данных из файла
    with open("data.csv", "r") as file:
        points = list(csv.DictReader(file))

    for point in points:
        x = np.append(x, float(point.get("x")))      
        y = np.append(y, float(point.get("y")))
        y_der = np.append(y_der, float(point.get("y_der")))

    return x, y, y_der

def get_configuration(x_value, x, y, y_der, poly_pow):      # функция для получения конфигурации

    if (x_value < np.min(x) or x_value > np.max(y)):
        raise ValueError("Extrapolation is prohibited!")
    else:

        x_config = np.zeros(0)
        y_config = np.zeros(0)
        y_der_config = np.zeros(0)

        index = 0
        size = np.size(x)

        for i in range(1, size + 1):
            if x[i] >= x_value and x[i - 1] <= x_value:
                index = i
                break
    
        i = 0

        while (i != poly_pow + 1):
            if (index + i < size):
                x_config = np.append(x_config, x[index + i])
                y_config = np.append(y_config, y[index + i])
                y_der_config = np.append(y_der_config, y_der[index + i])

            if (index - i >= 0 and i != 0):
                x_config = np.append(x_config, x[index - i])
                y_config = np.append(y_config, y[index - i])
                y_der_config = np.append(y_der_config, y_der[index - i])

            i += 1

        return x_config, y_config, y_der_config

def calculate_divided_diff(x, y):                     # функция для расчета распределенных коеффициентов

    size = np.size(y)
    divided_diff = np.zeros((size, size))
    divided_diff[:, 0] = y

    for j in range(1, size):
        for i in range(size - j):
            divided_diff[i, j] = (divided_diff[i, j - 1] - divided_diff[i + 1, j - 1]) / (x[i] - x[j + i])

    return divided_diff[0]

def get_newton_poly(x_value, x, coef):                    # функция для расчета значения конкретной точки полинома Ньютона
    
    poly_pow = np.size(x) - 1   # степень полинома
    y = coef[-1]

    for i in range(1, poly_pow + 1): # идем "обратным" ходом, от последнего значения к-та
        y = coef[poly_pow - i] + (x_value - x[poly_pow - i]) * y

    return y

x = np.empty(0)     # массив, содержащий "x"      
y = np.empty(0)     # массив, содержащий "y" 
y_der = np.empty(0) # массив, содержащий значения 1й производной 
coef = np.empty(0)  # массив, содержащий к-ты полинома Ньютона 

x, y, y_der = read_from_file(x, y, y_der)   # считываем данные из файла

x_config, y_config, y_der_config = get_configuration(0.6, x, y, y_der, 3)
print(x_config)
coef = calculate_divided_diff(x_config, y_config)

print(get_newton_poly(0.6, x_config, coef))

x_new = np.arange(np.min(x_config), np.max(x_config), .1)
y_new = np.array([get_newton_poly(point, x_config, coef) for point in x_new])

fig, ax = plt.subplots()

ax.plot(x_new, y_new, color = "black")
ax.plot(x_config, y_config, 'bo')
plt.show()


# TODO: сделать нормальные графики и границы конфигурации
