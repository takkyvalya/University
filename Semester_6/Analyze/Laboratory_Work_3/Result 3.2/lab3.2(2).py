import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, confusion_matrix, roc_curve, auc, 
                           precision_recall_curve, PrecisionRecallDisplay)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Загрузка и предобработка данных
titanic = pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')
titanic_clean = titanic.dropna().drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
le = LabelEncoder()
titanic_clean['Sex'] = le.fit_transform(titanic_clean['Sex'])
titanic_clean['Embarked'] = le.fit_transform(titanic_clean['Embarked']) + 1

X = titanic_clean.drop('Survived', axis=1)
y = titanic_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Функция для оценки модели
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X_test)
    
    # Основные метрики
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1': f1_score(y_test, y_pred)
    }
    
    # ROC AUC
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    metrics['ROC AUC'] = roc_auc
    
    # Визуализация
    plt.figure(figsize=(15, 4))
    
    # Матрица ошибок
    plt.subplot(1, 3, 1)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Матрица ошибок\n{model.__class__.__name__}')
    
    # PR кривая
    plt.subplot(1, 3, 2)
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    plt.plot(recall, precision)
    plt.title(f'PR кривая\nAUC={auc(recall, precision):.2f}')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    
    # ROC кривая
    plt.subplot(1, 3, 3)
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title(f'ROC кривая\n{model.__class__.__name__}')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return metrics

# Инициализация моделей
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": SVC(probability=True),
    "KNN": KNeighborsClassifier()
}

# Обучение и оценка моделей
results = {}
for name, model in models.items():
    print(f"\n=== {name} ===")
    model.fit(X_train, y_train)
    results[name] = evaluate_model(model, X_test, y_test)
    print(pd.Series(results[name]).to_string())

# Сравнение моделей
results_df = pd.DataFrame(results).T
print("\nСравнение моделей:")
print(results_df)

# Вывод о наилучшей модели
best_model = results_df['ROC AUC'].idxmax()
print(f"\nНаилучшая модель: {best_model} с AUC-ROC = {results_df.loc[best_model, 'ROC AUC']:.3f}")
print("Основание для вывода:")
print("1. ROC AUC - наиболее важная метрика для несбалансированных данных")
print("2. F1-score учитывает и precision, и recall")
print("3. Accuracy показывает общую точность")