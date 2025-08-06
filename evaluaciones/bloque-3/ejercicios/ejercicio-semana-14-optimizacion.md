# Ejercicio Semana 14: Feature Engineering y Optimización

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 14 - Optimización Avanzada de Modelos  
**Tiempo estimado:** 60 minutos  
**Tipo:** Individual  
**Puntuación:** 100 puntos (25 puntos por parte)

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Implementar** técnicas de feature engineering para datos deportivos
2. **Crear** variables derivadas más predictivas a partir de datos existentes
3. **Aplicar** métodos de selección automática de características
4. **Optimizar** modelos mediante pipelines de procesamiento avanzado

## Contexto del Problema

Trabajaremos como científicos de datos para **Manchester City**, desarrollando el sistema de feature engineering más avanzado del fútbol. Nuestro objetivo es crear variables inteligentes que capturen patrones complejos y mejoren significativamente la capacidad predictiva de nuestros modelos.

---

# Ejercicio Integrador: Laboratorio de Feature Engineering Manchester City

## Parte 1: Creación de Variables Avanzadas (25 puntos)

### Objetivo
Desarrollar un sistema completo de feature engineering que transforme datos básicos en variables altamente predictivas.

### Instrucciones Detalladas

**Paso 1:** Configura laboratorio de feature engineering:

```python
# Configuración del laboratorio de feature engineering Manchester City
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, RFE, SelectFromModel
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score
import warnings
warnings.filterwarnings('ignore')

# Configuración visual Manchester City
colores_city = ['#6CABDD', '#1C2C5B', '#FFFFFF', '#FFD700']
sns.set_theme(style="whitegrid", palette=colores_city)
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11

print("=== LABORATORIO FEATURE ENGINEERING MANCHESTER CITY ===")
print("Sistema avanzado de creación de variables iniciado")
print("¡Transformando datos básicos en insights poderosos!")
```

**Paso 2:** Genera dataset base y crea variables derivadas:

```python
# Dataset base y feature engineering avanzado

# TU CÓDIGO AQUÍ:
# 1. Crear dataset base de 600 partidos del Manchester City
# 2. Incluir variables temporales y contextuales:
#    - posesion_balon: % posesión en el partido
#    - pases_completados: Número de pases completados
#    - tiros_a_puerta: Tiros al arco en el partido
#    - corners_favor: Corners a favor
#    - faltas_cometidas: Faltas cometidas por el equipo
#    - minutos_ventaja: Minutos jugando con ventaja en marcador
# 3. Crear variables derivadas sofisticadas:
#    - eficiencia_posesion: tiros_a_puerta / posesion_balon
#    - intensidad_ofensiva: (tiros_a_puerta + corners_favor) / pases_completados
#    - control_partido: posesion_balon * (1 - faltas_cometidas/100)
#    - dominio_temporal: minutos_ventaja / 90
# 4. Variable objetivo: 'victoria_dominante' (victoria con >60% posesión)

np.random.seed(789)  # Para reproducibilidad

# Generar datos base del Manchester City
partidos_city = []
for i in range(600):
    # Variables base del estilo Manchester City
    posesion_balon = np.random.normal(65, 8)  # City suele tener alta posesión
    pases_completados = np.random.normal(600, 100)
    tiros_a_puerta = np.random.normal(6, 2)
    corners_favor = np.random.normal(7, 3)
    faltas_cometidas = np.random.normal(12, 4)
    minutos_ventaja = np.random.normal(25, 15)
    
    # Asegurar valores realistas
    posesion_balon = max(30, min(80, posesion_balon))
    pases_completados = max(200, pases_completados)
    tiros_a_puerta = max(0, tiros_a_puerta)
    corners_favor = max(0, corners_favor)
    faltas_cometidas = max(0, faltas_cometidas)
    minutos_ventaja = max(0, min(90, minutos_ventaja))
    
    # Variables derivadas (feature engineering)
    eficiencia_posesion = tiros_a_puerta / (posesion_balon + 1)
    intensidad_ofensiva = (tiros_a_puerta + corners_favor) / (pases_completados + 1) * 1000
    control_partido = posesion_balon * (1 - faltas_cometidas/100)
    dominio_temporal = minutos_ventaja / 90
    
    # Probabilidad de victoria dominante
    prob_victoria_dominante = (
        posesion_balon * 0.02 + 
        eficiencia_posesion * 5 + 
        intensidad_ofensiva * 2 + 
        control_partido * 0.01 + 
        dominio_temporal * 0.3
    ) / 10
    
    prob_victoria_dominante = max(0, min(1, prob_victoria_dominante))
    
    partido = {
        # Variables base
        'posesion_balon': posesion_balon,
        'pases_completados': pases_completados,
        'tiros_a_puerta': tiros_a_puerta,
        'corners_favor': corners_favor,
        'faltas_cometidas': faltas_cometidas,
        'minutos_ventaja': minutos_ventaja,
        
        # Variables derivadas
        'eficiencia_posesion': eficiencia_posesion,
        'intensidad_ofensiva': intensidad_ofensiva,
        'control_partido': control_partido,
        'dominio_temporal': dominio_temporal,
        
        # Variable objetivo
        'victoria_dominante': 1 if (np.random.random() < prob_victoria_dominante and posesion_balon > 60) else 0
    }
    partidos_city.append(partido)

df_city = pd.DataFrame(partidos_city)

print("=== DATASET MANCHESTER CITY GENERADO ===")
print(f"Total partidos: {len(df_city)}")
print(f"Distribución victorias dominantes: {df_city['victoria_dominante'].value_counts()}")
print(f"Porcentaje victorias dominantes: {df_city['victoria_dominante'].mean():.1%}")

# Mostrar correlaciones de variables derivadas
print("\n=== CORRELACIONES VARIABLES DERIVADAS ===")
variables_derivadas = ['eficiencia_posesion', 'intensidad_ofensiva', 'control_partido', 'dominio_temporal']
for var in variables_derivadas:
    corr = df_city[var].corr(df_city['victoria_dominante'])
    print(f"{var}: {corr:.3f}")
```

