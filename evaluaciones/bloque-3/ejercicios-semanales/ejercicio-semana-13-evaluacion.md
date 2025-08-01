# Ejercicio Semanal - Semana 13: ¿Qué Tan Buena es Mi Predicción?

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 13 - Métricas Avanzadas de Evaluación  
**Tiempo estimado:** 3-4 horas  
**Tipo:** Individual  

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Calcular** e **interpretar** múltiples métricas de evaluación
2. **Analizar** matrices de confusión en profundidad
3. **Identificar** cuándo un modelo es realmente bueno vs cuando solo tiene suerte
4. **Aplicar** técnicas de validación robusta
5. **Comunicar** la calidad de modelos de manera profesional

## Contexto del Problema

La precisión (accuracy) no siempre cuenta toda la historia. Un modelo puede tener 80% de precisión pero ser terrible prediciendo victorias, o puede ser muy bueno con equipos fuertes pero malo con equipos débiles. Como científicos de datos profesionales, necesitamos herramientas más sofisticadas para evaluar nuestros modelos.

**Pregunta central:** *¿Cómo saber si mi modelo es realmente bueno o solo está adivinando con suerte?*

---

## Ejercicio 1: Más Allá de la Precisión - Métricas Fundamentales (1 hora)

### Contexto

La precisión simple puede ser engañosa. Si el 90% de los equipos locales ganan, un modelo que siempre prediga "victoria local" tendrá 90% de precisión, pero no será útil. Necesitamos métricas más informativas.

### Tareas

**1.1 Configuración y datos base**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score,
    roc_curve, precision_recall_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="viridis")
```

**1.2 Creación de conjunto de datos desbalanceado**

- Crea un dataset donde las victorias locales sean 70% de los casos (más realista)
- Incluye al menos 1000 partidos con variables relevantes
- Entrena tu mejor modelo de la semana anterior

**1.3 Cálculo de métricas básicas**

Calcula y explica cada métrica:

- **Accuracy:** ¿Qué porcentaje de predicciones fueron correctas?
- **Precision:** De todas las victorias locales que predije, ¿cuántas fueron correctas?
- **Recall (Sensitivity):** De todas las victorias locales reales, ¿cuántas detecté?
- **Specificity:** De todas las derrotas locales reales, ¿cuántas detecté?
- **F1-Score:** Promedio armónico de precision y recall

**1.4 Interpretación en contexto deportivo**

Para cada métrica, explica:

- ¿Qué significa en términos de predicciones deportivas?
- ¿Cuándo sería más importante cada una?
- ¿Qué métrica usarías para un sitio de apuestas vs un entrenador?

### Entregables

- Dataset desbalanceado creado
- Cálculo correcto de todas las métricas
- Interpretación detallada de cada métrica en contexto deportivo
- Recomendaciones sobre cuándo usar cada métrica

---

## Ejercicio 2: Matrices de Confusión - Análisis Profundo (1 hora)

### Contexto

La matriz de confusión es como un "informe detallado" de dónde se equivoca tu modelo. Nos permite identificar patrones específicos de errores y fortalezas.

### Tareas

**2.1 Matrices de confusión visuales**

```python
from sklearn.metrics import ConfusionMatrixDisplay

# Crea matrices de confusión visuales para tus mejores 3 modelos
# Compara lado a lado
```

**2.2 Análisis detallado de errores**

Para cada modelo:

- **Verdaderos Positivos:** Victorias locales predichas correctamente
- **Falsos Positivos:** Predije victoria local pero fue derrota (Error Tipo I)
- **Falsos Negativos:** Predije derrota local pero fue victoria (Error Tipo II)
- **Verdaderos Negativos:** Derrotas locales predichas correctamente

**2.3 Análisis de casos específicos**

- Identifica 10 casos de Falsos Positivos: ¿Qué tienen en común?
- Identifica 10 casos de Falsos Negativos: ¿Por qué el modelo falló?
- ¿Hay patrones identificables en los errores?

**2.4 Matriz de confusión normalizada**

- Crea matrices normalizadas por fila (recall) y por columna (precision)
- ¿Qué insights adicionales proporciona la normalización?
- ¿Tu modelo es mejor prediciendo victorias o derrotas?

**2.5 Costos de errores**

Considera diferentes escenarios:

- **Para apostadores:** ¿Qué error es más costoso?
- **Para entrenadores:** ¿Qué error es más problemático?
- **Para medios deportivos:** ¿Qué error es más embarazoso?

### Entregables

- Matrices de confusión visuales comparativas
- Análisis detallado de tipos de errores
- Identificación de patrones en errores específicos
- Análisis de costos relativos de diferentes tipos de errores

---

## Ejercicio 3: Curvas ROC y Análisis de Probabilidades (1 hora)

### Contexto

Las curvas ROC nos ayudan a entender el trade-off entre detectar victorias verdaderas y evitar falsas alarmas. También nos permiten ajustar el "umbral de decisión" de nuestro modelo.

### Tareas

**3.1 Curvas ROC comparativas**

```python
# Calcula y grafica curvas ROC para tus mejores modelos
from sklearn.metrics import roc_curve, auc

