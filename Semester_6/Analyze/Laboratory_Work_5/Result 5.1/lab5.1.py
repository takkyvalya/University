import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, roc_curve, auc, precision_recall_curve,
                           confusion_matrix)
import graphviz

# 1. Загрузка данных
df = pd.read_csv('c:/Users/vtakk/OneDrive/Рабочий стол/Университет/3 курс/Анализ данных/Лабораторная 5.1/diabetes.csv')
print("Первые 5 строк датасета:")
print(df.head())

# Разделение на признаки и целевую переменную
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Сравнение моделей
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1': f1_score(y_test, y_pred)
    }
    
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        metrics['ROC AUC'] = auc(fpr, tpr)
    
    print(f"\nМетрики для {model_name}:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    
    return metrics

# Логистическая регрессия
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_metrics = evaluate_model(lr, X_test, y_test, "Logistic Regression")

# Решающее дерево (по умолчанию)
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
tree_metrics = evaluate_model(tree, X_test, y_test, "Decision Tree")

# Вывод о лучшей модели
print("\nВывод:")
if tree_metrics['Accuracy'] > lr_metrics['Accuracy']:
    print("Решающее дерево показало лучшую точность (Accuracy) по сравнению с логистической регрессией.")
else:
    print("Логистическая регрессия показала лучшую точность (Accuracy) по сравнению с решающим деревом.")

# 2. Исследование зависимости метрики от глубины дерева
max_depths = range(1, 21)
f1_scores = []

for depth in max_depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f1_scores.append(f1_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(max_depths, f1_scores, marker='o')
plt.xlabel('Глубина дерева')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от глубины дерева')
plt.grid()
plt.show()

# 3. Оптимальная модель и визуализация
optimal_depth = max_depths[np.argmax(f1_scores)]
print(f"\nОптимальная глубина дерева: {optimal_depth}")

# Обучение модели с оптимальной глубиной
optimal_tree = DecisionTreeClassifier(max_depth=optimal_depth, random_state=42)
optimal_tree.fit(X_train, y_train)

# Визуализация дерева
dot_data = export_graphviz(optimal_tree, out_file=None, 
                         feature_names=X.columns,
                         class_names=['No Diabetes', 'Diabetes'],
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("diabetes_tree")  # Сохраняет в файл diabetes_tree.pdf

# Важность признаков
plt.figure(figsize=(10, 6))
plt.barh(X.columns, optimal_tree.feature_importances_)
plt.xlabel('Важность признака')
plt.title('Важность признаков в модели')
plt.show()

# PR и ROC кривые
y_proba = optimal_tree.predict_proba(X_test)[:, 1]

# PR кривая
precision, recall, _ = precision_recall_curve(y_test, y_proba)
plt.figure(figsize=(8, 6))
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('PR-кривая')
plt.grid()
plt.show()

# ROC кривая
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC-кривая')
plt.legend()
plt.grid()
plt.show()

# 4. Опциональное задание: исследование max_features
max_features_range = range(1, len(X.columns)+1)
f1_scores_features = []

for n_features in max_features_range:
    model = DecisionTreeClassifier(max_depth=optimal_depth, 
                                 max_features=n_features, 
                                 random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f1_scores_features.append(f1_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(max_features_range, f1_scores_features, marker='o')
plt.xlabel('max_features')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от max_features')
plt.xticks(max_features_range)
plt.grid()
plt.show()