**Paso 3:** Implementa feature engineering automático:

```python
# Feature engineering automático avanzado

# TU CÓDIGO AQUÍ:
# 1. Crear interacciones entre variables (productos)
# 2. Implementar transformaciones polinomiales
# 3. Generar ratios y proporciones adicionales
# 4. Crear variables categóricas discretizadas
# 5. Evaluar impacto de nuevas variables

# Crear interacciones importantes
df_city['posesion_x_eficiencia'] = df_city['posesion_balon'] * df_city['eficiencia_posesion']
df_city['tiros_x_control'] = df_city['tiros_a_puerta'] * df_city['control_partido']
df_city['corners_x_dominio'] = df_city['corners_favor'] * df_city['dominio_temporal']

# Ratios adicionales
df_city['tiros_por_posesion'] = df_city['tiros_a_puerta'] / (df_city['posesion_balon'] + 1)
df_city['pases_por_minuto_ventaja'] = df_city['pases_completados'] / (df_city['minutos_ventaja'] + 1)

# Variables categóricas discretizadas
df_city['categoria_posesion'] = pd.cut(df_city['posesion_balon'], 
                                      bins=[0, 50, 65, 80, 100], 
                                      labels=['Baja', 'Media', 'Alta', 'Muy_Alta'])

df_city['categoria_eficiencia'] = pd.cut(df_city['eficiencia_posesion'], 
                                        bins=[0, 0.05, 0.1, 0.15, 1], 
                                        labels=['Baja', 'Media', 'Alta', 'Muy_Alta'])

# One-hot encoding para variables categóricas
df_city_encoded = pd.get_dummies(df_city, columns=['categoria_posesion', 'categoria_eficiencia'], prefix=['pos', 'ef'])

print("=== FEATURE ENGINEERING AUTOMÁTICO COMPLETADO ===")
print(f"Variables originales: 10")
print(f"Variables después de feature engineering: {len(df_city_encoded.columns) - 1}")  # -1 por variable objetivo

# Mostrar las nuevas variables más correlacionadas
print("\n=== TOP 10 VARIABLES MÁS CORRELACIONADAS ===")
correlaciones = df_city_encoded.corr()['victoria_dominante'].abs().sort_values(ascending=False)
top_10 = correlaciones.head(11)[1:]  # Excluir la variable objetivo
for i, (var, corr) in enumerate(top_10.items(), 1):
    print(f"{i:2d}. {var}: {corr:.3f}")
```

### Criterios de Evaluación
- **Implementación correcta de variables derivadas** (15 puntos)
- **Feature engineering automático completo** (10 puntos)

---

## Parte 2: Selección Automática de Características (25 puntos)

### Objetivo
Implementar múltiples técnicas de selección de características para identificar las variables más predictivas.

### Instrucciones Detalladas

**Paso 4:** Aplica métodos de selección de características:

```python
# Métodos de selección de características

# TU CÓDIGO AQUÍ:
# 1. Preparar datos para selección de características
# 2. Aplicar SelectKBest con diferentes valores de k
# 3. Implementar Recursive Feature Elimination (RFE)
# 4. Usar SelectFromModel con RandomForest
# 5. Comparar resultados de diferentes métodos

# Preparar datos
features_numericas = df_city_encoded.select_dtypes(include=[np.number]).columns.tolist()
features_numericas.remove('victoria_dominante')

X = df_city_encoded[features_numericas]
y = df_city_encoded['victoria_dominante']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("=== SELECCIÓN DE CARACTERÍSTICAS ===")
print(f"Total características disponibles: {len(features_numericas)}")

# Método 1: SelectKBest
selector_kbest = SelectKBest(f_classif, k=15)
X_train_kbest = selector_kbest.fit_transform(X_train, y_train)
X_test_kbest = selector_kbest.transform(X_test)

# Obtener nombres de características seleccionadas
caracteristicas_kbest = [features_numericas[i] for i in selector_kbest.get_support(indices=True)]

print(f"\n📊 SELECTKBEST (k=15):")
for i, char in enumerate(caracteristicas_kbest[:10], 1):
    score = selector_kbest.scores_[features_numericas.index(char)]
    print(f"{i:2d}. {char}: {score:.2f}")

# Método 2: Recursive Feature Elimination
rf_base = RandomForestClassifier(n_estimators=50, random_state=42)
selector_rfe = RFE(rf_base, n_features_to_select=15)
X_train_rfe = selector_rfe.fit_transform(X_train, y_train)
X_test_rfe = selector_rfe.transform(X_test)

caracteristicas_rfe = [features_numericas[i] for i in selector_rfe.get_support(indices=True)]

print(f"\n🔄 RECURSIVE FEATURE ELIMINATION:")
for i, char in enumerate(caracteristicas_rfe[:10], 1):
    ranking = selector_rfe.ranking_[features_numericas.index(char)]
    print(f"{i:2d}. {char} (ranking: {ranking})")

# Método 3: SelectFromModel
rf_selector = RandomForestClassifier(n_estimators=100, random_state=42)
selector_model = SelectFromModel(rf_selector, threshold='median')
X_train_model = selector_model.fit_transform(X_train, y_train)
X_test_model = selector_model.transform(X_test)

caracteristicas_model = [features_numericas[i] for i in selector_model.get_support(indices=True)]

print(f"\n🌳 SELECTFROMMODEL (RandomForest):")
importancias = rf_selector.fit(X_train, y_train).feature_importances_
importancias_sorted = sorted(zip(features_numericas, importancias), key=lambda x: x[1], reverse=True)

for i, (char, imp) in enumerate(importancias_sorted[:10], 1):
    print(f"{i:2d}. {char}: {imp:.4f}")

print(f"\n📈 RESUMEN DE SELECCIÓN:")
print(f"SelectKBest seleccionó: {len(caracteristicas_kbest)} características")
print(f"RFE seleccionó: {len(caracteristicas_rfe)} características")
print(f"SelectFromModel seleccionó: {len(caracteristicas_model)} características")
```

