import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Загрузка и исследование датасета Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 1. Визуализация зависимостей
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for target, color in zip([0, 1, 2], ['red', 'green', 'blue']):
    subset = df[df['target'] == target]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], 
                c=color, label=iris.target_names[target])
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.legend()

plt.subplot(1, 2, 2)
for target, color in zip([0, 1, 2], ['red', 'green', 'blue']):
    subset = df[df['target'] == target]
    plt.scatter(subset['petal length (cm)'], subset['petal width (cm)'], 
                c=color, label=iris.target_names[target])
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend()

plt.suptitle('Зависимости для разных сортов ириса')
plt.show()

# 2. Pairplot для всего датасета
sns.pairplot(df, hue='target', palette='viridis')
plt.suptitle('Pairplot для датасета Iris', y=1.02)
plt.show()

# 3. Подготовка двух датасетов
# Датсет 1: setosa (0) и versicolor (1)
df1 = df[df['target'].isin([0, 1])]
X1 = df1[iris.feature_names]
y1 = df1['target']

# Датсет 2: versicolor (1) и virginica (2)
df2 = df[df['target'].isin([1, 2])]
X2 = df2[iris.feature_names]
y2 = df2['target']

# 4-8. Обучение и оценка моделей для обоих датасетов
def train_and_evaluate(X, y, dataset_name):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = LogisticRegression(random_state=0)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    accuracy = clf.score(X_test, y_test)
    
    print(f"\nРезультаты для датасета {dataset_name}:")
    print(f"Точность модели: {accuracy:.2f}")
    print(f"Коэффициенты: {clf.coef_}")
    print(f"Пересечение: {clf.intercept_}")

train_and_evaluate(X1, y1, "Setosa vs Versicolor")
train_and_evaluate(X2, y2, "Versicolor vs Virginica")

# 9. Генерация и классификация искусственного датасета
X_gen, y_gen = make_classification(n_samples=1000, n_features=2, n_redundant=0,
                                 n_informative=2, random_state=1, n_clusters_per_class=1)

plt.figure(figsize=(8, 6))
plt.scatter(X_gen[:, 0], X_gen[:, 1], c=y_gen, cmap='viridis', alpha=0.7)
plt.title('Сгенерированный датасет для бинарной классификации')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.colorbar()
plt.show()

# Обучение модели на сгенерированных данных
X_train, X_test, y_train, y_test = train_test_split(X_gen, y_gen, test_size=0.2, random_state=42)

clf_gen = LogisticRegression(random_state=0)
clf_gen.fit(X_train, y_train)

y_pred_gen = clf_gen.predict(X_test)
accuracy_gen = clf_gen.score(X_test, y_test)

print("\nРезультаты для сгенерированного датасета:")
print(f"Точность модели: {accuracy_gen:.2f}")
print(f"Коэффициенты: {clf_gen.coef_}")
print(f"Пересечение: {clf_gen.intercept_}")

# Визуализация разделяющей границы
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.4, cmap='viridis')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', alpha=0.7)
    plt.title('Разделяющая граница логистической регрессии')
    plt.xlabel('Признак 1')
    plt.ylabel('Признак 2')

plt.figure(figsize=(8, 6))
plot_decision_boundary(X_gen, y_gen, clf_gen)
plt.show()