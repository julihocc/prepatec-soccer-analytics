# Ejercicio Semanal - Semana 12: Modelos Más Inteligentes

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 12 - Modelos Avanzados de Clasificación  
**Tiempo estimado:** 3-4 horas  
**Tipo:** Individual  

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Implementar** múltiples algoritmos de machine learning
2. **Comparar** diferentes tipos de modelos predictivos
3. **Optimizar** parámetros básicos de modelos
4. **Seleccionar** el mejor modelo para cada situación
5. **Aplicar** ensemble methods básicos

## Contexto del Problema

En la vida real, los científicos de datos prueban múltiples algoritmos antes de elegir el mejor. Es como tener diferentes "cerebros" que piensan de manera distinta, y queremos encontrar cuál es mejor para nuestro problema específico.

**Pregunta central:** *¿Qué algoritmo predice mejor los resultados de fútbol: uno simple pero confiable, o uno complejo pero potente?*

---

## Ejercicio 1: Arsenal de Modelos - Probando Diferentes Algoritmos (1.5 horas)

### Contexto
Vamos a implementar varios algoritmos de machine learning y compararlos sistemáticamente. Cada algoritmo "piensa" diferente y puede capturar patrones distintos en los datos.

### Tareas

**1.1 Configuración del entorno**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="viridis")
```

**1.2 Preparación de datos mejorados**

- Crea un dataset más robusto con 1000+ partidos
- Incluye variables adicionales: `rival_fuerza`, `dias_descanso`, `lesionados`, `clima`, `importancia_partido`
- Asegúrate de tener datos balanceados (aproximadamente 50% victorias locales)

**1.3 Implementación de múltiples modelos**

- **Regresión Logística:** Simple y interpretable
- **Árbol de Decisión:** Fácil de visualizar y entender
- **Random Forest:** Combinación de muchos árboles
- **Gradient Boosting:** Algoritmo que corrige errores iterativamente
- **K-Nearest Neighbors:** Predicción basada en casos similares
- **Naive Bayes:** Algoritmo probabilístico
- **Support Vector Machine:** Algoritmo que encuentra fronteras óptimas

**1.4 Entrenamiento y evaluación inicial**

- Entrena todos los modelos con los mismos datos
- Calcula la precisión de cada uno
- Crea una tabla comparativa ordenada por rendimiento

### Entregables

- Código funcional con 7 modelos implementados
- Dataset mejorado con variables adicionales
- Tabla comparativa de rendimientos iniciales
- Explicación de qué hace cada algoritmo

---

## Ejercicio 2: Análisis Profundo de Modelos (1 hora)

### Contexto
Más allá de la simple precisión, necesitamos entender cómo se comporta cada modelo y en qué situaciones funciona mejor.

### Tareas

**2.1 Matrices de confusión comparativas**

- Crea matrices de confusión para los 3 mejores modelos
- Analiza qué tipo de errores comete cada uno
- ¿Algunos modelos son mejores prediciendo victorias? ¿Otros mejores prediciendo derrotas?

**2.2 Análisis de características importantes**

- Para modelos que lo permitan (Random Forest, Gradient Boosting), extrae la importancia de variables
- Compara qué variables considera más importantes cada modelo
- ¿Coinciden en las variables más predictivas?

**2.3 Predicciones en casos extremos**

Crea escenarios específicos y compara predicciones:

- **Escenario 1:** Equipo muy fuerte vs muy débil en casa
- **Escenario 2:** Equipos similares, uno descansado vs uno cansado
- **Escenario 3:** Partido de alta importancia vs partido sin consecuencias

**2.4 Tiempo de entrenamiento y predicción**

- Mide cuánto tarda cada modelo en entrenar
- Mide cuánto tarda en hacer predicciones
- ¿Hay trade-offs entre velocidad y precisión?

### Entregables

- Matrices de confusión comparativas
- Análisis de importancia de variables
- Predicciones en escenarios específicos
- Análisis de eficiencia computacional

---

## Ejercicio 3: Optimización de Hiperparámetros (1 hora)

### Contexto
Cada algoritmo tiene "perillas" que podemos ajustar para mejorar su rendimiento. Es como afinar un instrumento musical para que suene mejor.

### Tareas

**3.1 Optimización de Random Forest**

```python
from sklearn.model_selection import GridSearchCV

# Parámetros a probar
parametros_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

# Tu código de optimización aquí
```

**3.2 Optimización de otros modelos**

- **Gradient Boosting:** Prueba diferentes learning_rate y n_estimators
- **KNN:** Prueba diferentes valores de k (neighbors)
- **SVM:** Prueba diferentes kernels y parámetros C

**3.3 Validación cruzada**

- Usa validación cruzada de 5 folds para todos los modelos optimizados
- Compara resultados antes y después de la optimización
- ¿Qué modelo mejoró más con la optimización?

**3.4 Modelo final optimizado**

- Selecciona el mejor modelo después de la optimización
- Entrénalo con todos los datos de entrenamiento disponibles
- Evalúa en el conjunto de prueba

### Entregables

- Modelos optimizados con mejores parámetros
- Comparación antes/después de optimización
- Validación cruzada implementada
- Selección y evaluación de modelo final

---

## Ejercicio 4: Ensemble Methods - Combinando Modelos (45 minutos)

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
