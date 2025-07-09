# Optimización de Hiperparámetros y Validación de Modelos

## Objetivos de Aprendizaje

Al finalizar esta sesión, los estudiantes podrán:
- Comprender la importancia de la optimización de hiperparámetros
- Implementar técnicas de búsqueda de hiperparámetros (Grid Search, Random Search)
- Aplicar validación cruzada robusta
- Evaluar y comparar modelos de manera estadísticamente válida
- Interpretar y visualizar resultados de optimización

## 1. Fundamentos de Hiperparámetros

### ¿Qué son los Hiperparámetros?

Los hiperparámetros son configuraciones del algoritmo que no se aprenden durante el entrenamiento, sino que deben ser establecidos antes de entrenar el modelo. Controlan el comportamiento del algoritmo de aprendizaje.

#### Diferencia entre Parámetros e Hiperparámetros

**Parámetros:**
- Se aprenden durante el entrenamiento
- Ejemplos: pesos en redes neuronales, coeficientes en regresión lineal
- Valores optimizados automáticamente

**Hiperparámetros:**
- Se establecen antes del entrenamiento
- Ejemplos: learning rate, número de árboles, C en SVM
- Requieren optimización manual o automática

### Importancia de la Optimización

- **Rendimiento:** Hiperparámetros óptimos mejoran significativamente el rendimiento
- **Generalización:** Previenen overfitting y underfitting
- **Eficiencia:** Reducen tiempo de entrenamiento y recursos computacionales
- **Robustez:** Hacen el modelo más estable ante variaciones en datos

## 2. Hiperparámetros por Algoritmo

### Regresión Logística
```python
LogisticRegression(
    C=1.0,                    # Inverso de la regularización
    penalty='l2',             # Tipo de regularización (l1, l2, elasticnet)
    solver='lbfgs',           # Algoritmo de optimización
    max_iter=100,             # Número máximo de iteraciones
    class_weight=None         # Peso de las clases
)
```

### Random Forest
```python
RandomForestClassifier(
    n_estimators=100,         # Número de árboles
    max_depth=None,           # Profundidad máxima de árboles
    min_samples_split=2,      # Mínimo de muestras para dividir
    min_samples_leaf=1,       # Mínimo de muestras en hoja
    max_features='auto',      # Número de características por división
    bootstrap=True,           # Muestreo con reemplazo
    class_weight=None         # Peso de las clases
)
```

### SVM (Support Vector Machine)
```python
SVC(
    C=1.0,                    # Parámetro de regularización
    kernel='rbf',             # Tipo de kernel (linear, poly, rbf, sigmoid)
    gamma='scale',            # Coeficiente del kernel
    degree=3,                 # Grado del kernel polinomial
    class_weight=None         # Peso de las clases
)
```

### Gradient Boosting
```python
GradientBoostingClassifier(
    n_estimators=100,         # Número de boosting stages
    learning_rate=0.1,        # Tasa de aprendizaje
    max_depth=3,              # Profundidad máxima de árboles
    min_samples_split=2,      # Mínimo de muestras para dividir
    min_samples_leaf=1,       # Mínimo de muestras en hoja
    subsample=1.0,            # Fracción de muestras por árbol
    max_features=None         # Número de características por división
)
```

### Redes Neuronales (MLP)
```python
MLPClassifier(
    hidden_layer_sizes=(100,), # Tamaño de capas ocultas
    activation='relu',         # Función de activación
    solver='adam',             # Optimizador
    alpha=0.0001,             # Parámetro de regularización L2
    learning_rate='constant',  # Estrategia de learning rate
    learning_rate_init=0.001,  # Learning rate inicial
    max_iter=200,             # Número máximo de iteraciones
    early_stopping=False      # Parada temprana
)
```

## 3. Estrategias de Optimización

### Grid Search (Búsqueda Exhaustiva)

Grid Search evalúa todas las combinaciones posibles de hiperparámetros en un grid predefinido.