**Paso 5:** Evalúa impacto de selección de características:

```python
# Evaluación del impacto de selección de características

# TU CÓDIGO AQUÍ:
# 1. Entrenar modelos con todas las características
# 2. Entrenar modelos con características seleccionadas por cada método
# 3. Comparar rendimiento (accuracy y F1-score)
# 4. Analizar tiempo de entrenamiento
# 5. Identificar método óptimo de selección

import time

# Modelo base con todas las características
rf_completo = RandomForestClassifier(n_estimators=100, random_state=42)

start_time = time.time()
rf_completo.fit(X_train, y_train)
tiempo_completo = time.time() - start_time

y_pred_completo = rf_completo.predict(X_test)
accuracy_completo = accuracy_score(y_test, y_pred_completo)
f1_completo = f1_score(y_test, y_pred_completo)

print("=== COMPARACIÓN DE RENDIMIENTO ===")
print(f"MODELO COMPLETO ({len(features_numericas)} características):")
print(f"  Accuracy: {accuracy_completo:.3f}")
print(f"  F1-Score: {f1_completo:.3f}")
print(f"  Tiempo entrenamiento: {tiempo_completo:.3f}s")

# Evaluación con cada método de selección
metodos_seleccion = {
    'SelectKBest': (X_train_kbest, X_test_kbest, caracteristicas_kbest),
    'RFE': (X_train_rfe, X_test_rfe, caracteristicas_rfe),
    'SelectFromModel': (X_train_model, X_test_model, caracteristicas_model)
}

resultados_seleccion = {}

for nombre, (X_tr, X_te, caracteristicas) in metodos_seleccion.items():
    rf_seleccionado = RandomForestClassifier(n_estimators=100, random_state=42)
    
    start_time = time.time()
    rf_seleccionado.fit(X_tr, y_train)
    tiempo_entrenamiento = time.time() - start_time
    
    y_pred = rf_seleccionado.predict(X_te)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    resultados_seleccion[nombre] = {
        'accuracy': accuracy,
        'f1': f1,
        'tiempo': tiempo_entrenamiento,
        'n_caracteristicas': len(caracteristicas),
        'caracteristicas': caracteristicas
    }
    
    print(f"\n{nombre.upper()} ({len(caracteristicas)} características):")
    print(f"  Accuracy: {accuracy:.3f}")
    print(f"  F1-Score: {f1:.3f}")
    print(f"  Tiempo entrenamiento: {tiempo_entrenamiento:.3f}s")
    print(f"  Mejora F1: {f1 - f1_completo:+.3f}")

# Visualización comparativa
metodos = ['Completo'] + list(resultados_seleccion.keys())
accuracies = [accuracy_completo] + [r['accuracy'] for r in resultados_seleccion.values()]
f1_scores = [f1_completo] + [r['f1'] for r in resultados_seleccion.values()]
tiempos = [tiempo_completo] + [r['tiempo'] for r in resultados_seleccion.values()]
n_features = [len(features_numericas)] + [r['n_caracteristicas'] for r in resultados_seleccion.values()]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Accuracy
axes[0, 0].bar(metodos, accuracies, color=colores_city[:len(metodos)])
axes[0, 0].set_title('Accuracy por Método de Selección')
axes[0, 0].set_ylabel('Accuracy')
axes[0, 0].tick_params(axis='x', rotation=45)

# F1-Score
axes[0, 1].bar(metodos, f1_scores, color=colores_city[:len(metodos)])
axes[0, 1].set_title('F1-Score por Método de Selección')
axes[0, 1].set_ylabel('F1-Score')
axes[0, 1].tick_params(axis='x', rotation=45)

# Tiempo de entrenamiento
axes[1, 0].bar(metodos, tiempos, color='orange', alpha=0.7)
axes[1, 0].set_title('Tiempo de Entrenamiento')
axes[1, 0].set_ylabel('Segundos')
axes[1, 0].tick_params(axis='x', rotation=45)

# Número de características
axes[1, 1].bar(metodos, n_features, color='green', alpha=0.7)
axes[1, 1].set_title('Número de Características')
axes[1, 1].set_ylabel('N° Características')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.suptitle('Comparación de Métodos de Selección: Manchester City', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Identificar mejor método
mejor_metodo = max(resultados_seleccion.items(), key=lambda x: x[1]['f1'])
print(f"\n🏆 MEJOR MÉTODO: {mejor_metodo[0]}")
print(f"F1-Score: {mejor_metodo[1]['f1']:.3f}")
print(f"Características: {mejor_metodo[1]['n_caracteristicas']}")
```

### Criterios de Evaluación
- **Implementación correcta de múltiples métodos de selección** (15 puntos)
- **Evaluación comparativa detallada** (10 puntos)

---

## Parte 3: Pipeline de Procesamiento Avanzado (25 puntos)

### Objetivo
Crear un pipeline completo que integre preprocesamiento, selección de características y modelado.

### Instrucciones Detalladas

**Paso 6:** Construye pipeline de machine learning completo:

