import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.datasets import load_diabetes

# 1. Загрузка и подготовка данных
df = pd.read_csv('c:/Users/vtakk/OneDrive/Рабочий стол/Университет/3 курс/Анализ данных/Лабораторная 5.1/diabetes.csv')
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Исследование Random Forest
def evaluate_rf():
    # 2.1 Исследование зависимости от глубины деревьев
    depths = range(1, 21)
    accuracies = []
    f1_scores = []
    
    for depth in depths:
        rf = RandomForestClassifier(max_depth=depth, n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))
        f1_scores.append(f1_score(y_test, y_pred))
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(depths, accuracies, marker='o')
    plt.xlabel('Глубина деревьев')
    plt.ylabel('Accuracy')
    plt.title('Зависимость accuracy от глубины деревьев')
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(depths, f1_scores, marker='o', color='orange')
    plt.xlabel('Глубина деревьев')
    plt.ylabel('F1-score')
    plt.title('Зависимость F1-score от глубины деревьев')
    plt.grid()
    plt.tight_layout()
    plt.show()

    # 2.2 Исследование зависимости от количества признаков
    max_features_range = range(1, len(X.columns)+1)
    accuracies_feat = []
    f1_scores_feat = []
    
    for n_features in max_features_range:
        rf = RandomForestClassifier(max_features=n_features, n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        accuracies_feat.append(accuracy_score(y_test, y_pred))
        f1_scores_feat.append(f1_score(y_test, y_pred))
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(max_features_range, accuracies_feat, marker='o')
    plt.xlabel('Количество признаков')
    plt.ylabel('Accuracy')
    plt.title('Зависимость accuracy от количества признаков')
    plt.xticks(max_features_range)
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(max_features_range, f1_scores_feat, marker='o', color='orange')
    plt.xlabel('Количество признаков')
    plt.ylabel('F1-score')
    plt.title('Зависимость F1-score от количества признаков')
    plt.xticks(max_features_range)
    plt.grid()
    plt.tight_layout()
    plt.show()

    # 2.3 Исследование зависимости от количества деревьев
    n_estimators_range = [10, 50, 100, 150, 200, 250, 300]
    accuracies_est = []
    f1_scores_est = []
    times = []
    
    for n_est in n_estimators_range:
        start_time = time.time()
        rf = RandomForestClassifier(n_estimators=n_est, random_state=42)
        rf.fit(X_train, y_train)
        times.append(time.time() - start_time)
        y_pred = rf.predict(X_test)
        accuracies_est.append(accuracy_score(y_test, y_pred))
        f1_scores_est.append(f1_score(y_test, y_pred))
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    color = 'tab:blue'
    ax1.set_xlabel('Количество деревьев')
    ax1.set_ylabel('Accuracy/F1', color=color)
    ax1.plot(n_estimators_range, accuracies_est, marker='o', label='Accuracy', color=color)
    ax1.plot(n_estimators_range, f1_scores_est, marker='o', label='F1-score', linestyle='--', color='tab:orange')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')
    
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Время обучения (с)', color=color)
    ax2.plot(n_estimators_range, times, marker='s', color=color, label='Время обучения')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')
    
    plt.title('Зависимость accuracy/F1-score и времени обучения от количества деревьев')
    plt.grid()
    plt.show()

    return {
        'best_depth': depths[np.argmax(f1_scores)],
        'best_n_features': max_features_range[np.argmax(f1_scores_feat)],
        'best_n_estimators': n_estimators_range[np.argmax(f1_scores_est)],
        'best_f1': max(f1_scores_est)
    }

rf_results = evaluate_rf()

# 3. Исследование XGBoost
def evaluate_xgboost():
    # Подбор параметров вручную
    params = {
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.3],
        'n_estimators': [50, 100, 150],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0]
    }
    
    best_f1 = 0
    best_params = {}
    results = []
    
    for max_depth in params['max_depth']:
        for lr in params['learning_rate']:
            for n_est in params['n_estimators']:
                for subsample in params['subsample']:
                    for colsample in params['colsample_bytree']:
                        start_time = time.time()
                        xgb = XGBClassifier(
                            max_depth=max_depth,
                            learning_rate=lr,
                            n_estimators=n_est,
                            subsample=subsample,
                            colsample_bytree=colsample,
                            random_state=42,
                            eval_metric='logloss',
                            use_label_encoder=False
                        )
                        xgb.fit(X_train, y_train)
                        train_time = time.time() - start_time
                        
                        y_pred = xgb.predict(X_test)
                        f1 = f1_score(y_test, y_pred)
                        accuracy = accuracy_score(y_test, y_pred)
                        
                        results.append({
                            'max_depth': max_depth,
                            'learning_rate': lr,
                            'n_estimators': n_est,
                            'subsample': subsample,
                            'colsample_bytree': colsample,
                            'f1': f1,
                            'accuracy': accuracy,
                            'time': train_time
                        })
                        
                        if f1 > best_f1:
                            best_f1 = f1
                            best_params = {
                                'max_depth': max_depth,
                                'learning_rate': lr,
                                'n_estimators': n_est,
                                'subsample': subsample,
                                'colsample_bytree': colsample
                            }
    
    # Вывод лучших параметров
    print("\nЛучшие параметры XGBoost:")
    for param, value in best_params.items():
        print(f"{param}: {value}")
    print(f"Лучший F1-score: {best_f1:.4f}")
    
    # Обучение модели с лучшими параметрами
    best_xgb = XGBClassifier(
        **best_params,
        random_state=42,
        eval_metric='logloss',
        use_label_encoder=False
    )
    best_xgb.fit(X_train, y_train)
    y_pred = best_xgb.predict(X_test)
    
    print("\nОтчет о классификации:")
    print(classification_report(y_test, y_pred))
    
    print("\nМатрица ошибок:")
    print(confusion_matrix(y_test, y_pred))
    
    return {
        'best_params': best_params,
        'best_f1': best_f1,
        'results': pd.DataFrame(results)
    }

xgb_results = evaluate_xgboost()

# 4. Сравнение моделей
print("\nСравнение моделей:")
print(f"Random Forest - Лучший F1-score: {rf_results['best_f1']:.4f}")
print(f"XGBoost - Лучший F1-score: {xgb_results['best_f1']:.4f}")

# Визуализация важности признаков
rf_best = RandomForestClassifier(
    max_depth=rf_results['best_depth'],
    max_features=rf_results['best_n_features'],
    n_estimators=rf_results['best_n_estimators'],
    random_state=42
)
rf_best.fit(X_train, y_train)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.barh(X.columns, rf_best.feature_importances_)
plt.title('Важность признаков (Random Forest)')
plt.xlabel('Важность')

plt.subplot(1, 2, 2)
plt.barh(X.columns, best_xgb.feature_importances_)
plt.title('Важность признаков (XGBoost)')
plt.xlabel('Важность')
plt.tight_layout()
plt.show()