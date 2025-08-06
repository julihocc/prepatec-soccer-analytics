# Ejercicio Semana 12: Modelos Avanzados de Clasificación

## Información General

**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 12  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 12  
**Archivo entrega:** `[matricula]-ejercicio-semana-12.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Implementar múltiples algoritmos de machine learning
- Comparar diferentes tipos de modelos predictivos
- Optimizar parámetros básicos de modelos
- Seleccionar el mejor modelo para cada situación
- Aplicar ensemble methods básicos

## Prerrequisitos

- Ejercicio de la Semana 11 completado exitosamente
- Conocimiento básico de modelos de clasificación
- Familiaridad con métricas de evaluación
- Comprensión de conceptos de overfitting y underfitting

## Contexto del Ejercicio

Eres el **ingeniero de machine learning** del FC Barcelona. Después del éxito inicial con modelos básicos, necesitas desarrollar un arsenal completo de algoritmos para:

- Probar múltiples enfoques predictivos
- Encontrar el modelo más efectivo para cada situación
- Optimizar rendimiento mediante ensemble methods
- Crear sistema robusto de predicción deportiva

---

## Ejercicio 1: Arsenal de Modelos - Probando Diferentes Algoritmos (1.5 horas)

# Ejercicio Integrador: Arsenal de Algoritmos FC Barcelona

## Parte 1: Implementación de Múltiples Modelos (25 puntos)

### Objetivo
Crear y entrenar múltiples algoritmos de machine learning para encontrar el más efectivo para el FC Barcelona.

### Instrucciones Detalladas

**Paso 1:** Configura el laboratorio de modelos avanzados:

```python
# Configuración del laboratorio ML avanzado FC Barcelona
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuración visual FC Barcelona
colores_barca = ['#004D98', '#FCBF49', '#DC143C', '#212121']
sns.set_theme(style="whitegrid", palette=colores_barca)
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11

print("=== LABORATORIO AVANZADO FC BARCELONA ===")
print("Arsenal de algoritmos de machine learning iniciado")
print("¡Múltiples modelos listos para competir!")
```

**Paso 2:** Prepara dataset avanzado del Barcelona:

```python
# Dataset mejorado para FC Barcelona

# TU CÓDIGO AQUÍ:
# 1. Crear dataset de 400 partidos históricos del Barcelona
# 2. Incluir variables más sofisticadas:
#    - forma_reciente: Puntos promedio últimos 5 partidos
#    - efectividad_local: % victorias en casa histórico
#    - fuerza_rival: Rating del equipo rival (1-10)
#    - presion_alta: % recuperaciones en campo rival
#    - precision_pases: % pases completados
#    - minutos_posesion: Minutos con balón por partido
# 3. Variable objetivo: 'goleada' (1 si ganó por 2+ goles, 0 si no)
# 4. Balancear dataset para tener distribución realista

np.random.seed(123)  # Para reproducibilidad

# Generar datos del Barcelona
partidos_barca = []
for i in range(400):
    # Variables base
    forma_reciente = np.random.normal(2.2, 0.5)
    efectividad_local = np.random.normal(75, 10)
    fuerza_rival = np.random.randint(1, 11)
    presion_alta = np.random.normal(35, 8)
    precision_pases = np.random.normal(88, 5)
    minutos_posesion = np.random.normal(38, 6)
    
    # Probabilidad de goleada basada en variables
    prob_goleada = (
        forma_reciente * 0.2 + 
        efectividad_local * 0.01 + 
        (11 - fuerza_rival) * 0.05 + 
        presion_alta * 0.01 + 
        precision_pases * 0.005 + 
        minutos_posesion * 0.01
    ) / 10
    
    partido = {
        'forma_reciente': forma_reciente,
        'efectividad_local': efectividad_local,
        'fuerza_rival': fuerza_rival,
        'presion_alta': presion_alta,
        'precision_pases': precision_pases,
        'minutos_posesion': minutos_posesion,
        'goleada': 1 if np.random.random() < prob_goleada else 0
    }
    partidos_barca.append(partido)

df_barca = pd.DataFrame(partidos_barca)

print("=== DATASET BARCELONA GENERADO ===")
print(f"Total partidos: {len(df_barca)}")
print(f"Distribución goleadas: {df_barca['goleada'].value_counts()}")
print(f"Porcentaje goleadas: {df_barca['goleada'].mean():.1%}")
```

### Criterios de Evaluación
- **Configuración correcta del entorno avanzado** (10 puntos)
- **Dataset realista con variables sofisticadas** (15 puntos)

---

## Parte 2: Comparación Sistemática de Algoritmos (25 puntos)

### Objetivo
Entrenar y comparar múltiples algoritmos para identificar el más efectivo para el Barcelona.

### Instrucciones Detalladas

**Paso 3:** Implementa arsenal completo de modelos:

```python
# Arsenal de modelos de machine learning