```python
# Pipeline completo de machine learning

# TU CÓDIGO AQUÍ:
# 1. Crear pipeline con StandardScaler, selección de características y modelo
# 2. Implementar validación cruzada del pipeline
# 3. Optimizar hiperparámetros del pipeline completo
# 4. Comparar con modelo simple sin pipeline
# 5. Evaluar robustez del pipeline

from sklearn.model_selection import GridSearchCV, cross_val_score

# Pipeline completo
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(f_classif)),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Parámetros para optimización
param_grid = {
    'selector__k': [10, 15, 20, 25],
    'classifier__n_estimators': [50, 100, 150],
    'classifier__max_depth': [None, 10, 20]
}

print("=== PIPELINE DE MACHINE LEARNING ===")
print("Optimizando hiperparámetros del pipeline completo...")

# Búsqueda de mejores parámetros
grid_search = GridSearchCV(
    pipeline, 
    param_grid, 
    cv=5, 
    scoring='f1',
    n_jobs=-1,
    verbose=0
)

# Entrenar pipeline optimizado
grid_search.fit(X_train, y_train)

# Mejores parámetros
print(f"\n🎯 MEJORES PARÁMETROS:")
for param, valor in grid_search.best_params_.items():
    print(f"  {param}: {valor}")

# Evaluación del pipeline optimizado
y_pred_pipeline = grid_search.predict(X_test)
accuracy_pipeline = accuracy_score(y_test, y_pred_pipeline)
f1_pipeline = f1_score(y_test, y_pred_pipeline)

print(f"\n📊 RENDIMIENTO PIPELINE OPTIMIZADO:")
print(f"  Accuracy: {accuracy_pipeline:.3f}")
print(f"  F1-Score: {f1_pipeline:.3f}")
print(f"  Mejora vs modelo completo: {f1_pipeline - f1_completo:+.3f}")

# Validación cruzada del pipeline
cv_scores = cross_val_score(grid_search.best_estimator_, X, y, cv=5, scoring='f1')
print(f"\n🔄 VALIDACIÓN CRUZADA PIPELINE:")
print(f"  F1-Score CV: {cv_scores.mean():.3f} (±{cv_scores.std():.3f})")
print(f"  Scores individuales: {[f'{score:.3f}' for score in cv_scores]}")

# Análisis de características seleccionadas por pipeline
best_selector = grid_search.best_estimator_.named_steps['selector']
caracteristicas_pipeline = [features_numericas[i] for i in best_selector.get_support(indices=True)]

print(f"\n🔧 CARACTERÍSTICAS SELECCIONADAS POR PIPELINE ({len(caracteristicas_pipeline)}):")
scores_pipeline = best_selector.scores_
for i, char in enumerate(caracteristicas_pipeline[:10], 1):
    score = scores_pipeline[features_numericas.index(char)]
    print(f"{i:2d}. {char}: {score:.2f}")
```

**Paso 7:** Crea sistema de monitoreo de características:

```python
# Sistema de monitoreo de características

# TU CÓDIGO AQUÍ:
# 1. Analizar estabilidad de selección de características
# 2. Evaluar importancia relativa de cada tipo de variable
# 3. Crear métricas de calidad del feature engineering
# 4. Generar reporte de impacto de variables derivadas
# 5. Establecer sistema de alertas para degradación

# Análisis de estabilidad de selección
print("=== ANÁLISIS DE ESTABILIDAD DE CARACTERÍSTICAS ===")

# Comparar características seleccionadas por diferentes métodos
caracteristicas_conjuntos = {
    'SelectKBest': set(caracteristicas_kbest),
    'RFE': set(caracteristicas_rfe),
    'SelectFromModel': set(caracteristicas_model),
    'Pipeline': set(caracteristicas_pipeline)
}

# Características que aparecen en múltiples métodos
interseccion_todos = set.intersection(*caracteristicas_conjuntos.values())
print(f"\n🎯 CARACTERÍSTICAS ESTABLES (en todos los métodos):")
for char in sorted(interseccion_todos):
    print(f"  • {char}")

# Análisis por tipo de variable
variables_originales = ['posesion_balon', 'pases_completados', 'tiros_a_puerta', 'corners_favor', 'faltas_cometidas', 'minutos_ventaja']
variables_derivadas = ['eficiencia_posesion', 'intensidad_ofensiva', 'control_partido', 'dominio_temporal']
variables_interacciones = ['posesion_x_eficiencia', 'tiros_x_control', 'corners_x_dominio', 'tiros_por_posesion', 'pases_por_minuto_ventaja']

tipos_variables = {
    'Originales': variables_originales,
    'Derivadas': variables_derivadas,
    'Interacciones': variables_interacciones
}

print(f"\n📊 ANÁLISIS POR TIPO DE VARIABLE:")
caracteristicas_importantes = set(caracteristicas_pipeline)

for tipo, variables in tipos_variables.items():
    seleccionadas = [var for var in variables if var in caracteristicas_importantes]
    porcentaje = len(seleccionadas) / len(variables) * 100 if variables else 0
    
    print(f"\n{tipo.upper()}:")
    print(f"  Total: {len(variables)}")
    print(f"  Seleccionadas: {len(seleccionadas)} ({porcentaje:.1f}%)")
    if seleccionadas:
        print(f"  Variables: {', '.join(seleccionadas)}")

# Métricas de calidad del feature engineering
mejora_feature_engineering = f1_pipeline - f1_completo
reduccion_caracteristicas = (len(features_numericas) - len(caracteristicas_pipeline)) / len(features_numericas)

print(f"\n🏆 MÉTRICAS DE CALIDAD FEATURE ENGINEERING:")
print(f"  Mejora F1-Score: {mejora_feature_engineering:+.3f}")
print(f"  Reducción características: {reduccion_caracteristicas:.1%}")
print(f"  Eficiencia: {mejora_feature_engineering / (1 - reduccion_caracteristicas):.3f}")

# Reporte de impacto de variables derivadas
print(f"\n📈 IMPACTO DE VARIABLES DERIVADAS:")
variables_derivadas_seleccionadas = [var for var in variables_derivadas if var in caracteristicas_importantes]
if variables_derivadas_seleccionadas:
    for var in variables_derivadas_seleccionadas:
        correlacion = df_city[var].corr(df_city['victoria_dominante'])
        print(f"  • {var}: correlación {correlacion:.3f}")
else:
    print("  • Ninguna variable derivada fue seleccionada")

# Visualización final del pipeline
plt.figure(figsize=(16, 10))

# Subplot 1: Comparación de rendimiento
plt.subplot(2, 3, 1)
metodos_completos = ['Modelo Base', 'SelectKBest', 'RFE', 'SelectFromModel', 'Pipeline Optimizado']
f1_completos = [f1_completo, resultados_seleccion['SelectKBest']['f1'], 
                resultados_seleccion['RFE']['f1'], resultados_seleccion['SelectFromModel']['f1'], f1_pipeline]

bars = plt.bar(metodos_completos, f1_completos, color=colores_city[:len(metodos_completos)])
plt.title('F1-Score por Método')
plt.ylabel('F1-Score')
plt.xticks(rotation=45)

# Añadir valores en barras
for bar, f1 in zip(bars, f1_completos):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{f1:.3f}', ha='center', fontweight='bold')

# Subplot 2: Número de características
plt.subplot(2, 3, 2)
n_caracteristicas_completo = [len(features_numericas), len(caracteristicas_kbest), 
                              len(caracteristicas_rfe), len(caracteristicas_model), len(caracteristicas_pipeline)]

plt.bar(metodos_completos, n_caracteristicas_completo, color='orange', alpha=0.7)
plt.title('Número de Características')
plt.ylabel('N° Características')
plt.xticks(rotation=45)

# Subplot 3: Validación cruzada pipeline
plt.subplot(2, 3, 3)
plt.plot(range(1, 6), cv_scores, marker='o', linewidth=2, markersize=8, color='#6CABDD')
plt.axhline(y=cv_scores.mean(), color='red', linestyle='--', label=f'Media: {cv_scores.mean():.3f}')
plt.title('Validación Cruzada Pipeline')
plt.xlabel('Fold')
plt.ylabel('F1-Score')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 4: Importancia de tipos de variables
plt.subplot(2, 3, 4)
tipos = list(tipos_variables.keys())
porcentajes_seleccion = []
for tipo, variables in tipos_variables.items():
    seleccionadas = [var for var in variables if var in caracteristicas_importantes]
    porcentaje = len(seleccionadas) / len(variables) * 100 if variables else 0
    porcentajes_seleccion.append(porcentaje)

plt.bar(tipos, porcentajes_seleccion, color='green', alpha=0.7)
plt.title('% Selección por Tipo de Variable')
plt.ylabel('% Seleccionadas')

# Subplot 5: Correlaciones top variables
plt.subplot(2, 3, 5)
top_vars = caracteristicas_pipeline[:8]
correlaciones_top = [df_city_encoded[var].corr(df_city_encoded['victoria_dominante']) for var in top_vars]

plt.barh(range(len(top_vars)), correlaciones_top, color='purple', alpha=0.7)
plt.yticks(range(len(top_vars)), [var[:20] + '...' if len(var) > 20 else var for var in top_vars])
plt.title('Correlaciones Top Variables')
plt.xlabel('Correlación')

# Subplot 6: Eficiencia del sistema
plt.subplot(2, 3, 6)
metricas_eficiencia = ['Mejora F1', 'Reducción Características', 'Eficiencia Global']
valores_eficiencia = [mejora_feature_engineering * 10, reduccion_caracteristicas * 100, 
                      (mejora_feature_engineering / (1 - reduccion_caracteristicas)) * 10]

plt.bar(metricas_eficiencia, valores_eficiencia, color=['blue', 'orange', 'green'], alpha=0.7)
plt.title('Métricas de Eficiencia')
plt.ylabel('Valor (escalado)')
plt.xticks(rotation=45)

plt.suptitle('Dashboard Feature Engineering Manchester City', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Criterios de Evaluación
- **Pipeline completo funcionando correctamente** (15 puntos)
- **Sistema de monitoreo y análisis de calidad** (10 puntos)

---

## Parte 4: Reporte de Optimización y Recomendaciones (25 puntos)

### Objetivo
Generar un reporte ejecutivo que documente el proceso de optimización y proporcione recomendaciones estratégicas.

### Instrucciones Detalladas

**Paso 8:** Genera reporte ejecutivo de optimización:

```python
# Reporte ejecutivo completo de feature engineering y optimización

# TU CÓDIGO AQUÍ:
# 1. Resumir proceso completo de feature engineering
# 2. Documentar mejoras obtenidas en cada etapa
# 3. Recomendar variables más importantes para el Manchester City
# 4. Establecer protocolo de mantenimiento del sistema
# 5. Proponer próximas etapas de desarrollo

print("=" * 80)
print("MANCHESTER CITY - REPORTE FEATURE ENGINEERING Y OPTIMIZACIÓN")
print("Sistema Avanzado de Creación y Selección de Variables Predictivas")
print("=" * 80)

print("\n🔬 PROCESO DE FEATURE ENGINEERING IMPLEMENTADO:")
print("1. Generación de variables derivadas a partir de datos base")
print("2. Creación de interacciones entre variables clave")
print("3. Implementación de ratios y proporciones avanzadas")
print("4. Discretización inteligente de variables continuas")
print("5. Selección automática de características óptimas")

