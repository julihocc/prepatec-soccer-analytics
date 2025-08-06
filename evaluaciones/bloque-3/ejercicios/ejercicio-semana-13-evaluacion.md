# Ejercicio Semana 13: Métricas Avanzadas de Evaluación

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 13 - Evaluación Avanzada de Modelos  
**Tiempo estimado:** 60 minutos  
**Tipo:** Individual  
**Puntuación:** 100 puntos (25 puntos por parte)

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Implementar** múltiples métricas de evaluación más allá de accuracy
2. **Interpretar** matrices de confusión y curvas ROC para modelos deportivos
3. **Evaluar** la robustez de modelos con validación cruzada avanzada
4. **Generar** reportes profesionales de evaluación de modelos

## Contexto del Problema

Trabajaremos como analistas para **Atlético de Madrid**, evaluando la efectividad real de nuestros modelos predictivos. No basta con conocer el accuracy general; necesitamos entender exactamente qué tan bien funcionan nuestros modelos en diferentes situaciones para tomar decisiones estratégicas fundamentadas.

---

# Ejercicio Integrador: Laboratorio de Evaluación Atlético de Madrid

## Parte 1: Implementación de Métricas Avanzadas (25 puntos)

### Objetivo
Desarrollar un sistema completo de evaluación con múltiples métricas para modelos del Atlético de Madrid.

### Instrucciones Detalladas

**Paso 1:** Configura laboratorio de evaluación avanzada:

```python
# Configuración del laboratorio de evaluación Atlético de Madrid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score,
    roc_curve, precision_recall_curve, average_precision_score
)
from sklearn.model_selection import validation_curve, learning_curve
import warnings
warnings.filterwarnings('ignore')

# Configuración visual Atlético de Madrid
colores_atletico = ['#CE2524', '#FFFFFF', '#223447', '#FFD700']
sns.set_theme(style="whitegrid", palette=colores_atletico)
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11

print("=== LABORATORIO EVALUACIÓN ATLÉTICO DE MADRID ===")
print("Sistema avanzado de métricas de evaluación iniciado")
print("¡Análisis exhaustivo de modelos en marcha!")
```

**Paso 2:** Genera dataset realista del Atlético:

```python
# Dataset optimizado para Atlético de Madrid

# TU CÓDIGO AQUÍ:
# 1. Crear dataset de 500 partidos del Atlético de Madrid
# 2. Incluir variables específicas del estilo del Atlético:
#    - solidez_defensiva: Rating defensivo (1-10)
#    - efectividad_contraataque: % goles en contraataque
#    - condicion_fisica: Estado físico del equipo (1-10)
#    - intensidad_partido: Nivel de intensidad esperado (1-10)
#    - experiencia_plantilla: Años promedio experiencia
#    - motivacion_extra: Factor motivacional especial (0-1)
# 3. Variable objetivo: 'victoria_convincente' (1 si ganó sin sufrir, 0 si no)
# 4. Crear distribución realista (35% victorias convincentes)

np.random.seed(456)  # Para reproducibilidad

# Generar datos del Atlético
partidos_atletico = []
for i in range(500):
    # Variables características del Atlético
    solidez_defensiva = np.random.normal(8.5, 1.2)
    efectividad_contraataque = np.random.normal(45, 12)
    condicion_fisica = np.random.normal(8.0, 1.0)
    intensidad_partido = np.random.normal(7.5, 1.5)
    experiencia_plantilla = np.random.normal(6.2, 2.0)
    motivacion_extra = np.random.beta(2, 5)  # Sesgado hacia valores bajos
    
    # Probabilidad de victoria convincente
    prob_victoria = (
        solidez_defensiva * 0.15 + 
        efectividad_contraataque * 0.01 + 
        condicion_fisica * 0.12 + 
        intensidad_partido * 0.08 + 
        experiencia_plantilla * 0.1 + 
        motivacion_extra * 1.5
    ) / 10
    
    # Ajustar para tener ~35% de victorias convincentes
    prob_victoria = max(0, min(1, prob_victoria * 0.8))
    
    partido = {
        'solidez_defensiva': solidez_defensiva,
        'efectividad_contraataque': efectividad_contraataque,
        'condicion_fisica': condicion_fisica,
        'intensidad_partido': intensidad_partido,
        'experiencia_plantilla': experiencia_plantilla,
        'motivacion_extra': motivacion_extra,
        'victoria_convincente': 1 if np.random.random() < prob_victoria else 0
    }
    partidos_atletico.append(partido)

df_atletico = pd.DataFrame(partidos_atletico)

print("=== DATASET ATLÉTICO GENERADO ===")
print(f"Total partidos: {len(df_atletico)}")
print(f"Distribución victorias convincentes: {df_atletico['victoria_convincente'].value_counts()}")
print(f"Porcentaje victorias convincentes: {df_atletico['victoria_convincente'].mean():.1%}")
```