```python
from sklearn.model_selection import GridSearchCV

# Definir grid de hiperparámetros
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Configurar Grid Search
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,                    # Validación cruzada de 5 folds
    scoring='accuracy',      # Métrica de evaluación
    n_jobs=-1,              # Usar todos los cores disponibles
    verbose=1               # Mostrar progreso
)

# Ejecutar búsqueda
grid_search.fit(X_train, y_train)

# Mejores parámetros
best_params = grid_search.best_params_
best_score = grid_search.best_score_
```

**Ventajas:**
- Garantiza encontrar el óptimo en el grid
- Fácil de implementar y entender
- Reproducible

**Desventajas:**
- Computacionalmente costoso
- Crecimiento exponencial con número de parámetros
- Limitado al grid predefinido

### Random Search (Búsqueda Aleatoria)

Random Search evalúa combinaciones aleatorias de hiperparámetros.

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Definir distribuciones de hiperparámetros
param_distributions = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': uniform(0.1, 0.9)
}

# Configurar Random Search
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=100,             # Número de iteraciones
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

# Ejecutar búsqueda
random_search.fit(X_train, y_train)
```

**Ventajas:**
- Más eficiente que Grid Search
- Puede encontrar mejores soluciones
- Escala mejor con más parámetros

**Desventajas:**
- No garantiza encontrar el óptimo
- Requiere más configuración
- Resultados pueden variar

### Optimización Bayesiana

Usa información de evaluaciones previas para seleccionar próximos hiperparámetros.

```python
# Usando Optuna (instalación: pip install optuna)
import optuna

def objective(trial):
    # Definir hiperparámetros a optimizar
    n_estimators = trial.suggest_int('n_estimators', 50, 200)
    max_depth = trial.suggest_int('max_depth', 3, 20)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 20)
    
    # Crear modelo
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    
    # Evaluación con validación cruzada
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    return scores.mean()

# Crear estudio y optimizar
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

# Mejores parámetros
best_params = study.best_params
best_score = study.best_value
```

## 4. Validación Cruzada Avanzada

### Validación Cruzada Estratificada

Mantiene la proporción de clases en cada fold.

```python
from sklearn.model_selection import StratifiedKFold

# Configurar validación cruzada estratificada
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Evaluar modelo con validación cruzada
scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='accuracy')

print(f"Accuracy: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
```

### Validación Cruzada Temporal

Para datos con componente temporal.

```python
from sklearn.model_selection import TimeSeriesSplit

# Configurar validación temporal
tscv = TimeSeriesSplit(n_splits=5)

# Evaluar modelo preservando orden temporal
scores = cross_val_score(model, X_train, y_train, cv=tscv, scoring='accuracy')
```

### Validación Cruzada Anidada

Combina selección de modelo con evaluación de rendimiento.

```python
from sklearn.model_selection import cross_validate

# Validación cruzada anidada
def nested_cv(model, param_grid, X, y, cv_outer=5, cv_inner=3):
    outer_scores = []
    
    # Loop externo para evaluación
    for train_idx, test_idx in StratifiedKFold(n_splits=cv_outer, shuffle=True, random_state=42).split(X, y):
        X_train_outer, X_test_outer = X[train_idx], X[test_idx]
        y_train_outer, y_test_outer = y[train_idx], y[test_idx]
        
        # Loop interno para selección de hiperparámetros
        grid_search = GridSearchCV(
            model, param_grid, cv=cv_inner, scoring='accuracy'
        )
        grid_search.fit(X_train_outer, y_train_outer)
        
        # Evaluar en conjunto de prueba externo
        score = grid_search.score(X_test_outer, y_test_outer)
        outer_scores.append(score)
    
    return np.array(outer_scores)

# Ejecutar validación cruzada anidada
nested_scores = nested_cv(RandomForestClassifier(random_state=42), param_grid, X_train, y_train)
print(f"Nested CV Score: {nested_scores.mean():.3f} (+/- {nested_scores.std() * 2:.3f})")
```

## 5. Métricas de Evaluación Avanzadas

### Métricas para Clasificación Multiclase

```python
from sklearn.metrics import classification_report, confusion_matrix

# Reporte completo de clasificación
report = classification_report(y_test, y_pred, target_names=['Home', 'Draw', 'Away'])
print(report)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print(cm)
```

### Métricas Personalizadas

```python
from sklearn.metrics import make_scorer

def custom_football_score(y_true, y_pred):
    """Métrica personalizada que penaliza más los errores en partidos importantes"""
    correct = (y_true == y_pred).sum()
    total = len(y_true)
    
    # Penalizar errores en partidos importantes (simplificado)
    penalty = 0
    for i in range(len(y_true)):
        if y_true[i] != y_pred[i]:
            penalty += 1.5  # Penalización por error
    
    return correct / total - penalty / (total * 10)

# Usar métrica personalizada
custom_scorer = make_scorer(custom_football_score)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring=custom_scorer)
```

## 6. Análisis de Curvas de Aprendizaje

### Curva de Validación

Analiza el efecto de un hiperparámetro en el rendimiento.

```python
from sklearn.model_selection import validation_curve

