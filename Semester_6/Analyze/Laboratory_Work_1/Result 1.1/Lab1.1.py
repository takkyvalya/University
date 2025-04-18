import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    print("\nПрочитанные данные:")
    print(data.head())
    return data

def show_statistics(data):
    print("\nСтатистика по каждому столбцу:")
    for column in data.columns:
        print(f"{column}:")
        print(f"  Количество: {data[column].count()}")
        print(f"  Минимум: {data[column].min()}")
        print(f"  Максимум: {data[column].max()}")
        print(f"  Среднее: {data[column].mean()}")

def plot_original_data(x, y):
    plt.figure(1)
    plt.scatter(x, y, color='blue')
    plt.title('Исходные данные')
    plt.xlabel('X')
    plt.ylabel('Y')

def least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    print(f"\nПараметры регрессии:\n  Наклон (m): {m}\n  Смещение (b): {b}")
    return m, b

def plot_regression_line(x, y, m, b):
    plt.figure(2)
    plt.scatter(x, y, color='blue')
    y_pred = m * x + b
    plt.plot(x, y_pred, color='red')
    plt.title('Регрессионная прямая')
    plt.xlabel('X')
    plt.ylabel('Y')

def plot_error_squares(x, y, m, b):
    plt.figure(3)
    y_pred = m * x + b
    plt.scatter(x, y, color='blue')
    plt.plot(x, y_pred, color='red')

    for xi, yi, ypi in zip(x, y, y_pred):
        plt.plot([xi, xi], [yi, ypi], color='gray', linestyle='--')
        plt.fill_between([xi - 0.05, xi + 0.05], yi, ypi, color='red', alpha=0.3)

    plt.title('Квадраты ошибок')
    plt.xlabel('X')
    plt.ylabel('Y')

def main():
    file_path = input("Введите путь к CSV файлу: ")
    data = read_csv_file(file_path)
    show_statistics(data)

    print(f"\nСтолбцы в файле: {list(data.columns)}")
    x_column = input("Выберите столбец для X: ")
    y_column = input("Выберите столбец для Y: ")

    x = data[x_column].values
    y = data[y_column].values

    plot_original_data(x, y)
    m, b = least_squares(x, y)
    plot_regression_line(x, y, m, b)
    plot_error_squares(x, y, m, b)

    plt.show()

if __name__ == "__main__":
    main()

