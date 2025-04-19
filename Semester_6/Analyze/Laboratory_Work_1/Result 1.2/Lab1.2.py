import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Загрузка данных
df = pd.read_csv("c:/Users/vtakk/OneDrive/Рабочий стол/Университет/3 курс/Анализ данных/Лабораторная 1/ML1ext/insurance_miptstats.csv")
print("Первые строки таблицы:")
print(df.head())

# 2. Выбор признаков: bmi -> charges
X = df["bmi"].values.reshape(-1, 1)
y = df["charges"].values

# 3. Разделение на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Линейная регрессия с помощью scikit-learn
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_sklearn = model.predict(X_test)

print("\n Scikit-learn коэффициенты:")
print(f"  Угловой коэффициент (slope): {model.coef_[0]}")
print(f"  Смещение (intercept): {model.intercept_}")

# 5. Собственная реализация МНК
def least_squares(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - m * x_mean
    return m, b

m_custom, b_custom = least_squares(X_train.flatten(), y_train)
y_pred_custom = m_custom * X_test.flatten() + b_custom

print("\n Собственный метод МНК:")
print(f"  Угловой коэффициент (slope): {m_custom}")
print(f"  Смещение (intercept): {b_custom}")

# 6. График
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color="blue", label="Тестовые данные")
plt.plot(X_test, y_pred_sklearn, color="red", label="Scikit-learn линия")
plt.plot(X_test, y_pred_custom, color="green", linestyle="--", label="Собственная линия")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.legend()
plt.title("Линейная регрессия: BMI -> Charges")
plt.grid(True)
plt.show()

# 7. Таблица предсказаний
results = pd.DataFrame({
    "BMI": X_test.flatten(),
    "y_true (charges)": y_test,
    "y_pred_sklearn": y_pred_sklearn,
    "y_pred_custom": y_pred_custom
})

print("\n Таблица результатов (первые 10 строк):")
print(results.head(10))

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression 
from sklearn import metrics


print("Result for 1.3")

regressor = LinearRegression() 
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

print("MAE %.2f" % metrics.mean_absolute_error(y_test, y_pred))

print("MAPE %.2f" % (100 * (np.abs(y_test - y_pred) / y_test).mean()))