print(f"\n📊 RESULTADOS CUANTITATIVOS:")
print(f"• Variables iniciales: {len(features_numericas)}")
print(f"• Variables después de FE: {len(df_city_encoded.columns) - 1}")
print(f"• Variables seleccionadas finales: {len(caracteristicas_pipeline)}")
print(f"• Mejora F1-Score: {mejora_feature_engineering:+.3f} ({mejora_feature_engineering/f1_completo*100:+.1f}%)")
print(f"• Reducción dimensionalidad: {reduccion_caracteristicas:.1%}")
print(f"• Eficiencia del sistema: {(mejora_feature_engineering / (1 - reduccion_caracteristicas)):.3f}")

print(f"\n🏆 VARIABLES MÁS IMPORTANTES PARA MANCHESTER CITY:")
# Top 10 características del pipeline
caracteristicas_top = caracteristicas_pipeline[:10]
for i, var in enumerate(caracteristicas_top, 1):
    if var in df_city.columns:
        correlacion = df_city[var].corr(df_city['victoria_dominante'])
        tipo = "Original" if var in variables_originales else "Derivada" if var in variables_derivadas else "Interacción"
        print(f"{i:2d}. {var} (Corr: {correlacion:.3f}, Tipo: {tipo})")

print(f"\n⚽ INSIGHTS ESTRATÉGICOS PARA EL MANCHESTER CITY:")

# Análisis de variables derivadas más importantes
variables_city_importantes = [var for var in caracteristicas_pipeline if var in variables_derivadas + variables_interacciones]

print("🎯 Variables derivadas clave:")
if 'eficiencia_posesion' in variables_city_importantes:
    print("  • EFICIENCIA DE POSESIÓN: Convertir posesión en ocasiones de gol")
if 'control_partido' in variables_city_importantes:
    print("  • CONTROL DE PARTIDO: Dominar sin cometer faltas innecesarias")
if 'intensidad_ofensiva' in variables_city_importantes:
    print("  • INTENSIDAD OFENSIVA: Maximizar tiros y corners por pase")
if 'dominio_temporal' in variables_city_importantes:
    print("  • DOMINIO TEMPORAL: Mantener ventaja en el marcador")

print("\n🔧 RECOMENDACIONES TÁCTICAS:")
print("1. Priorizar eficiencia sobre posesión pura")
print("2. Mantener disciplina para evitar faltas que rompan el control")
print("3. Intensificar presión ofensiva en los primeros 30 minutos")
print("4. Desarrollar estrategias para convertir corners en goles")

print(f"\n🚀 PROTOCOLO DE MANTENIMIENTO DEL SISTEMA:")
print("1. Reentrenar pipeline cada 15 partidos")
print("2. Monitorear degradación de variables derivadas mensualmente")
print("3. Ajustar umbrales de selección según cambios tácticos")
print("4. Validar estabilidad de características trimestralmente")

print(f"\n📈 PRÓXIMAS ETAPAS DE DESARROLLO:")
print("• Incorporar datos de jugadores individuales")
print("• Añadir variables contextuales (rival, competición, clima)")
print("• Desarrollar feature engineering específico por tipo de rival")
print("• Implementar selección de características en tiempo real")

