# Introducción al Modelado Predictivo en Fútbol

## Objetivos de Aprendizaje

Al finalizar esta sesión, los estudiantes podrán:
- Comprender los fundamentos del modelado predictivo en deportes
- Identificar problemas de clasificación y regresión en fútbol
- Reconocer la importancia de la preparación de datos
- Aplicar técnicas básicas de feature engineering
- Evaluar la calidad de variables predictoras

## 1. Fundamentos del Modelado Predictivo

### ¿Qué es el Modelado Predictivo?

El modelado predictivo es el proceso de crear modelos matemáticos que pueden predecir resultados futuros basándose en datos históricos. En el contexto del fútbol, nos permite:

- **Predecir resultados** de partidos futuros
- **Estimar probabilidades** de eventos específicos
- **Clasificar estilos** de juego y tácticas
- **Evaluar rendimiento** de jugadores y equipos

### Tipos de Problemas Predictivos

#### Clasificación
- **Resultado del partido:** Victoria, empate, derrota
- **Clasificación de jugadores:** Ofensivo, defensivo, mixto
- **Tipo de jugada:** Ataque directo, posesión, contraataque

#### Regresión
- **Número de goles:** Predicción continua de goles por partido
- **Valor de mercado:** Estimación del precio de transferencia
- **Minutos jugados:** Predicción de tiempo de juego

#### Ranking
- **Clasificación de equipos:** Ordenar por probabilidad de victoria
- **Ranking de jugadores:** Ordenar por rendimiento esperado

## 2. El Proceso de Modelado Predictivo

### Fase 1: Definición del Problema
1. **Objetivo claro:** ¿Qué queremos predecir?
2. **Métricas de éxito:** ¿Cómo mediremos el rendimiento?
3. **Contexto de uso:** ¿Cómo se usará el modelo?

### Fase 2: Recolección y Preparación de Datos
1. **Fuentes de datos:** Resultados, estadísticas, contexto
2. **Calidad de datos:** Completitud, consistencia, relevancia
3. **Transformaciones:** Limpieza, normalización, codificación

### Fase 3: Feature Engineering
1. **Variables básicas:** Goles, tarjetas, posesión
2. **Variables derivadas:** Rachas, forma, ventaja local
3. **Variables contextuales:** Clima, importancia del partido

### Fase 4: Selección de Algoritmo
1. **Algoritmos simples:** Regresión logística, árboles de decisión
2. **Algoritmos avanzados:** Random Forest, SVM, redes neuronales
3. **Ensemble methods:** Combinación de múltiples modelos

### Fase 5: Entrenamiento y Evaluación
1. **División de datos:** Entrenamiento, validación, prueba
2. **Métricas de evaluación:** Accuracy, precision, recall, F1
3. **Validación cruzada:** Robustez del modelo

### Fase 6: Optimización y Tuning
1. **Hiperparámetros:** Ajuste fino del modelo
2. **Feature selection:** Selección de variables más relevantes
3. **Regularización:** Prevención de overfitting

## 3. Características Específicas del Fútbol

### Desafíos Únicos

#### Baja Frecuencia de Eventos
- Los goles son eventos raros
- Muchos partidos terminan 0-0 o 1-1
- Necesidad de considerar contexto temporal

#### Dependencia del Contexto
- **Importancia del partido:** Liga vs. Copa vs. Amistoso
- **Momento de la temporada:** Inicio, mitad, final
- **Condiciones externas:** Clima, lesiones, presión

#### Naturaleza Temporal
- **Rachas:** Secuencias de victorias/derrotas
- **Forma actual:** Rendimiento reciente vs. histórico
- **Fatiga:** Calendario de partidos

### Oportunidades Específicas

#### Datos Ricos
- **Estadísticas detalladas:** Pases, tiros, posesión
- **Datos de posición:** Tracking de jugadores
- **Métricas avanzadas:** xG, xA, PPDA

#### Patrones Reconocibles
- **Ventaja local:** Tendencia histórica consistente
- **Estilos de juego:** Patrones tácticos identificables
- **Rendimiento por rival:** Historiales específicos

## 4. Variables Predictoras en Fútbol

### Variables Básicas
- **Resultados históricos:** Victorias, empates, derrotas
- **Estadísticas de goles:** Goles a favor y en contra
- **Posición en tabla:** Ranking actual en liga

### Variables Derivadas
- **Forma reciente:** Rendimiento en últimos 5 partidos
- **Racha actual:** Partidos consecutivos sin perder
- **Eficiencia:** Puntos por partido, goles por tiro

### Variables Contextuales
- **Localía:** Jugar en casa vs. fuera
- **Rivalidad:** Partidos contra equipos específicos
- **Importancia:** Playoff, descenso, título

### Variables Avanzadas
- **Expected Goals (xG):** Calidad de oportunidades
- **Pressing intensity:** Intensidad defensiva
- **Pass completion rate:** Eficiencia en pases

## 5. Preparación de Datos para Modelado

### Limpieza de Datos

