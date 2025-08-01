# Ejercicio Semanal - Semana 11: Mi Primera Predicción

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 11 - Modelado Predictivo: Introducción  
**Tiempo estimado:** 3-4 horas  
**Tipo:** Individual  

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Comprender** los conceptos básicos del machine learning aplicado al fútbol
2. **Implementar** su primera predicción usando scikit-learn
3. **Crear** modelos simples de clasificación binaria
4. **Aplicar** conceptos de entrenamiento y prueba de modelos
5. **Interpretar** resultados de predicciones básicas

## Contexto del Problema

¡Bienvenido al mundo de las predicciones deportivas! Como analista de datos, tu primera misión es crear un modelo que pueda predecir si un equipo ganará jugando como local. Utilizarás datos históricos de partidos para "entrenar" a tu modelo y luego probarlo con partidos nuevos.

**Pregunta central:** *¿Podemos predecir si un equipo ganará en casa basándonos en sus estadísticas históricas?*

---

## Ejercicio 1: Preparación de Datos para Predicción (1 hora)

### Contexto
Antes de crear cualquier modelo predictivo, necesitamos preparar nuestros datos correctamente. Esto incluye crear variables que el modelo pueda "entender" y dividir los datos en conjuntos de entrenamiento y prueba.

### Tareas