# TU CÓDIGO AQUÍ:
# 1. Preparar datos (X, y) y división train/test
# 2. Implementar 6 modelos diferentes:
#    - Regresión Logística
#    - Árbol de Decisión
#    - Random Forest
#    - Gradient Boosting
#    - Support Vector Machine
#    - K-Nearest Neighbors
# 3. Entrenar todos con los mismos datos
# 4. Realizar predicciones en conjunto de prueba
# 5. Calcular accuracy para cada modelo

# Preparar datos
features = ['forma_reciente', 'efectividad_local', 'fuerza_rival', 'presion_alta', 'precision_pases', 'minutos_posesion']
X = df_barca[features]
y = df_barca['goleada']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Diccionario de modelos
modelos = {
    'Regresión Logística': LogisticRegression(random_state=42),
    'Árbol de Decisión': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'SVM': SVC(random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)
}

# Entrenar y evaluar modelos
resultados = {}
for nombre, modelo in modelos.items():
    # Entrenar modelo
    modelo.fit(X_train, y_train)
    
    # Predicciones
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    resultados[nombre] = {
        'modelo': modelo,
        'accuracy': accuracy,
        'predicciones': y_pred
    }
    
    print(f"{nombre}: {accuracy:.3f}")

print("=== ARSENAL DE MODELOS ENTRENADO ===")
```

**Paso 4:** Analiza rendimiento detallado:

```python
# Análisis detallado de rendimiento por modelo

# TU CÓDIGO AQUÍ:
# 1. Crear visualización comparativa de accuracy
# 2. Generar matrices de confusión para top 3 modelos
# 3. Analizar fortalezas/debilidades de cada algoritmo
# 4. Identificar qué modelos son mejores para diferentes escenarios
# 5. Calcular métricas adicionales (precision, recall)

# Visualización comparativa
plt.figure(figsize=(12, 6))
nombres = list(resultados.keys())
accuracies = [resultados[nombre]['accuracy'] for nombre in nombres]

bars = plt.bar(nombres, accuracies, color=colores_barca[:len(nombres)])
plt.title('Comparación de Modelos: FC Barcelona', fontsize=16, fontweight='bold')
plt.ylabel('Precisión (Accuracy)')
plt.xticks(rotation=45)
plt.ylim(0, 1)