# Curva de validación para n_estimators
param_range = [10, 50, 100, 200, 500]
train_scores, test_scores = validation_curve(
    RandomForestClassifier(random_state=42),
    X_train, y_train,
    param_name='n_estimators',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)

# Visualizar curva
plt.figure(figsize=(10, 6))
plt.plot(param_range, train_scores.mean(axis=1), 'o-', label='Training')
plt.plot(param_range, test_scores.mean(axis=1), 'o-', label='Validation')
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.title('Validation Curve')
plt.legend()
plt.grid(True)
plt.show()
```

### Curva de Aprendizaje

Analiza el efecto del tamaño del conjunto de entrenamiento.

```python
from sklearn.model_selection import learning_curve

# Curva de aprendizaje
train_sizes, train_scores, test_scores = learning_curve(
    RandomForestClassifier(random_state=42),
    X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5,
    scoring='accuracy'
)

# Visualizar curva
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), 'o-', label='Training')
plt.plot(train_sizes, test_scores.mean(axis=1), 'o-', label='Validation')
plt.xlabel('Training Set Size')
plt.ylabel('Accuracy')
plt.title('Learning Curve')
plt.legend()
plt.grid(True)
plt.show()
```

## 7. Detección de Overfitting y Underfitting

### Indicadores de Overfitting
- Gran diferencia entre accuracy de entrenamiento y validación
- Mejora continua en entrenamiento pero estancamiento en validación
- Modelo muy complejo para el tamaño de datos

### Indicadores de Underfitting
- Baja accuracy tanto en entrenamiento como en validación
- Modelo demasiado simple para capturar patrones
- Convergencia prematura

### Técnicas de Regularización

```python
# Regularización L1 y L2 en Regresión Logística
from sklearn.linear_model import LogisticRegression

# L1 (Lasso) - Selección automática de características
model_l1 = LogisticRegression(penalty='l1', solver='liblinear', C=0.1)

# L2 (Ridge) - Reducción de pesos
model_l2 = LogisticRegression(penalty='l2', C=0.1)

# Elastic Net - Combinación de L1 y L2
model_elastic = LogisticRegression(penalty='elasticnet', l1_ratio=0.5, solver='saga', C=0.1)
```

## 8. Consideraciones Prácticas

### Tiempo Computacional vs. Rendimiento

```python
import time

# Medir tiempo de optimización
start_time = time.time()
grid_search.fit(X_train, y_train)
optimization_time = time.time() - start_time

