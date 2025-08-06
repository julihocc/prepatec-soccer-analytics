# Ejercicio Semana 11: Mi Primera Predicción Deportiva

## Información General

**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 11  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 11  
**Archivo entrega:** `[matricula]-ejercicio-semana-11.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Comprender los conceptos básicos del machine learning aplicado al fútbol
- Implementar su primera predicción usando scikit-learn
- Crear modelos simples de clasificación binaria  
- Aplicar conceptos de entrenamiento y prueba de modelos
- Interpretar resultados básicos de predicciones deportivas

## Prerrequisitos

- Ejercicios completos de los Bloques 1 y 2
- Conocimiento sólido de análisis exploratorio y estadística
- Familiaridad con pandas, numpy y visualización
- Comprensión básica de conceptos de machine learning

## Contexto del Ejercicio

Eres el **científico de datos** del Real Madrid CF. El cuerpo técnico quiere implementar un sistema predictivo básico para:

- Predecir probabilidades de victoria en partidos de local
- Identificar factores clave que influyen en el resultado
- Tomar decisiones tácticas basadas en datos históricos
- Desarrollar ventajas competitivas mediante análisis predictivo

---

# Ejercicio Integrador: Sistema Predictivo Real Madrid CF

## Parte 1: Preparación de Datos para Predicción (25 puntos)

### Objetivo
Configurar el entorno de machine learning y preparar datos históricos del Real Madrid para entrenamiento predictivo.

### Instrucciones Detalladas

**Paso 1:** Configura el laboratorio de machine learning:

```python
# Configuración del laboratorio predictivo Real Madrid CF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuración visual Real Madrid
colores_madrid = ['#FEBE10', '#00529F', '#FFFFFF', '#212121']
sns.set_theme(style="whitegrid", palette=colores_madrid)
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

print("=== LABORATORIO PREDICTIVO REAL MADRID CF ===")
print("Sistema de predicción deportiva iniciado")
print("¡Herramientas de machine learning listas!")
```

**Paso 2:** Crea dataset de entrenamiento con datos históricos:

```python
# Crear dataset histórico del Real Madrid (simulado)

# TU CÓDIGO AQUÍ:
# 1. Generar 300 partidos históricos del Real Madrid como local
# 2. Crear variables predictoras realistas:
#    - goles_favor_ultimos_5: Promedio goles últimos 5 partidos
#    - posesion_promedio: Porcentaje de posesión histórica
#    - tiros_por_partido: Promedio de tiros al arco
#    - faltas_cometidas: Promedio de faltas por partido
#    - dias_descanso: Días entre partidos
# 3. Crear variable objetivo 'victoria_local' (1=victoria, 0=no victoria)
# 4. Incluir variabilidad realista en los datos
# 5. Verificar distribución balanceada de la variable objetivo

np.random.seed(42)  # Para reproducibilidad

# Ejemplo de estructura:
partidos_madrid = []
for i in range(300):
    partido = {
        'fecha': f'2023-{(i//30)+1:02d}-{(i%30)+1:02d}',
        'rival': f'Equipo_{i%20}',
        'goles_favor_ultimos_5': np.random.normal(2.1, 0.6),
        'posesion_promedio': np.random.normal(62, 8),
        'tiros_por_partido': np.random.normal(15, 4),
        'faltas_cometidas': np.random.normal(12, 3),
        'dias_descanso': np.random.choice([3, 4, 7], p=[0.4, 0.3, 0.3])
    }
    # Calcular probabilidad de victoria basada en variables
    # Tu implementación aquí
    partidos_madrid.append(partido)

df_madrid = pd.DataFrame(partidos_madrid)

print("=== DATASET REAL MADRID GENERADO ===")
print(f"Total partidos: {len(df_madrid)}")
print(f"Distribución victoria_local: {df_madrid['victoria_local'].value_counts()}")
```

### Criterios de Evaluación
- **Configuración correcta del entorno ML** (10 puntos)
- **Dataset histórico realista y balanceado** (15 puntos)

---

## Parte 2: Primer Modelo de Clasificación (25 puntos)

### Objetivo
Implementar el primer modelo predictivo del Real Madrid usando regresión logística.

### Instrucciones Detalladas

**Paso 3:** Prepara datos para entrenamiento:

```python
# Preparación de variables para machine learning