print(f"\n⚙️ ESPECIFICACIONES TÉCNICAS DEL SISTEMA:")
print(f"• Pipeline: StandardScaler → SelectKBest(k={grid_search.best_params_['selector__k']}) → RandomForest")
print(f"• Hiperparámetros óptimos: {grid_search.best_params_}")
print(f"• Validación cruzada: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
print(f"• Características estables: {len(interseccion_todos)} variables")

print(f"\n🎖️ CERTIFICACIÓN DE CALIDAD:")
robustez = "Alta" if cv_scores.std() < 0.02 else "Media" if cv_scores.std() < 0.05 else "Baja"
mejora_significativa = "Sí" if mejora_feature_engineering > 0.02 else "No"

print(f"• Robustez del modelo: {robustez}")
print(f"• Mejora significativa: {mejora_significativa}")
print(f"• Estabilidad de características: {len(interseccion_todos)}/{len(caracteristicas_pipeline)} estables")
print(f"• Eficiencia computacional: Reducción {reduccion_caracteristicas:.1%} de variables")

# Generar resumen ejecutivo final
print("\n" + "="*50)
print("RESUMEN EJECUTIVO")
print("="*50)

if mejora_feature_engineering > 0.02:
    print("✅ Sistema de feature engineering EXITOSO")
    print(f"   Mejora significativa de {mejora_feature_engineering:.3f} en F1-Score")
else:
    print("⚠️  Sistema de feature engineering MODERADO")
    print(f"   Mejora limitada de {mejora_feature_engineering:.3f} en F1-Score")

if cv_scores.std() < 0.03:
    print("✅ Pipeline ROBUSTO y estable")
else:
    print("⚠️  Pipeline requiere mayor estabilización")

print(f"🎯 Recomendación: Implementar para partidos importantes")
print(f"📊 Confianza del sistema: {cv_scores.mean():.1%}")
print(f"🔧 Mantenimiento: Cada {15} partidos")
```

### Criterios de Evaluación
- **Reporte ejecutivo completo y detallado** (15 puntos)
- **Recomendaciones estratégicas fundamentadas** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Implementación correcta de feature engineering avanzado
- Aplicación apropiada de métodos de selección de características
- Pipeline de ML funcionando correctamente
- Sistema de monitoreo y validación implementado

### Aplicación Práctica (30 puntos)
- Variables derivadas relevantes para el contexto del Manchester City
- Interpretación correcta de resultados de selección
- Recomendaciones tácticas basadas en insights de datos
- Protocolo de mantenimiento realista y útil

### Claridad y Documentación (30 puntos)
- Explicaciones claras del proceso de feature engineering
- Análisis comparativo bien estructurado
- Reporte ejecutivo profesional y comprensible
- Código bien documentado y organizado

## Instrucciones de Entrega

1. **Implementa el pipeline completo** de feature engineering
2. **Incluye comparación detallada** entre métodos de selección
3. **Verifica funcionamiento** del sistema de monitoreo
4. **Guarda como:** `[matricula]-ejercicio-semana-14.ipynb`
5. **Entrega antes del final de Semana 14**

## Recursos de Apoyo

- Notebook de la Semana 14: `feature-engineering-optimizacion.ipynb`
- Documentación scikit-learn: Feature selection y pipelines
- Guía de feature engineering para datos deportivos

---

**¡Desarrolla el sistema de feature engineering más avanzado del fútbol y lleva al Manchester City al siguiente nivel de análisis predictivo!** ⚽🔬

**1.2 Dataset expandido con fechas**

- Crea un dataset con 1500+ partidos distribuidos en 3 temporadas
- Incluye fechas realistas y equipos consistentes
- Variables base: `fecha`, `equipo_local`, `equipo_visitante`, `goles_local`, `goles_visitante`, `posesion_local`, `tiros_local`, etc.

**1.3 Variables de racha reciente**

Crea variables basadas en los últimos N partidos:

- `racha_victorias_local_3`: Victorias en los últimos 3 partidos como local
- `promedio_goles_local_5`: Promedio de goles en los últimos 5 partidos como local
- `tendencia_goles_local`: ¿Está mejorando o empeorando? (regresión simple)
- `partidos_sin_ganar_local`: Partidos consecutivos sin victoria como local

**1.4 Variables de forma reciente**

```python
def calcular_forma_reciente(df, equipo, fecha, ventana=5):
    """
    Calcula indicadores de forma reciente para un equipo
    """
    # Tu código aquí
    pass
```

- Implementa función para calcular forma reciente automáticamente
- Variables: `forma_local_3`, `forma_visitante_3` (puntos promedio recientes)
- `volatilidad_reciente`: Varianza en el rendimiento reciente

**1.5 Variables de fatiga y descanso**

- `dias_descanso_local`: Días desde el último partido
- `partidos_recientes_local`: Partidos jugados en los últimos 14 días
- `fatiga_acumulada`: Índice de fatiga basado en intensidad de partidos recientes

### Entregables

- Dataset expandido con fechas realistas
- Funciones automatizadas para calcular variables temporales
- Al menos 8 nuevas variables temporales creadas
- Análisis de correlación entre nuevas variables y resultado

---

## Ejercicio 2: Feature Engineering Avanzado - Variables Contextuales (1.5 horas)

### Contexto

El contexto del partido importa enormemente: rivalidades, importancia del partido, historial directo, etc. Estas variables capturan aspectos psicológicos y estratégicos del fútbol.

### Tareas

**2.1 Variables de historial directo**

- `historial_local_vs_visitante`: Porcentaje de victorias históricas del local contra el visitante
- `goles_promedio_duelo`: Promedio de goles en enfrentamientos directos históricos
- `ultimo_resultado_directo`: Resultado del último enfrentamiento (victoria/empate/derrota)

**2.2 Variables de contexto competitivo**

- `diferencia_posicion_tabla`: Diferencia en posición de tabla entre equipos
- `presion_resultado`: ¿Equipo necesita puntos desesperadamente? (basado en objetivos de temporada)
- `importancia_partido`: Escala 1-5 basada en contexto (derby, final de temporada, etc.)

**2.3 Variables de análisis de rival**

```python
def analizar_fortaleza_rival(df, equipo_local, equipo_visitante, fecha):
    """
    Analiza las fortalezas del rival específico
    """
    # Tu código aquí
    pass
```

- `fortaleza_rival_ofensiva`: ¿Qué tan bueno es el rival atacando?
- `fortaleza_rival_defensiva`: ¿Qué tan bueno es el rival defendiendo?
- `compatibilidad_estilos`: ¿El estilo del local favorece contra este rival?

**2.4 Variables de momentum**

- `momentum_local`: Tendencia reciente en rendimiento (improving/declining/stable)
- `confianza_equipo`: Índice basado en resultados recientes y expectativas
- `sorpresa_factor`: ¿Qué tan inesperado sería una victoria/derrota?

**2.5 Variables agregadas inteligentes**

- `ventaja_casa_historica`: Ventaja histórica específica de este estadio
- `rendimiento_vs_similares`: Rendimiento vs equipos de fuerza similar
- `consistencia_local`: ¿Qué tan predecible es este equipo en casa?

### Entregables

- Funciones para calcular variables contextuales automáticamente
- Al menos 10 nuevas variables de contexto
- Análisis de cuáles variables son más predictivas
- Visualización de distribución de nuevas variables

---

## Ejercicio 3: Selección Automática de Variables (1 hora)

### Contexto

Con tantas variables nuevas, necesitamos identificar automáticamente cuáles son realmente útiles y cuáles solo añaden ruido. La selección de features es crucial para modelos eficientes.

### Tareas

**3.1 Análisis de correlación y multicolinealidad**

```python
# Matriz de correlación de todas las variables
correlation_matrix = df_features.corr()

# Identificar variables altamente correlacionadas
def find_correlated_features(corr_matrix, threshold=0.8):
    # Tu código aquí
    pass
```

- Identifica pares de variables con correlación > 0.8
- ¿Qué variables están capturando información similar?
- Decide cuáles conservar en cada par correlacionado

**3.2 Selección univariada (SelectKBest)**

```python
from sklearn.feature_selection import SelectKBest, f_classif

# Selecciona las K mejores variables usando pruebas estadísticas
selector_univariado = SelectKBest(score_func=f_classif, k=15)
X_selected = selector_univariado.fit_transform(X, y)
```

- Aplica SelectKBest para identificar las 15 mejores variables
- ¿Cuáles variables tienen mayor poder predictivo individual?
- Compara con tu intuición deportiva

**3.3 Selección recursiva (RFE)**

```python
from sklearn.feature_selection import RFE

# Eliminación recursiva con Random Forest
estimator = RandomForestClassifier(n_estimators=100, random_state=42)
selector_rfe = RFE(estimator, n_features_to_select=15, step=1)
```

- Usa RFE para seleccionar variables de manera iterativa
- ¿Coincide con SelectKBest en las variables importantes?
- ¿Qué método da mejores resultados?

**3.4 Importancia de variables con Random Forest**

- Entrena Random Forest con todas las variables
- Extrae importancia de cada variable
- Crea ranking y visualización de importancia
- Selecciona top 15 variables por importancia

**3.5 Comparación de métodos de selección**

- Compara las 15 variables seleccionadas por cada método
- ¿Hay consenso en las variables más importantes?
- Entrena modelos con cada selección y compara rendimiento

### Entregables

- Análisis de correlación y multicolinealidad
- Tres métodos de selección de variables implementados
- Comparación de rendimiento entre métodos
- Selección final de variables óptimas

---

## Ejercicio 4: Pipeline de Procesamiento Optimizado (1 hora)

### Contexto

En producción, necesitamos procesar automáticamente nuevos datos con las mismas transformaciones. Los pipelines nos permiten encadenar preprocessing, feature engineering y modelado de manera reproducible.

### Tareas

**4.1 Pipeline básico de preprocessing**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Pipeline de preprocessing
preprocessor = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
```

**4.2 Pipeline completo con feature engineering**

```python
from sklearn.base import BaseEstimator, TransformerMixin

class FootballFeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Tu código de feature engineering aquí
        return X_transformed
```

- Crea clase personalizada para feature engineering automático
- Incluye todas las transformaciones de variables temporales y contextuales

**4.3 Pipeline completo integrado**

```python
# Pipeline completo: preprocessing + feature engineering + modelo
pipeline_completo = Pipeline([
    ('feature_engineering', FootballFeatureEngineer()),
    ('preprocessing', preprocessor),
    ('feature_selection', SelectKBest(k=15)),
    ('modelo', RandomForestClassifier(n_estimators=200))
])
```

**4.4 Optimización de hiperparámetros del pipeline**

```python
from sklearn.model_selection import GridSearchCV

# Optimiza todo el pipeline
param_grid = {
    'feature_selection__k': [10, 15, 20],
    'modelo__n_estimators': [100, 200, 300],
    'modelo__max_depth': [10, 15, 20]
}

grid_search = GridSearchCV(pipeline_completo, param_grid, cv=5)
```

**4.5 Evaluación del pipeline optimizado**

- Compara rendimiento antes y después del feature engineering
- ¿Cuánto mejoraron las métricas principales?
- ¿Qué componentes del pipeline aportaron más mejora?

### Entregables

- Pipeline completo funcional y reproducible
- Clase personalizada de feature engineering
- Optimización de hiperparámetros implementada
- Comparación cuantitativa de mejoras obtenidas

---

## Ejercicio Bonus: Validación en Datos Completamente Nuevos (30 minutos)

### Contexto

La prueba definitiva es aplicar tu pipeline optimizado a datos que nunca ha visto, simulando el uso en producción.

### Tareas

**Bonus.1 Simulación de nuevos datos**

- Crea un nuevo conjunto de 100 partidos simulados
- Aplica tu pipeline completo para generar predicciones
- ¿Qué tan confiable es el modelo en datos completamente nuevos?

**Bonus.2 Análisis de degradación**

- ¿El rendimiento se mantiene en datos nuevos?
- ¿Qué variables siguen siendo importantes?
- ¿Hay signos de overfitting en tu pipeline?

**Bonus.3 Recomendaciones para producción**

- ¿Qué modificaciones harías para uso en producción?
- ¿Cómo monitorizarías la calidad de las predicciones?
- ¿Con qué frecuencia reentrenarías el modelo?

### Entregables

- Validación en datos completamente nuevos
- Análisis de estabilidad del modelo
- Recomendaciones para implementación en producción

---

## Criterios de Evaluación

### Innovación en Feature Engineering (40%)

- **Creatividad:** Variables nuevas e inteligentes creadas
- **Relevancia deportiva:** Features que tienen sentido futbolístico
- **Implementación técnica:** Código robusto y eficiente

### Metodología y Optimización (35%)

- **Selección de variables:** Uso apropiado de técnicas de selección
- **Pipeline design:** Arquitectura limpia y reproducible
- **Optimización:** Mejoras cuantificables en rendimiento

### Análisis y Validación (25%)

- **Comparación sistemática:** Antes vs después del feature engineering
- **Validación robusta:** Uso de técnicas de validación apropiadas
- **Interpretación:** Comprensión de qué mejoras funcionan y por qué

## Recursos de Apoyo

### Documentación Técnica

- [Scikit-learn Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html)
- [Pipeline and ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html)
- [Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html)

### Conceptos Clave

- **Feature Engineering:** Crear variables más predictivas
- **Feature Selection:** Elegir las variables más importantes
- **Pipeline:** Encadenar transformaciones de manera reproducible
- **Cross-validation:** Validar mejoras de manera robusta

## Entrega

- **Formato:** Jupyter Notebook (.ipynb) + Archivo de pipeline (.pkl)
- **Nombre:** `apellido_nombre_semana14_feature_engineering.ipynb`
- **Fecha límite:** [Definir según cronograma]
- **Plataforma:** [Especificar LMS o sistema de entrega]

---

*¡Increíble progreso! Ya dominas técnicas avanzadas de feature engineering. En la próxima semana integrarás todo lo aprendido en un proyecto final completo.*

**Tiempo total estimado:** 4-5 horas  
**Dificultad:** ⭐⭐⭐⭐⭐ (Muy Alto)  
**Prerrequisitos:** Completar Ejercicios Semanas 11-13