```python
# Ejemplo de limpieza básica
import pandas as pd
import numpy as np

# Identificar valores faltantes
missing_data = df.isnull().sum()

# Tratar valores atípicos
Q1 = df['goals'].quantile(0.25)
Q3 = df['goals'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['goals'] < Q1 - 1.5*IQR) | (df['goals'] > Q3 + 1.5*IQR)]

# Normalización de datos
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[numeric_columns])
```

### Codificación de Variables Categóricas

```python
# Codificación de equipos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label encoding para variables ordinales
le = LabelEncoder()
df['team_encoded'] = le.fit_transform(df['team'])

# One-hot encoding para variables nominales
ohe = OneHotEncoder(sparse=False)
team_encoded = ohe.fit_transform(df[['team']])
```

### Creación de Variables Temporales

```python
# Variables de tiempo
df['match_date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['match_date'].dt.dayofweek
df['month'] = df['match_date'].dt.month
df['is_weekend'] = df['day_of_week'].isin([5, 6])

# Variables de racha
df['points_last_5'] = df.groupby('team')['points'].rolling(5).sum()
df['goals_last_3'] = df.groupby('team')['goals'].rolling(3).mean()
```

## 6. Selección de Variables

### Métodos Estadísticos

#### Correlación
```python
# Matriz de correlación
correlation_matrix = df.corr()
high_corr_features = correlation_matrix[abs(correlation_matrix) > 0.7]
```

#### Información Mutua
```python
from sklearn.feature_selection import mutual_info_classif

# Información mutua con variable objetivo
mi_scores = mutual_info_classif(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': mi_scores
}).sort_values('importance', ascending=False)
```

### Métodos de Machine Learning

#### Importance de Random Forest
```python
from sklearn.ensemble import RandomForestClassifier

# Entrenar modelo para obtener importancia
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Importancia de características
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
```

#### Recursive Feature Elimination (RFE)
```python
from sklearn.feature_selection import RFE

# Selección recursiva de características
rfe = RFE(estimator=rf, n_features_to_select=10)
rfe.fit(X_train, y_train)
selected_features = X.columns[rfe.support_]
```

## 7. Consideraciones Éticas y Limitaciones

### Sesgos en los Datos
- **Sesgo de selección:** Equipos o ligas sub-representadas
- **Sesgo temporal:** Cambios en reglas o estilos de juego
- **Sesgo de confirmación:** Buscar patrones que confirmen creencias

### Limitaciones del Modelado
- **Eventos impredecibles:** Lesiones, tarjetas rojas, errores arbitrales
- **Factores externos:** Motivación, presión, factores psicológicos
- **Cambios tácticos:** Adaptaciones durante el partido

### Uso Responsable
- **Transparencia:** Explicar cómo funciona el modelo
- **Actualización:** Mantener modelos actualizados
- **Contexto:** No usar modelos fuera de su dominio

## 8. Casos de Estudio

### Caso 1: Predicción de Resultados
- **Problema:** Predecir resultado de La Liga
- **Variables:** Forma, localía, historial
- **Modelo:** Regresión logística multinomial
- **Resultado:** 55% de accuracy

### Caso 2: Expected Goals
- **Problema:** Estimar calidad de oportunidades
- **Variables:** Posición, tipo de jugada, presión
- **Modelo:** Regresión logística
- **Resultado:** Correlación 0.8 con goles reales

### Caso 3: Clasificación de Estilos
- **Problema:** Identificar estilo de juego
- **Variables:** Pases, pressing, posesión
- **Modelo:** K-means clustering
- **Resultado:** 4 estilos diferenciados

## 9. Herramientas y Recursos

### Librerías de Python
- **scikit-learn:** Machine learning general
- **pandas:** Manipulación de datos
- **numpy:** Computación numérica
- **matplotlib/seaborn:** Visualización

### Datasets Recomendados
- **FBref:** Estadísticas detalladas de ligas
- **Understat:** Datos de expected goals
- **StatsBomb:** Datos de eventos detallados

### Herramientas Avanzadas
- **Jupyter:** Notebooks interactivos
- **MLflow:** Tracking de experimentos
- **Optuna:** Optimización de hiperparámetros

## 10. Actividades Prácticas

### Ejercicio 1: Análisis Exploratorio
1. Cargar dataset de partidos
2. Identificar variables predictoras potenciales
3. Analizar distribuciones y correlaciones
4. Detectar valores atípicos

### Ejercicio 2: Feature Engineering
1. Crear variables de racha
2. Calcular métricas de eficiencia
3. Generar variables de contexto
4. Evaluar importancia de variables

### Ejercicio 3: Preparación de Datos
1. Limpiar datos faltantes
2. Codificar variables categóricas
3. Normalizar variables numéricas
4. Dividir en conjuntos de entrenamiento y prueba

## Próxima Sesión

En la siguiente sesión exploraremos scikit-learn en profundidad y implementaremos nuestros primeros modelos de clasificación para predicción de resultados futbolísticos.

## Recursos Adicionales

- **Documentación scikit-learn:** https://scikit-learn.org/
- **Curso de Machine Learning:** Andrew Ng (Coursera)
- **Libro:** "Introduction to Statistical Learning" (James et al.)
- **Blog:** Towards Data Science (Medium)