# TU CÓDIGO AQUÍ:
# 1. Seleccionar variables predictoras (features):
#    ['goles_favor_ultimos_5', 'posesion_promedio', 'tiros_por_partido', 'faltas_cometidas', 'dias_descanso']
# 2. Definir variable objetivo (target): 'victoria_local'
# 3. Dividir datos en entrenamiento (70%) y prueba (30%)
# 4. Verificar que ambos conjuntos mantienen distribución balanceada
# 5. Mostrar estadísticas descriptivas de variables predictoras

# Preparar matrices X (predictoras) e y (objetivo)
features = ['goles_favor_ultimos_5', 'posesion_promedio', 'tiros_por_partido', 'faltas_cometidas', 'dias_descanso']
X = df_madrid[features]
y = df_madrid['victoria_local']

# División train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("=== PREPARACIÓN DE DATOS COMPLETADA ===")
print(f"Entrenamiento: {X_train.shape[0]} partidos")
print(f"Prueba: {X_test.shape[0]} partidos")
print(f"Variables predictoras: {len(features)}")
```

**Paso 4:** Entrena tu primer modelo predictivo:

```python
# Entrenamiento del primer modelo: Regresión Logística

# TU CÓDIGO AQUÍ:
# 1. Crear modelo de Regresión Logística
# 2. Entrenar (fit) el modelo con datos de entrenamiento
# 3. Realizar predicciones en conjunto de prueba
# 4. Calcular precisión (accuracy) del modelo
# 5. Generar reporte de clasificación completo
# 6. Interpretar coeficientes del modelo (cuáles variables son más importantes)

# Crear y entrenar modelo
modelo_logistico = LogisticRegression(random_state=42)
modelo_logistico.fit(X_train, y_train)

# Predicciones
y_pred = modelo_logistico.predict(X_test)
y_pred_proba = modelo_logistico.predict_proba(X_test)[:, 1]

# Evaluación
accuracy = accuracy_score(y_test, y_pred)

print("=== PRIMER MODELO REAL MADRID ===")
print(f"Precisión del modelo: {accuracy:.3f}")
print("\nReporte detallado:")
print(classification_report(y_test, y_pred))

print("\nImportancia de variables:")
for feature, coef in zip(features, modelo_logistico.coef_[0]):
    print(f"{feature}: {coef:.3f}")
```

### Criterios de Evaluación
- **Preparación correcta de datos** (10 puntos)
- **Implementación exitosa del modelo** (15 puntos)

---

## Parte 3: Análisis y Validación del Modelo (25 puntos)

### Objetivo
Analizar el rendimiento del modelo y validar su utilidad práctica para el Real Madrid.

### Instrucciones Detalladas

**Paso 5:** Analiza el rendimiento en profundidad:

```python
# Análisis detallado del rendimiento predictivo

# TU CÓDIGO AQUÍ:
# 1. Crear matriz de confusión y visualizarla
# 2. Calcular métricas específicas:
#    - Verdaderos positivos, falsos positivos
#    - Sensibilidad (recall) y especificidad
#    - Precisión por clase
# 3. Analizar casos de predicciones incorrectas
# 4. Identificar patrones en errores del modelo
# 5. Evaluar utilidad práctica para decisiones del Real Madrid

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Victoria', 'Victoria'],
            yticklabels=['No Victoria', 'Victoria'])
plt.title('Matriz de Confusión: Predicciones Real Madrid', fontsize=14, fontweight='bold')
plt.xlabel('Predicción')
plt.ylabel('Realidad')
plt.show()

