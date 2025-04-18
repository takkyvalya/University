import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, confusion_matrix, precision_recall_curve, 
                           roc_curve, auc, PrecisionRecallDisplay, RocCurveDisplay)
from sklearn.preprocessing import LabelEncoder

# Загрузка и предобработка данных
titanic = pd.read_csv('c:/Users/vtakk/OneDrive/Рабочий стол/Университет/3 курс/Анализ данных/Лабораторная 3/LabML_3_2/Titanic.csv')
titanic_clean = titanic.dropna().drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
le = LabelEncoder()
titanic_clean['Sex'] = le.fit_transform(titanic_clean['Sex'])
titanic_clean['Embarked'] = le.fit_transform(titanic_clean['Embarked']) + 1

# Разделение данных
X = titanic_clean.drop('Survived', axis=1)
y = titanic_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
y_proba = lr.predict_proba(X_test)[:, 1]

# Вычисление метрик
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Метрики классификации:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")

# Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Не выжил', 'Выжил'], 
            yticklabels=['Не выжил', 'Выжил'])
plt.title('Матрица ошибок')
plt.ylabel('Истинный класс')
plt.xlabel('Предсказанный класс')
plt.show()

# Кривая PR
precision_curve, recall_curve, _ = precision_recall_curve(y_test, y_proba)
plt.figure(figsize=(8, 6))
plt.plot(recall_curve, precision_curve, color='darkorange')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('PR-кривая')
plt.grid()
plt.show()

# Кривая ROC
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', label=f'ROC кривая (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC-кривая')
plt.legend()
plt.grid()
plt.show()

# Вывод о качестве модели
print("\nВывод о качестве модели:")
print("1. Accuracy показывает общую точность модели.")
print("2. Precision указывает на долю верно предсказанных выживших среди всех предсказанных выживших.")
print("3. Recall показывает, какую долю выживших модель смогла правильно идентифицировать.")
print("4. F1-score балансирует между precision и recall.")
print(f"5. AUC-ROC = {roc_auc:.2f} показывает хорошее качество классификации.")