# Añadir valores en barras
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{acc:.3f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Top 3 modelos
top_3 = sorted(resultados.items(), key=lambda x: x[1]['accuracy'], reverse=True)[:3]

print("=== TOP 3 MODELOS BARCELONA ===")
for i, (nombre, datos) in enumerate(top_3, 1):
    print(f"{i}. {nombre}: {datos['accuracy']:.3f}")
```

### Criterios de Evaluación
- **Implementación correcta de múltiples modelos** (15 puntos)
- **Análisis comparativo detallado** (10 puntos)
---

## Parte 3: Optimización y Ensemble Methods (25 puntos)

### Objetivo
Optimizar el mejor modelo y crear combinaciones de modelos para máximo rendimiento.

### Instrucciones Detalladas

**Paso 5:** Optimiza el mejor modelo individual:

```python
# Optimización del modelo más prometedor

# TU CÓDIGO AQUÍ:
# 1. Seleccionar el modelo con mejor rendimiento
# 2. Implementar optimización de hiperparámetros
# 3. Probar diferentes configuraciones
# 4. Validar mejora con validación cruzada
# 5. Comparar modelo original vs optimizado

# Ejemplo para Random Forest (ajustar según tu mejor modelo)
from sklearn.model_selection import GridSearchCV

mejor_modelo_nombre = max(resultados.items(), key=lambda x: x[1]['accuracy'])[0]
print(f"Optimizando: {mejor_modelo_nombre}")

if 'Random Forest' in mejor_modelo_nombre:
    # Optimización Random Forest
    parametros_rf = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    
    rf_optimizado = GridSearchCV(
        RandomForestClassifier(random_state=42),
        parametros_rf,
        cv=5,
        scoring='accuracy'
    )
    
    rf_optimizado.fit(X_train, y_train)
    
    print(f"Mejores parámetros: {rf_optimizado.best_params_}")
    print(f"Mejor score CV: {rf_optimizado.best_score_:.3f}")
    
    # Evaluar en test
    y_pred_optimizado = rf_optimizado.predict(X_test)
    accuracy_optimizado = accuracy_score(y_test, y_pred_optimizado)
    print(f"Accuracy optimizado: {accuracy_optimizado:.3f}")

print("=== OPTIMIZACIÓN COMPLETADA ===")
```

**Paso 6:** Crea ensemble de modelos:

```python
# Ensemble Methods para máximo rendimiento

# TU CÓDIGO AQUÍ:
# 1. Seleccionar top 3 modelos diferentes
# 2. Crear ensemble por votación (Voting Classifier)
# 3. Implementar ensemble ponderado por rendimiento
# 4. Comparar ensemble vs mejores modelos individuales
# 5. Evaluar estabilidad del ensemble con validación cruzada

from sklearn.ensemble import VotingClassifier

# Seleccionar top 3 modelos diversos
top_3_nombres = [nombre for nombre, _ in top_3]
top_3_modelos = [(nombre, resultados[nombre]['modelo']) for nombre in top_3_nombres]

# Ensemble por votación
ensemble_voting = VotingClassifier(
    estimators=top_3_modelos,
    voting='hard'
)

ensemble_voting.fit(X_train, y_train)
y_pred_ensemble = ensemble_voting.predict(X_test)
accuracy_ensemble = accuracy_score(y_test, y_pred_ensemble)

print("=== ENSEMBLE BARCELONA ===")
print(f"Modelos en ensemble: {top_3_nombres}")
print(f"Accuracy ensemble: {accuracy_ensemble:.3f}")

# Comparación final
print("\n=== COMPARACIÓN FINAL ===")
for nombre in top_3_nombres:
    print(f"{nombre}: {resultados[nombre]['accuracy']:.3f}")
print(f"Ensemble: {accuracy_ensemble:.3f}")

# Validación cruzada del ensemble
cv_scores = cross_val_score(ensemble_voting, X, y, cv=5)
print(f"CV Score ensemble: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
```

### Criterios de Evaluación
- **Optimización exitosa de hiperparámetros** (15 puntos)
- **Implementación correcta de ensemble methods** (10 puntos)

---

## Parte 4: Análisis de Variables y Reporte Final (25 puntos)

### Objetivo
Analizar importancia de variables y generar reporte ejecutivo para el FC Barcelona.

### Instrucciones Detalladas

**Paso 7:** Analiza importancia de variables:

```python
# Análisis de importancia de variables

# TU CÓDIGO AQUÍ:
# 1. Extraer importancia de variables de Random Forest
# 2. Analizar coeficientes de Regresión Logística
# 3. Crear visualizaciones de importancia
# 4. Interpretar qué factores son más predictivos para goleadas
# 5. Generar insights tácticos para el Barcelona

# Importancia en Random Forest
if 'Random Forest' in resultados:
    rf_model = resultados['Random Forest']['modelo']
    importancias = rf_model.feature_importances_
    
    # Visualización de importancia
    plt.figure(figsize=(10, 6))
    indices = np.argsort(importancias)[::-1]
    
    plt.bar(range(len(features)), importancias[indices], color='#004D98')
    plt.title('Importancia de Variables: Random Forest - FC Barcelona', fontsize=14, fontweight='bold')
    plt.xlabel('Variables')
    plt.ylabel('Importancia')
    plt.xticks(range(len(features)), [features[i] for i in indices], rotation=45)
    plt.tight_layout()
    plt.show()
    
    print("=== IMPORTANCIA DE VARIABLES ===")
    for i in indices:
        print(f"{features[i]}: {importancias[i]:.3f}")

# Análisis de coeficientes Regresión Logística
if 'Regresión Logística' in resultados:
    lr_model = resultados['Regresión Logística']['modelo']
    coeficientes = lr_model.coef_[0]
    
    print("\n=== COEFICIENTES REGRESIÓN LOGÍSTICA ===")
    for feature, coef in zip(features, coeficientes):
        direccion = "positivo" if coef > 0 else "negativo"
        print(f"{feature}: {coef:.3f} (impacto {direccion})")
```

**Paso 8:** Genera reporte ejecutivo final:

```python
# Reporte ejecutivo para la dirección del FC Barcelona

# TU CÓDIGO AQUÍ:
# 1. Resumir hallazgos del análisis de modelos
# 2. Recomendar estrategia de implementación
# 3. Identificar factores clave para goleadas
# 4. Proponer mejoras tácticas basadas en insights
# 5. Establecer plan de monitoreo del sistema

print("=" * 70)
print("FC BARCELONA - REPORTE SISTEMA PREDICTIVO AVANZADO")
print("Análisis Comparativo de Algoritmos de Machine Learning")
print("=" * 70)

print("\n🏆 MODELO RECOMENDADO:")
if accuracy_ensemble > max(accuracies):
    print(f"• Ensemble de modelos (Precisión: {accuracy_ensemble:.1%})")
    print(f"• Componentes: {', '.join(top_3_nombres)}")
else:
    mejor_individual = max(resultados.items(), key=lambda x: x[1]['accuracy'])
    print(f"• {mejor_individual[0]} (Precisión: {mejor_individual[1]['accuracy']:.1%})")

print("\n📊 FACTORES CLAVE PARA GOLEADAS:")
if 'Random Forest' in resultados:
    top_features = sorted(zip(features, importancias), key=lambda x: x[1], reverse=True)[:3]
    for i, (feature, importance) in enumerate(top_features, 1):
        print(f"{i}. {feature}: {importance:.1%}")

print("\n⚽ INSIGHTS TÁCTICOS:")
print("1. Mantener alta precisión en pases es crucial para goleadas")
print("2. La forma reciente del equipo predice fuertemente el resultado")
print("3. Presión alta en campo rival aumenta probabilidad de goleada")

print("\n🔧 RECOMENDACIONES DE IMPLEMENTACIÓN:")
print("1. Usar ensemble de modelos para decisiones críticas")
print("2. Monitorear variables clave antes de cada partido")
print("3. Ajustar táctica según predicciones del modelo")
print("4. Reentrenar modelos cada 10 partidos")

print("\n📈 PRÓXIMOS DESARROLLOS:")
print("1. Incorporar datos de jugadores individuales")
print("2. Añadir variables contextuales (clima, arbitraje)")
print("3. Desarrollar predicciones específicas por rival")

# Visualización resumen
plt.figure(figsize=(12, 8))

# Subplot 1: Comparación de modelos
plt.subplot(2, 2, 1)
plt.bar(nombres, accuracies, color='lightblue')
plt.title('Rendimiento por Modelo')
plt.xticks(rotation=45)
plt.ylabel('Accuracy')

# Subplot 2: Importancia de variables
plt.subplot(2, 2, 2)
if 'Random Forest' in resultados:
    plt.bar(range(len(features)), importancias, color='orange')
    plt.title('Importancia Variables')
    plt.xticks(range(len(features)), features, rotation=45)

# Subplot 3: Matriz confusión mejor modelo
plt.subplot(2, 2, 3)
mejor_pred = resultados[mejor_modelo_nombre]['predicciones']
cm = confusion_matrix(y_test, mejor_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz Confusión')

# Subplot 4: Distribución predicciones
plt.subplot(2, 2, 4)
plt.hist(y_test, alpha=0.5, label='Real', bins=2)
plt.hist(mejor_pred, alpha=0.5, label='Predicción', bins=2)
plt.title('Distribución Predicciones')
plt.legend()

plt.suptitle('Dashboard Analítico FC Barcelona', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Criterios de Evaluación
- **Análisis detallado de importancia de variables** (15 puntos)
- **Reporte ejecutivo completo y profesional** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Implementación correcta de múltiples algoritmos ML
- Optimización apropiada de hiperparámetros
- Ensemble methods implementados correctamente
- Análisis de variables estadísticamente válido

### Aplicación Práctica (30 puntos)
- Insights relevantes para estrategia del Barcelona
- Interpretación correcta de diferencias entre modelos
- Recomendaciones tácticas basadas en evidencia
- Evaluación práctica de utilidad del sistema

### Claridad y Documentación (30 puntos)
- Comparaciones claras entre algoritmos
- Explicaciones comprensibles de conceptos ML
- Presentación profesional de resultados
- Código bien estructurado y comentado

## Instrucciones de Entrega

1. **Implementa todos los modelos** correctamente
2. **Incluye análisis comparativo** detallado entre algoritmos
3. **Verifica funcionamiento** de ensemble methods
4. **Guarda como:** `[matricula]-ejercicio-semana-12.ipynb`
5. **Entrega antes del final de Semana 12**

## Recursos de Apoyo

- Notebook de la Semana 12: `modelos-avanzados-clasificacion.ipynb`
- Documentación scikit-learn: Algoritmos de clasificación
- Guía de ensemble methods y optimización

---

**¡Desarrolla el arsenal completo de algoritmos y convierte al Barcelona en líder tecnológico del fútbol!** ⚽🧠

### Contexto
A veces, combinar las predicciones de varios modelos puede dar mejores resultados que usar solo uno. Es como tener un comité de expertos tomando decisiones.

### Tareas

**4.1 Voting Classifier simple**

```python
from sklearn.ensemble import VotingClassifier

# Combina tus 3 mejores modelos
ensemble_votacion = VotingClassifier(
    estimators=[
        ('modelo1_nombre', modelo1),
        ('modelo2_nombre', modelo2), 
        ('modelo3_nombre', modelo3)
    ],
    voting='soft'  # o 'hard'
)
```

**4.2 Promedio de predicciones**

- Implementa manualmente un promedio de las probabilidades de predicción
- Compara con VotingClassifier
- ¿Da resultados similares?

**4.3 Evaluación del ensemble**

- Compara el rendimiento del ensemble vs modelos individuales
- ¿El ensemble supera a todos los modelos individuales?
- ¿En qué casos el ensemble es más confiable?

**4.4 Análisis de consenso**

- Identifica casos donde todos los modelos coinciden
- Identifica casos donde hay discrepancia
- ¿En qué tipo de partidos hay más acuerdo entre modelos?

### Entregables

- Ensemble method implementado
- Comparación ensemble vs modelos individuales
- Análisis de consenso entre modelos
- Recomendaciones sobre cuándo usar ensemble

---

## Ejercicio Bonus: Predicción de Resultados Múltiples (30 minutos)

### Contexto
Hasta ahora hemos predicho solo victoria/derrota local. ¿Podemos predecir resultado exacto o al menos victoria/empate/derrota?

### Tareas

**Bonus.1 Predicción de tres clases**

- Modifica el problema para predecir: Victoria Local / Empate / Victoria Visitante
- Adapta tus mejores modelos para esta nueva tarea
- ¿Cómo cambia la precisión?

**Bonus.2 Predicción de margen de goles**

- Intenta predecir si la diferencia será: 1 gol, 2+ goles, o empate
- ¿Qué variables son más importantes para esta predicción?

**Bonus.3 Reflexión sobre complejidad**

- ¿Es más fácil predecir victoria/derrota o resultado exacto?
- ¿Qué aplicación práctica tendría cada tipo de predicción?

### Entregables

- Modelos para problemas de clasificación múltiple
- Comparación de dificultad entre diferentes tipos de predicción
- Reflexión sobre aplicaciones prácticas

---

## Criterios de Evaluación

### Competencia Técnica (45%)

- **Implementación correcta:** Todos los modelos funcionan sin errores
- **Optimización:** Uso adecuado de hiperparámetros y validación cruzada
- **Ensemble methods:** Implementación correcta de técnicas de combinación

### Análisis Comparativo (35%)

- **Análisis profundo:** Comparación detallada entre modelos
- **Interpretación:** Comprensión de fortalezas y debilidades de cada algoritmo
- **Pensamiento crítico:** Identificación de patrones y insights

### Aplicación Práctica (20%)

- **Relevancia deportiva:** Análisis apropiado en contexto futbolístico
- **Metodología:** Proceso sistemático de evaluación y selección
- **Comunicación:** Presentación clara de resultados y recomendaciones

## Recursos de Apoyo

### Documentación Técnica

- [Scikit-learn Model Selection](https://scikit-learn.org/stable/model_selection.html)
- [Ensemble Methods Guide](https://scikit-learn.org/stable/modules/ensemble.html)
- [Hyperparameter Tuning](https://scikit-learn.org/stable/modules/grid_search.html)

### Conceptos Clave

- **Hyperparameters:** Configuraciones que afectan el aprendizaje del modelo
- **Cross-validation:** Técnica para validar modelos de manera robusta
- **Ensemble Learning:** Combinar múltiples modelos para mejor rendimiento
- **Bias-Variance Tradeoff:** Balance entre simplicidad y complejidad del modelo

## Entrega

- **Formato:** Jupyter Notebook (.ipynb)
- **Nombre:** `apellido_nombre_semana12_modelos_avanzados.ipynb`
- **Fecha límite:** [Definir según cronograma]
- **Plataforma:** [Especificar LMS o sistema de entrega]

---

*¡Excelente progreso! Ya dominas múltiples algoritmos de machine learning. En la próxima semana aprenderemos a evaluar más profundamente qué tan buenos son nuestros modelos.*

**Tiempo total estimado:** 3-4 horas  
**Dificultad:** ⭐⭐⭐⭐ (Alto)  
**Prerrequisitos:** Completar Ejercicio Semana 11