print("=== ANÁLISIS DE RENDIMIENTO ===")
print(f"Verdaderos Positivos: {cm[1,1]}")
print(f"Falsos Positivos: {cm[0,1]}")
print(f"Verdaderos Negativos: {cm[0,0]}")
print(f"Falsos Negativos: {cm[1,0]}")

# Análisis de errores
errores = X_test[y_test != y_pred].copy()
errores['prediccion'] = y_pred[y_test != y_pred]
errores['realidad'] = y_test[y_test != y_pred]

print(f"\nTotal errores: {len(errores)}")
print("Características promedio de predicciones incorrectas:")
print(errores[features].describe())
```

**Paso 6:** Valida la utilidad práctica del modelo:

```python
# Validación práctica para uso del Real Madrid

# TU CÓDIGO AQUÍ:
# 1. Simular predicciones para próximos 5 partidos
# 2. Incluir intervalos de confianza en predicciones
# 3. Crear recomendaciones tácticas basadas en probabilidades
# 4. Evaluar cuándo el modelo es más/menos confiable
# 5. Proponer estrategias para mejora continua

# Simular próximos partidos
proximos_partidos = pd.DataFrame({
    'goles_favor_ultimos_5': [2.2, 1.8, 2.5, 1.9, 2.1],
    'posesion_promedio': [65, 58, 70, 62, 66],
    'tiros_por_partido': [16, 12, 18, 14, 17],
    'faltas_cometidas': [10, 15, 8, 12, 11],
    'dias_descanso': [7, 3, 7, 4, 7]
})

# Predicciones
prob_victoria = modelo_logistico.predict_proba(proximos_partidos)[:, 1]
pred_victoria = modelo_logistico.predict(proximos_partidos)

print("=== PREDICCIONES PRÓXIMOS PARTIDOS ===")
for i, (prob, pred) in enumerate(zip(prob_victoria, pred_victoria)):
    resultado = "VICTORIA" if pred == 1 else "NO VICTORIA"
    confianza = "Alta" if prob > 0.7 or prob < 0.3 else "Media"
    print(f"Partido {i+1}: {resultado} (Prob: {prob:.2f}, Confianza: {confianza})")
```

### Criterios de Evaluación
- **Análisis detallado de rendimiento** (15 puntos)
- **Validación práctica y recomendaciones** (10 puntos)

---

## Parte 4: Comparación de Modelos y Reporte Ejecutivo (25 puntos)

### Objetivo
Comparar diferentes algoritmos y generar un reporte ejecutivo para el Real Madrid.

### Instrucciones Detalladas

**Paso 7:** Compara múltiples algoritmos:

```python
# Comparación de diferentes modelos predictivos

# TU CÓDIGO AQUÍ:
# 1. Implementar al menos 3 modelos diferentes:
#    - Regresión Logística (ya implementado)
#    - Random Forest
#    - Modelo baseline (predicción simple)
# 2. Entrenar todos con los mismos datos
# 3. Comparar rendimiento en conjunto de prueba
# 4. Identificar fortalezas/debilidades de cada modelo
# 5. Seleccionar el mejor modelo para el Real Madrid

# Random Forest
modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)
y_pred_rf = modelo_rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# Modelo baseline (predicción mayoritaria)
from scipy.stats import mode
prediccion_baseline = mode(y_train)[0][0]
y_pred_baseline = [prediccion_baseline] * len(y_test)
accuracy_baseline = accuracy_score(y_test, y_pred_baseline)

print("=== COMPARACIÓN DE MODELOS ===")
print(f"Regresión Logística: {accuracy:.3f}")
print(f"Random Forest: {accuracy_rf:.3f}")
print(f"Baseline: {accuracy_baseline:.3f}")

# Importancia de variables en Random Forest
importancias_rf = modelo_rf.feature_importances_
print("\nImportancia variables (Random Forest):")
for feature, imp in zip(features, importancias_rf):
    print(f"{feature}: {imp:.3f}")
```

**Paso 8:** Genera reporte ejecutivo final:

```python
# Reporte ejecutivo para la dirección del Real Madrid