print(f"Tiempo de optimización: {optimization_time:.2f} segundos")
print(f"Mejora en accuracy: {grid_search.best_score_ - baseline_score:.3f}")
print(f"Costo por punto de mejora: {optimization_time / (grid_search.best_score_ - baseline_score):.2f} seg/punto")
```

### Estrategias de Optimización Eficiente

1. **Búsqueda Coarse-to-Fine:**
   - Primero búsqueda amplia con pocos valores
   - Luego búsqueda fina en región prometedora

2. **Paralelización:**
   - Usar `n_jobs=-1` para usar todos los cores
   - Considerar distribución en múltiples máquinas

3. **Parada Temprana:**
   - Detener búsqueda si no hay mejora significativa
   - Usar validación en conjunto holdout

### Reproducibilidad

```python
# Asegurar reproducibilidad
np.random.seed(42)

# Usar random_state en todos los componentes
model = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(model, param_grid, cv=5, random_state=42)
```

## 9. Ejemplo Completo: Optimización para Fútbol

```python
# Ejemplo completo de optimización para predicción de resultados
def optimize_football_model(X_train, y_train, X_test, y_test):
    """Optimización completa para modelo de fútbol"""
    
    # Definir modelos y grids
    models_and_grids = {
        'Random Forest': {
            'model': RandomForestClassifier(random_state=42),
            'params': {
                'n_estimators': [50, 100, 200],
                'max_depth': [5, 10, 15, None],
                'min_samples_split': [2, 5, 10],
                'class_weight': [None, 'balanced']
            }
        },
        'SVM': {
            'model': SVC(random_state=42, probability=True),
            'params': {
                'C': [0.1, 1, 10, 100],
                'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
                'class_weight': [None, 'balanced']
            }
        },
        'Gradient Boosting': {
            'model': GradientBoostingClassifier(random_state=42),
            'params': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 5, 7],
                'subsample': [0.8, 1.0]
            }
        }
    }
    
    # Optimizar cada modelo
    best_models = {}
    results = {}
    
    for name, config in models_and_grids.items():
        print(f"\n🔄 Optimizando {name}...")
        
        # Grid search con validación cruzada
        grid_search = GridSearchCV(
            config['model'],
            config['params'],
            cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
            scoring='accuracy',
            n_jobs=-1,
            verbose=0
        )
        
        # Entrenar
        grid_search.fit(X_train, y_train)
        
        # Evaluar en conjunto de prueba
        test_score = grid_search.score(X_test, y_test)
        
        # Guardar resultados
        best_models[name] = grid_search.best_estimator_
        results[name] = {
            'best_params': grid_search.best_params_,
            'cv_score': grid_search.best_score_,
            'test_score': test_score,
            'model': grid_search.best_estimator_
        }
        
        print(f"✅ {name} - CV: {grid_search.best_score_:.3f}, Test: {test_score:.3f}")
    
    # Seleccionar mejor modelo
    best_model_name = max(results.keys(), key=lambda k: results[k]['test_score'])
    best_model = results[best_model_name]['model']
    
    print(f"\n🏆 Mejor modelo: {best_model_name}")
    print(f"   Test accuracy: {results[best_model_name]['test_score']:.3f}")
    
    return best_model, results

# Ejecutar optimización
best_model, optimization_results = optimize_football_model(X_train, y_train, X_test, y_test)
```

## 10. Mejores Prácticas

### Do's ✅
- Usar validación cruzada estratificada
- Separar datos de entrenamiento/validación/prueba
- Documentar todos los hiperparámetros probados
- Considerar tiempo computacional vs. mejora
- Validar estabilidad de resultados

### Don'ts ❌
- No usar datos de prueba para optimización
- No ignorar overfitting
- No optimizar solo una métrica
- No olvidar reproducibilidad
- No sobre-optimizar en dataset pequeño

## Próxima Sesión

En la siguiente sesión exploraremos técnicas de interpretabilidad de modelos y análisis de importancia de variables para entender mejor cómo nuestros modelos toman decisiones.

## Recursos Adicionales

- **Documentación scikit-learn:** Hyperparameter tuning
- **Paper:** "Random Search for Hyper-Parameter Optimization" (Bergstra & Bengio)
- **Herramienta:** Optuna documentation
- **Tutorial:** "Hyperparameter Tuning with Python" (Towards Data Science)