### Criterios de Evaluación
- **Configuración correcta del entorno de evaluación** (10 puntos)
- **Dataset realista con variables específicas del Atlético** (15 puntos)

---

## Parte 2: Análisis Detallado con Múltiples Métricas (25 puntos)

### Objetivo
Implementar y comparar múltiples métricas de evaluación para entender mejor el rendimiento de modelos.

### Instrucciones Detalladas

**Paso 3:** Entrena modelos y calcula métricas completas:

```python
# Sistema completo de evaluación de modelos

# TU CÓDIGO AQUÍ:
# 1. Preparar datos y división train/test
# 2. Entrenar 3 modelos diferentes
# 3. Calcular accuracy, precision, recall, F1-score para cada modelo
# 4. Generar classification reports detallados
# 5. Crear matrices de confusión informativas

# Preparar datos
features = ['solidez_defensiva', 'efectividad_contraataque', 'condicion_fisica', 
           'intensidad_partido', 'experiencia_plantilla', 'motivacion_extra']
X = df_atletico[features]
y = df_atletico['victoria_convincente']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Modelos para evaluar
modelos = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Regresión Logística': LogisticRegression(random_state=42)
}

# Diccionario para almacenar resultados
evaluaciones = {}

for nombre, modelo in modelos.items():
    # Entrenar modelo
    modelo.fit(X_train, y_train)
    
    # Predicciones
    y_pred = modelo.predict(X_test)
    y_proba = modelo.predict_proba(X_test)[:, 1]
    
    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    
    evaluaciones[nombre] = {
        'modelo': modelo,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'auc': auc,
        'y_pred': y_pred,
        'y_proba': y_proba
    }
    
    print(f"\n=== {nombre.upper()} ===")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1-Score: {f1:.3f}")
    print(f"AUC: {auc:.3f}")

print("\n=== EVALUACIÓN COMPLETA FINALIZADA ===")
```

**Paso 4:** Visualiza métricas comparativas:

```python
# Visualización comparativa de métricas

# TU CÓDIGO AQUÍ:
# 1. Crear gráfico de barras con múltiples métricas
# 2. Generar matrices de confusión para cada modelo
# 3. Crear tabla resumen de métricas
# 4. Identificar fortalezas/debilidades de cada modelo
# 5. Interpretar qué significa cada métrica para el Atlético

# DataFrame para comparación
metricas_df = pd.DataFrame.from_dict(
    {nombre: {metrica: datos[metrica] for metrica in ['accuracy', 'precision', 'recall', 'f1', 'auc']}
     for nombre, datos in evaluaciones.items()}, 
    orient='index'
)

# Visualización comparativa
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Gráfico de barras múltiples
ax1 = axes[0, 0]
metricas_df.plot(kind='bar', ax=ax1, color=colores_atletico[:len(metricas_df.columns)])
ax1.set_title('Comparación de Métricas: Atlético de Madrid', fontsize=14, fontweight='bold')
ax1.set_ylabel('Puntuación')
ax1.legend(title='Métricas')
ax1.tick_params(axis='x', rotation=45)

# Matrices de confusión
for i, (nombre, datos) in enumerate(list(evaluaciones.items())[:3]):
    row = (i + 1) // 2
    col = (i + 1) % 2
    if i < 2:
        ax = axes[row, col]
        cm = confusion_matrix(y_test, datos['y_pred'])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', ax=ax,
                    xticklabels=['No Convincente', 'Convincente'],
                    yticklabels=['No Convincente', 'Convincente'])
        ax.set_title(f'Matriz Confusión: {nombre}')
        ax.set_xlabel('Predicción')
        ax.set_ylabel('Real')

plt.tight_layout()
plt.show()

# Tabla resumen
print("\n=== RESUMEN MÉTRICAS ATLÉTICO DE MADRID ===")
print(metricas_df.round(3))

# Interpretación
mejor_accuracy = metricas_df['accuracy'].idxmax()
mejor_precision = metricas_df['precision'].idxmax()
mejor_recall = metricas_df['recall'].idxmax()
mejor_f1 = metricas_df['f1'].idxmax()

print(f"\n📊 MEJORES MODELOS POR MÉTRICA:")
print(f"• Accuracy: {mejor_accuracy} ({metricas_df.loc[mejor_accuracy, 'accuracy']:.3f})")
print(f"• Precision: {mejor_precision} ({metricas_df.loc[mejor_precision, 'precision']:.3f})")
print(f"• Recall: {mejor_recall} ({metricas_df.loc[mejor_recall, 'recall']:.3f})")
print(f"• F1-Score: {mejor_f1} ({metricas_df.loc[mejor_f1, 'f1']:.3f})")
```

### Criterios de Evaluación
- **Implementación correcta de múltiples métricas** (15 puntos)
- **Visualizaciones informativas y análisis comparativo** (10 puntos)

---

## Parte 3: Validación Robusta y Curvas de Rendimiento (25 puntos)

### Objetivo
Implementar técnicas avanzadas de validación para asegurar que los modelos son robustos y confiables.

### Instrucciones Detalladas

**Paso 5:** Implementa validación cruzada avanzada:

```python
# Validación cruzada robusta

# TU CÓDIGO AQUÍ:
# 1. Implementar validación cruzada estratificada con k=5
# 2. Calcular múltiples métricas para cada fold
# 3. Analizar variabilidad del rendimiento
# 4. Identificar modelos más estables
# 5. Calcular intervalos de confianza

from sklearn.model_selection import cross_validate

# Métricas para validación cruzada
scoring = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']

# Validación cruzada para cada modelo
cv_resultados = {}
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for nombre, modelo in modelos.items():
    scores = cross_validate(modelo, X, y, cv=kfold, scoring=scoring, return_train_score=True)
    
    cv_resultados[nombre] = {}
    for metrica in scoring:
        test_scores = scores[f'test_{metrica}']
        train_scores = scores[f'train_{metrica}']
        
        cv_resultados[nombre][metrica] = {
            'test_mean': test_scores.mean(),
            'test_std': test_scores.std(),
            'train_mean': train_scores.mean(),
            'train_std': train_scores.std(),
            'overfitting': train_scores.mean() - test_scores.mean()
        }
    
    print(f"\n=== VALIDACIÓN CRUZADA: {nombre.upper()} ===")
    for metrica in scoring:
        resultado = cv_resultados[nombre][metrica]
        print(f"{metrica.upper()}:")
        print(f"  Test: {resultado['test_mean']:.3f} (±{resultado['test_std']:.3f})")
        print(f"  Train: {resultado['train_mean']:.3f} (±{resultado['train_std']:.3f})")
        print(f"  Overfitting: {resultado['overfitting']:.3f}")

print("\n=== VALIDACIÓN CRUZADA COMPLETADA ===")
```

**Paso 6:** Genera curvas de rendimiento ROC y Precision-Recall:

```python
# Curvas de rendimiento avanzadas

# TU CÓDIGO AQUÍ:
# 1. Generar curvas ROC para cada modelo
# 2. Crear curvas Precision-Recall
# 3. Calcular AUC para ambas curvas
# 4. Interpretar qué modelo es mejor según cada curva
# 5. Analizar trade-offs entre precision y recall

plt.figure(figsize=(15, 5))

# Subplot 1: Curvas ROC
plt.subplot(1, 3, 1)
for nombre, datos in evaluaciones.items():
    fpr, tpr, _ = roc_curve(y_test, datos['y_proba'])
    auc = datos['auc']
    plt.plot(fpr, tpr, label=f'{nombre} (AUC = {auc:.3f})', linewidth=2)

plt.plot([0, 1], [0, 1], 'k--', alpha=0.5)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curvas ROC: Atlético de Madrid')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: Curvas Precision-Recall
plt.subplot(1, 3, 2)
for nombre, datos in evaluaciones.items():
    precision_curve, recall_curve, _ = precision_recall_curve(y_test, datos['y_proba'])
    avg_precision = average_precision_score(y_test, datos['y_proba'])
    plt.plot(recall_curve, precision_curve, label=f'{nombre} (AP = {avg_precision:.3f})', linewidth=2)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Curvas Precision-Recall')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 3: Estabilidad de modelos
plt.subplot(1, 3, 3)
modelos_nombres = list(cv_resultados.keys())
f1_means = [cv_resultados[nombre]['f1']['test_mean'] for nombre in modelos_nombres]
f1_stds = [cv_resultados[nombre]['f1']['test_std'] for nombre in modelos_nombres]

bars = plt.bar(modelos_nombres, f1_means, yerr=f1_stds, capsize=5, 
               color=colores_atletico[:len(modelos_nombres)], alpha=0.7)
plt.title('Estabilidad F1-Score (CV)')
plt.ylabel('F1-Score')
plt.xticks(rotation=45)

# Añadir valores en barras
for bar, mean in zip(bars, f1_means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{mean:.3f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Análisis de estabilidad
print("\n=== ANÁLISIS DE ESTABILIDAD ===")
for nombre in modelos_nombres:
    f1_data = cv_resultados[nombre]['f1']
    overfitting = f1_data['overfitting']
    variabilidad = f1_data['test_std']
    
    estabilidad = "Estable" if variabilidad < 0.05 else "Inestable"
    sobreajuste = "Alto" if overfitting > 0.1 else "Bajo" if overfitting < 0.05 else "Moderado"
    
    print(f"{nombre}:")
    print(f"  Variabilidad: {variabilidad:.3f} ({estabilidad})")
    print(f"  Overfitting: {overfitting:.3f} ({sobreajuste})")
```

### Criterios de Evaluación
- **Implementación correcta de validación cruzada** (15 puntos)
- **Generación e interpretación de curvas ROC y PR** (10 puntos)

---

## Parte 4: Reporte Ejecutivo de Evaluación (25 puntos)

### Objetivo
Crear un reporte profesional que comunique efectivamente la calidad y confiabilidad de los modelos.

### Instrucciones Detalladas

**Paso 7:** Identifica el modelo óptimo considerando múltiples criterios:

```python
# Selección del modelo óptimo

# TU CÓDIGO AQUÍ:
# 1. Crear sistema de scoring multi-criterio
# 2. Ponderar diferentes aspectos (accuracy, estabilidad, interpretabilidad)
# 3. Calcular score final para cada modelo
# 4. Justificar selección del modelo recomendado
# 5. Analizar pros/contras de cada modelo

# Sistema de scoring ponderado
pesos = {
    'accuracy': 0.25,
    'precision': 0.20,
    'recall': 0.20,
    'f1': 0.20,
    'estabilidad': 0.15  # Inverso de la desviación estándar
}

# Calcular scores finales
scores_finales = {}
for nombre in modelos_nombres:
    score = 0
    
    # Métricas de rendimiento
    for metrica in ['accuracy', 'precision', 'recall', 'f1']:
        valor = cv_resultados[nombre][metrica]['test_mean']
        score += pesos[metrica] * valor
    
    # Estabilidad (inverso de desviación estándar)
    estabilidad = 1 - min(1, cv_resultados[nombre]['f1']['test_std'] * 2)
    score += pesos['estabilidad'] * estabilidad
    
    scores_finales[nombre] = score

# Ranking de modelos
ranking = sorted(scores_finales.items(), key=lambda x: x[1], reverse=True)

print("=== RANKING FINAL DE MODELOS ===")
for i, (nombre, score) in enumerate(ranking, 1):
    print(f"{i}. {nombre}: {score:.3f}")

modelo_recomendado = ranking[0][0]
print(f"\n🏆 MODELO RECOMENDADO: {modelo_recomendado}")
```