# TU CÓDIGO AQUÍ:
# 1. Resumir hallazgos principales del análisis predictivo
# 2. Recomendar el mejor modelo para uso operativo
# 3. Identificar variables más importantes para victorias
# 4. Proponer estrategias basadas en insights del modelo
# 5. Establecer plan de monitoreo y mejora continua
# 6. Crear visualización resumen para presentación

print("=" * 60)
print("REAL MADRID CF - REPORTE SISTEMA PREDICTIVO")
print("Análisis de Modelos de Machine Learning")
print("=" * 60)

print("\n🎯 MODELO RECOMENDADO:")
mejor_modelo = "Random Forest" if accuracy_rf > accuracy else "Regresión Logística"
mejor_accuracy = max(accuracy_rf, accuracy)
print(f"• {mejor_modelo} (Precisión: {mejor_accuracy:.1%})")

print("\n📊 VARIABLES MÁS IMPORTANTES:")
if accuracy_rf > accuracy:
    for feature, imp in sorted(zip(features, importancias_rf), key=lambda x: x[1], reverse=True)[:3]:
        print(f"• {feature}: {imp:.1%}")
else:
    coefs_abs = np.abs(modelo_logistico.coef_[0])
    for feature, coef in sorted(zip(features, coefs_abs), key=lambda x: x[1], reverse=True)[:3]:
        print(f"• {feature}: {coef:.3f}")

print("\n🏆 RECOMENDACIONES ESTRATÉGICAS:")
print("1. Enfocar en mantener alta efectividad goleadora")
print("2. Monitorear días de descanso entre partidos")
print("3. Optimizar posesión de balón en partidos clave")

print("\n📈 PRÓXIMOS PASOS:")
print("1. Implementar sistema en tiempo real")
print("2. Reentrenar modelo mensualmente")
print("3. Integrar variables adicionales (clima, rivales)")

# Visualización resumen
plt.figure(figsize=(10, 6))
modelos = ['Baseline', 'Regresión\nLogística', 'Random\nForest']
accuracies = [accuracy_baseline, accuracy, accuracy_rf]

bars = plt.bar(modelos, accuracies, color=['gray', '#00529F', '#FEBE10'])
plt.title('Comparación de Modelos Predictivos - Real Madrid CF', fontsize=14, fontweight='bold')
plt.ylabel('Precisión')
plt.ylim(0, 1)

# Añadir valores en barras
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{acc:.1%}', ha='center', fontweight='bold')

plt.show()
```

### Criterios de Evaluación
- **Comparación correcta de múltiples modelos** (15 puntos)
- **Reporte ejecutivo profesional y completo** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Implementación correcta de modelos de machine learning
- Uso apropiado de train/test split y validación
- Cálculos precisos de métricas de evaluación
- Código ejecuta sin errores

### Aplicación Práctica (30 puntos)
- Análisis relevante para contexto Real Madrid
- Interpretación correcta de resultados del modelo
- Recomendaciones útiles para toma de decisiones
- Validación práctica de utilidad del modelo

### Claridad y Documentación (30 puntos)
- Código bien comentado en español
- Explicaciones claras de conceptos de ML
- Presentación profesional de resultados
- Variables y análisis con nombres descriptivos

## Instrucciones de Entrega

1. **Completa todos los modelos** con implementación correcta
2. **Incluye interpretaciones** para cada resultado del modelo
3. **Verifica funcionamiento** de todas las predicciones
4. **Guarda como:** `[matricula]-ejercicio-semana-11.ipynb`
5. **Entrega antes del final de Semana 11**

## Recursos de Apoyo

- Notebook de la Semana 11: `modelado-predictivo-introduccion.ipynb`
- Documentación scikit-learn: `train_test_split`, `LogisticRegression`, `RandomForestClassifier`
- Guía de métricas de evaluación en machine learning

---

**¡Desarrolla tu primer sistema predictivo y lleva al Real Madrid hacia el futuro del análisis deportivo!** ⚽🤖
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