**1.1 Carga y exploración inicial**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
sns.set_theme(style="whitegrid", palette="viridis")
```

**1.2 Crear dataset de entrenamiento**
- Genera un dataset con al menos 500 partidos históricos
- Incluye variables: `equipo_local`, `goles_local`, `goles_visitante`, `posesion_local`, `tiros_local`, `faltas_local`, `tarjetas_amarillas_local`, `tarjetas_rojas_local`
- Crea variables adicionales: `diferencia_goles_historica`, `promedio_goles_casa`, `victorias_consecutivas_casa`

**1.3 Variable objetivo (target)**
- Crea la variable `gano_local` (1 si el equipo local ganó, 0 si no)
- Explica por qué esta es una buena variable para predecir

**1.4 División de datos**
- Divide el dataset en 70% entrenamiento y 30% prueba
- Explica por qué es importante esta división

### Entregables
- Código funcional con dataset creado
- Variable objetivo correctamente definida
- División train/test implementada
- Explicación de cada paso

---

## Ejercicio 2: Mi Primer Modelo Predictivo (1.5 horas)

### Contexto
Ahora crearás tu primer modelo de machine learning usando Regresión Logística, uno de los algoritmos más simples y efectivos para predicciones binarias (sí/no, ganó/perdió).

### Tareas

**2.1 Preparación de variables predictoras**
- Selecciona las mejores variables para predecir (`goles_local`, `posesion_local`, `tiros_local`, etc.)
- Explica por qué elegiste esas variables

**2.2 Entrenamiento del modelo**
```python
# Tu código aquí
modelo_logistico = LogisticRegression()
# Entrena el modelo con los datos de entrenamiento
```

**2.3 Primeras predicciones**
- Usa el modelo entrenado para predecir los datos de prueba
- Calcula la precisión (accuracy) del modelo
- Interpreta el resultado: ¿es bueno predecir correctamente el 65% de las veces?

**2.4 Análisis de casos específicos**
- Elige 10 partidos de prueba y compara predicciones vs resultados reales
- Identifica patrones: ¿cuándo el modelo acierta más y cuándo falla?

### Entregables
- Modelo de regresión logística entrenado
- Predicciones realizadas y precisión calculada
- Análisis de casos específicos
- Interpretación de resultados

---

## Ejercicio 3: Comparando Modelos - ¿Cuál es Mejor? (1 hora)

### Contexto
En machine learning, nunca dependemos de un solo algoritmo. Es importante probar diferentes "cerebros" (modelos) para ver cuál funciona mejor con nuestros datos.

### Tareas

**3.1 Segundo modelo: Random Forest**
```python
# Crear y entrenar un modelo Random Forest
modelo_bosque = RandomForestClassifier(n_estimators=50, random_state=42)
# Tu código aquí
```

**3.2 Comparación de modelos**
- Entrena ambos modelos con los mismos datos
- Compara las precisiones de ambos
- Crea una tabla comparativa

**3.3 Análisis de importancia de variables**
- Usa Random Forest para identificar qué variables son más importantes
- Crea un gráfico de importancia de variables
- Interpreta los resultados: ¿qué factores son más predictivos?

**3.4 Predicciones en casos extremos**
- Crea 3 escenarios hipotéticos:
  1. Equipo con estadísticas muy buenas
  2. Equipo con estadísticas promedio  
  3. Equipo con estadísticas muy malas
- Compara las predicciones de ambos modelos

### Entregables
- Dos modelos entrenados y comparados
- Gráfico de importancia de variables
- Análisis de casos extremos
- Conclusiones sobre cuál modelo es mejor

---

## Ejercicio 4: Validación y Confianza en las Predicciones (30 minutos)

### Contexto
Un buen científico de datos siempre cuestiona sus resultados. ¿Realmente funciona mi modelo o solo tuve suerte? Vamos a validar nuestros resultados.

### Tareas

**4.1 Validación cruzada simple**
- Divide los datos originales de manera diferente (80%-20%)
- Entrena nuevamente ambos modelos
- Compara si los resultados son similares

**4.2 Análisis de confianza**
- Identifica predicciones donde ambos modelos coinciden
- Identifica predicciones donde difieren
- ¿En qué casos tienes más confianza en las predicciones?

**4.3 Recomendaciones prácticas**
- Basándote en tus resultados, ¿recomendarías usar este modelo en la vida real?
- ¿Qué limitaciones tiene?
- ¿Qué mejorarías?

### Entregables
- Validación cruzada implementada
- Análisis de confianza en predicciones
- Recomendaciones prácticas

---

## Ejercicio Bonus: Predicción de Partidos Reales (30 minutos)

### Contexto
¡Hora de poner a prueba tu modelo con partidos que realmente pasaron! Busca datos de partidos recientes y haz predicciones.

### Tareas

**Bonus.1 Datos reales**
- Busca estadísticas de 5 partidos recientes de tu liga favorita
- Aplica tus modelos para predecir quién ganó
- Compara con los resultados reales

**Bonus.2 Reflexión final**
- ¿Qué tan bien funcionó tu modelo con datos reales?
- ¿Qué aprendiste sobre las predicciones deportivas?
- ¿Qué harías diferente en tu próximo modelo?

### Entregables
- Predicciones de partidos reales
- Comparación con resultados reales
- Reflexión personal sobre el proceso

---

## Criterios de Evaluación

### Competencia Técnica (40%)
- **Correctitud:** Código ejecuta sin errores
- **Implementación:** Modelos correctamente entrenados y utilizados
- **Buenas prácticas:** División adecuada de datos, uso correcto de librerías

### Análisis y Interpretación (35%)
- **Comprensión:** Explicaciones claras de cada paso
- **Interpretación:** Análisis correcto de resultados y métricas
- **Pensamiento crítico:** Identificación de limitaciones y mejoras

### Aplicación Práctica (25%)
- **Relevancia:** Análisis apropiado en contexto futbolístico
- **Creatividad:** Insights adicionales o enfoques originales
- **Comunicación:** Presentación clara de resultados y conclusiones

## Recursos de Apoyo

### Documentación Recomendada
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Logistic Regression Explained](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [Random Forest Guide](https://scikit-learn.org/stable/modules/ensemble.html#forest)

### Conceptos Clave
- **Supervised Learning:** Aprendizaje con ejemplos etiquetados
- **Classification:** Predecir categorías (ganó/perdió)
- **Training/Test Split:** División para validar modelos
- **Feature Importance:** Qué variables son más predictivas

## Entrega

- **Formato:** Jupyter Notebook (.ipynb)
- **Nombre:** `apellido_nombre_semana11_modelado.ipynb`
- **Fecha límite:** [Definir según cronograma]
- **Plataforma:** [Especificar LMS o sistema de entrega]

---

*¡Felicitaciones! Has dado tu primer paso en el mundo del machine learning aplicado al fútbol. En la próxima semana exploraremos modelos más avanzados y técnicas de optimización.*

**Tiempo total estimado:** 3-4 horas  
**Dificultad:** ⭐⭐⭐ (Intermedio-Alto)  
**Prerrequisitos:** Completar Bloques 1 y 2