**Paso 8:** Genera reporte ejecutivo completo:

```python
# Reporte ejecutivo final para Atlético de Madrid

# TU CÓDIGO AQUÍ:
# 1. Resumir metodología de evaluación
# 2. Presentar hallazgos clave sobre cada modelo
# 3. Recomendar modelo final con justificación
# 4. Incluir limitaciones y próximos pasos
# 5. Proporcionar guías de implementación

print("=" * 80)
print("ATLÉTICO DE MADRID - REPORTE EVALUACIÓN DE MODELOS")
print("Análisis Exhaustivo de Calidad y Confiabilidad Predictiva")
print("=" * 80)

print("\n📋 METODOLOGÍA DE EVALUACIÓN:")
print("• Validación cruzada estratificada (5 folds)")
print("• Múltiples métricas: Accuracy, Precision, Recall, F1, AUC")
print("• Análisis de estabilidad y overfitting")
print("• Curvas ROC y Precision-Recall")
print("• Sistema de scoring multi-criterio")

print(f"\n🏆 MODELO RECOMENDADO: {modelo_recomendado}")
modelo_data = cv_resultados[modelo_recomendado]
print(f"• F1-Score: {modelo_data['f1']['test_mean']:.3f} (±{modelo_data['f1']['test_std']:.3f})")
print(f"• Precision: {modelo_data['precision']['test_mean']:.3f}")
print(f"• Recall: {modelo_data['recall']['test_mean']:.3f}")
print(f"• Score Final: {scores_finales[modelo_recomendado]:.3f}")

print("\n📊 ANÁLISIS POR MODELO:")
for nombre in modelos_nombres:
    data = cv_resultados[nombre]
    print(f"\n{nombre.upper()}:")
    print(f"  ✓ Fortalezas:")
    
    # Identificar fortalezas
    if data['precision']['test_mean'] > 0.7:
        print(f"    - Alta precisión ({data['precision']['test_mean']:.3f})")
    if data['recall']['test_mean'] > 0.7:
        print(f"    - Alto recall ({data['recall']['test_mean']:.3f})")
    if data['f1']['test_std'] < 0.05:
        print(f"    - Muy estable (std: {data['f1']['test_std']:.3f})")
    
    print(f"  ⚠ Consideraciones:")
    if data['f1']['overfitting'] > 0.1:
        print(f"    - Posible overfitting ({data['f1']['overfitting']:.3f})")
    if data['f1']['test_std'] > 0.08:
        print(f"    - Variabilidad alta ({data['f1']['test_std']:.3f})")

print("\n⚽ INSIGHTS PARA EL ATLÉTICO:")
print("1. La solidez defensiva es crucial para victorias convincentes")
print("2. Los contraataques efectivos aumentan significativamente las probabilidades")
print("3. La experiencia de la plantilla es un factor diferencial")
print("4. La motivación extra puede ser determinante en partidos clave")

print("\n🚀 RECOMENDACIONES DE IMPLEMENTACIÓN:")
print("1. Usar el modelo recomendado para decisiones estratégicas principales")
print("2. Monitorear métricas de rendimiento semanalmente")
print("3. Reentrenar modelo mensualmente con nuevos datos")
print("4. Establecer umbrales de alerta para degradación del rendimiento")

print("\n⚙️ LIMITACIONES Y PRÓXIMOS PASOS:")
print("• Limitación: Dataset simulado, necesita datos reales")
print("• Próximo: Incorporar datos de jugadores individuales")
print("• Próximo: Añadir variables contextuales (rival, competición)")
print("• Próximo: Desarrollar modelos específicos por tipo de partido")

# Dashboard final
plt.figure(figsize=(16, 10))

# Comparación final de métricas
plt.subplot(2, 3, 1)
for metrica in ['accuracy', 'precision', 'recall', 'f1']:
    valores = [cv_resultados[nombre][metrica]['test_mean'] for nombre in modelos_nombres]
    plt.plot(modelos_nombres, valores, marker='o', label=metrica, linewidth=2)
plt.title('Comparación de Métricas')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Estabilidad
plt.subplot(2, 3, 2)
estabilidades = [1 - cv_resultados[nombre]['f1']['test_std'] for nombre in modelos_nombres]
bars = plt.bar(modelos_nombres, estabilidades, color=colores_atletico[:len(modelos_nombres)])
plt.title('Estabilidad de Modelos')
plt.ylabel('Estabilidad (1 - std)')
plt.xticks(rotation=45)

# Score final
plt.subplot(2, 3, 3)
scores = list(scores_finales.values())
bars = plt.bar(modelos_nombres, scores, color=colores_atletico[:len(modelos_nombres)])
plt.title('Score Final Multi-Criterio')
plt.ylabel('Score Ponderado')
plt.xticks(rotation=45)

# Overfitting analysis
plt.subplot(2, 3, 4)
overfit_values = [cv_resultados[nombre]['f1']['overfitting'] for nombre in modelos_nombres]
bars = plt.bar(modelos_nombres, overfit_values, color='red', alpha=0.6)
plt.axhline(y=0.05, color='green', linestyle='--', label='Umbral Aceptable')
plt.title('Análisis de Overfitting')
plt.ylabel('Train - Test F1')
plt.xticks(rotation=45)
plt.legend()

# Matriz de confusión del mejor modelo
plt.subplot(2, 3, 5)
mejor_pred = evaluaciones[modelo_recomendado]['y_pred']
cm = confusion_matrix(y_test, mejor_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds',
            xticklabels=['No Convincente', 'Convincente'],
            yticklabels=['No Convincente', 'Convincente'])
plt.title(f'Matriz Confusión: {modelo_recomendado}')

# Distribución de predicciones
plt.subplot(2, 3, 6)
mejor_proba = evaluaciones[modelo_recomendado]['y_proba']
plt.hist(mejor_proba[y_test == 0], alpha=0.5, label='No Convincente', bins=20)
plt.hist(mejor_proba[y_test == 1], alpha=0.5, label='Convincente', bins=20)
plt.title('Distribución de Probabilidades')
plt.xlabel('Probabilidad Predicha')
plt.ylabel('Frecuencia')
plt.legend()

plt.suptitle('Dashboard Evaluación Completa: Atlético de Madrid', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Criterios de Evaluación
- **Sistema de scoring multi-criterio robusto** (15 puntos)
- **Reporte ejecutivo completo y profesional** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Implementación correcta de múltiples métricas de evaluación
- Validación cruzada apropiada y análisis de estabilidad
- Generación correcta de curvas ROC y Precision-Recall
- Sistema de scoring multi-criterio bien fundamentado

### Aplicación Práctica (30 puntos)
- Interpretación correcta de métricas en contexto deportivo
- Identificación apropiada de fortalezas y debilidades de modelos
- Recomendaciones prácticas para implementación
- Análisis realista de limitaciones y próximos pasos

### Claridad y Documentación (30 puntos)
- Explicaciones claras de cada métrica y su importancia
- Visualizaciones informativas y bien diseñadas
- Reporte ejecutivo profesional y comprensible
- Código bien estructurado y comentado

## Instrucciones de Entrega

1. **Implementa todas las métricas** de evaluación correctamente
2. **Incluye análisis comparativo** detallado entre modelos
3. **Verifica funcionamiento** de validación cruzada y curvas
4. **Guarda como:** `[matricula]-ejercicio-semana-13.ipynb`
5. **Entrega antes del final de Semana 13**

## Recursos de Apoyo

- Notebook de la Semana 13: `metricas-avanzadas-evaluacion.ipynb`
- Documentación scikit-learn: Métricas de evaluación
- Guía de interpretación de curvas ROC y Precision-Recall

---

**¡Convierte al Atlético de Madrid en el equipo con la evaluación de modelos más rigurosa del fútbol mundial!** ⚽📊

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