# Tu código aquí para crear curvas ROC comparativas
```

**3.2 Interpretación de AUC (Area Under Curve)**

- Calcula el AUC para cada modelo
- ¿Qué significa un AUC de 0.85 vs 0.92 en términos prácticos?
- ¿Cuál es el modelo más "discriminativo"?

**3.3 Ajuste de umbrales**

- Por defecto, el umbral es 0.5 (si probabilidad > 0.5, predice victoria)
- Experimenta con umbrales de 0.3, 0.5, 0.7
- ¿Cómo cambian precision, recall y F1 con cada umbral?

**3.4 Curva Precision-Recall**

- Crea curvas Precision-Recall para datos desbalanceados
- ¿Qué información adicional proporciona vs curva ROC?
- ¿Cuál es más informativa para tu problema específico?

**3.5 Selección de umbral óptimo**

- Encuentra el umbral que maximiza F1-score
- Encuentra el umbral que balancéa precision y recall
- ¿Qué umbral recomendarías para diferentes aplicaciones?

### Entregables

- Curvas ROC comparativas con AUC calculado
- Análisis de diferentes umbrales de decisión
- Curvas Precision-Recall para datos desbalanceados
- Recomendaciones de umbrales óptimos para diferentes escenarios

---

## Ejercicio 4: Validación Robusta y Confianza Estadística (1 hora)

### Contexto

¿Cómo sabemos si nuestro modelo realmente funciona o solo tuvimos suerte con la división de datos? Necesitamos técnicas de validación que nos den confianza estadística en nuestros resultados.

### Tareas

**4.1 Validación cruzada k-fold**

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Implementa validación cruzada de 10 folds
cv_scores = cross_val_score(modelo, X, y, cv=10, scoring='accuracy')
```

**4.2 Múltiples métricas con validación cruzada**

- Valida accuracy, precision, recall, f1 y AUC con 10-fold CV
- Calcula media y desviación estándar de cada métrica
- ¿Qué tan consistente es el rendimiento de tu modelo?

**4.3 Intervalos de confianza**

- Calcula intervalos de confianza del 95% para cada métrica
- ¿Cuál es el rango probable del verdadero rendimiento?
- ¿Los intervalos se superponen entre modelos?

**4.4 Pruebas de significancia**

- Compara estadísticamente tus dos mejores modelos
- ¿La diferencia en rendimiento es estadísticamente significativa?
- ¿O podrían ser iguales de buenos?

**4.5 Análisis de estabilidad**

- Repite la validación cruzada 10 veces con diferentes semillas aleatorias
- ¿Qué tan estables son los resultados?
- ¿Algún modelo es más consistente que otros?

### Entregables

- Validación cruzada implementada con múltiples métricas
- Intervalos de confianza calculados
- Análisis estadístico de diferencias entre modelos
- Evaluación de estabilidad y consistencia

---

## Ejercicio Bonus: Reporte Profesional de Evaluación (30 minutos)

### Contexto

Como científico de datos profesional, necesitas comunicar la calidad de tus modelos de manera clara y convincente a audiencias no técnicas.

### Tareas

**Bonus.1 Dashboard de métricas**

- Crea un dashboard visual que muestre todas las métricas importantes
- Incluye comparaciones entre modelos
- Hazlo comprensible para directivos deportivos

**Bonus.2 Reporte ejecutivo**

Escribe un reporte de 1 página que incluya:

- **Resumen ejecutivo:** ¿Cuál es el mejor modelo y por qué?
- **Métricas clave:** Las 3 métricas más importantes
- **Confianza:** ¿Qué tan confiables son las predicciones?
- **Recomendaciones:** ¿Cómo usar el modelo en la práctica?
- **Limitaciones:** ¿Qué no puede hacer el modelo?

**Bonus.3 Análisis de casos de uso**

- **Caso 1:** Apostar en partidos - ¿Qué métricas importan más?
- **Caso 2:** Planificación de equipo - ¿Qué tipo de errores son aceptables?
- **Caso 3:** Análisis mediático - ¿Qué nivel de confianza se necesita?

### Entregables

- Dashboard visual profesional
- Reporte ejecutivo de 1 página
- Análisis específico por casos de uso

---

## Criterios de Evaluación

### Competencia Técnica (40%)

- **Cálculo correcto:** Todas las métricas calculadas apropiadamente
- **Implementación:** Validación cruzada y análisis estadístico correctos
- **Visualizaciones:** Gráficos claros y informativos

### Análisis e Interpretación (40%)

- **Comprensión profunda:** Interpretación correcta de cada métrica
- **Pensamiento crítico:** Identificación de fortalezas y limitaciones
- **Contexto deportivo:** Aplicación apropiada al dominio futbolístico

### Comunicación Profesional (20%)

- **Claridad:** Explicaciones comprensibles para audiencias no técnicas
- **Recomendaciones:** Sugerencias prácticas y actionables
- **Presentación:** Organización profesional de resultados

## Recursos de Apoyo

### Documentación Técnica

- [Scikit-learn Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [ROC Curves Explained](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)
- [Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)

### Conceptos Clave

- **Precision vs Recall:** Trade-off entre exactitud y completitud
- **ROC-AUC:** Capacidad discriminativa del modelo
- **Cross-validation:** Validación robusta de rendimiento
- **Statistical Significance:** Confianza en las diferencias observadas

## Entrega

- **Formato:** Jupyter Notebook (.ipynb) + Reporte PDF (1 página)
- **Nombre:** `apellido_nombre_semana13_evaluacion_modelos.ipynb`
- **Fecha límite:** [Definir según cronograma]
- **Plataforma:** [Especificar LMS o sistema de entrega]

---

*¡Excelente! Ya sabes evaluar modelos como un profesional. En la próxima semana aprenderemos a mejorar nuestros modelos mediante feature engineering y optimización avanzada.*

**Tiempo total estimado:** 3-4 horas  
**Dificultad:** ⭐⭐⭐⭐ (Alto)  
**Prerrequisitos:** Completar Ejercicios Semanas 11-12
