# Ejercicio Semana 15: Proyecto Final Integrador

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 15 - Proyecto Final del Curso  
**Tiempo estimado:** 60 minutos  
**Tipo:** Individual  
**Puntuación:** 100 puntos (25 puntos por parte)

## Objetivos de Aprendizaje

Al completar este proyecto final, el estudiante será capaz de:

1. **Integrar** todas las habilidades de programación, análisis y machine learning del curso
2. **Desarrollar** un sistema completo de análisis predictivo para Liverpool FC
3. **Presentar** resultados profesionales con visualizaciones impactantes
4. **Demostrar** competencia integral en data science aplicada al fútbol

## Contexto del Proyecto

Como analista senior del **Liverpool FC**, desarrollarás un sistema integral que combine todo el conocimiento adquirido en el curso. Tu misión es crear una herramienta completa que permita al club tomar decisiones estratégicas basadas en datos para la próxima temporada.

---

# Proyecto Final: Sistema de Análisis Integral Liverpool FC

## Parte 1: Dashboard de Análisis Exploratorio (25 puntos)

### Objetivo
Crear un sistema completo de análisis exploratorio que integre múltiples fuentes de datos del Liverpool FC.

### Instrucciones Detalladas

**Paso 1:** Construye dataset maestro del Liverpool FC:

```python
# Configuración del sistema integral Liverpool FC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuración visual Liverpool FC
colores_liverpool = ['#C8102E', '#F6EB61', '#00B2A9', '#FFFFFF']
sns.set_theme(style="whitegrid", palette=colores_liverpool)
plt.rcParams['figure.figsize'] = (16, 12)
plt.rcParams['font.size'] = 12

print("=" * 60)
print("🔴 LIVERPOOL FC - SISTEMA DE ANÁLISIS INTEGRAL")
print("Proyecto Final: Data Science para el Fútbol")
print("=" * 60)
```

**Paso 2:** Genera dataset completo multidimensional:

```python
# Dataset maestro Liverpool FC - Integración completa del curso

# TU CÓDIGO AQUÍ:
# 1. Crear dataset de 500 partidos históricos del Liverpool FC
# 2. Integrar TODAS las habilidades del curso:
#    BLOQUE 1: Estructuras de datos, funciones, pandas básico
#    BLOQUE 2: Análisis exploratorio, estadística, visualización
#    BLOQUE 3: Machine learning, feature engineering, evaluación
# 3. Variables base del Liverpool:
#    - pressing_intensidad: Intensidad de presión alta (1-10)
#    - transiciones_rapidas: Velocidad de transición (1-10) 
#    - solidez_defensiva: Rating defensivo (1-10)
#    - creatividad_ataque: Creatividad en ataque (1-10)
#    - condicion_fisica: Estado físico del equipo (1-10)
#    - ambiente_anfield: Factor casa en Anfield (1-10)
# 4. Variables derivadas (Feature Engineering):
#    - dominancia_total: (pressing + transiciones + creatividad) / 3
#    - equilibrio_equipo: min(solidez_defensiva, creatividad_ataque)
#    - factor_liverpool: pressing * ambiente_anfield / 10
# 5. Variable objetivo: 'actuacion_memorable' (partido destacado del Liverpool)

np.random.seed(2024)  # Año del proyecto

# Función para generar partidos del Liverpool (Programación Bloque 1)
def generar_partido_liverpool():
    """
    Función que genera un partido del Liverpool FC con todas las variables del curso.
    Integra conceptos de programación del Bloque 1.
    """
    # Variables base del estilo Liverpool
    pressing_intensidad = np.random.normal(8.5, 1.2)  # Liverpool conocido por pressing
    transiciones_rapidas = np.random.normal(8.0, 1.0)
    solidez_defensiva = np.random.normal(7.5, 1.3)
    creatividad_ataque = np.random.normal(8.2, 1.1)
    condicion_fisica = np.random.normal(8.0, 1.0)
    ambiente_anfield = np.random.normal(9.0, 0.8)  # Anfield es especial
    
    # Asegurar valores realistas (Control de flujo Bloque 1)
    variables = [pressing_intensidad, transiciones_rapidas, solidez_defensiva, 
                creatividad_ataque, condicion_fisica, ambiente_anfield]
    
    for i, var in enumerate(variables):
        variables[i] = max(1, min(10, var))
    
    pressing_intensidad, transiciones_rapidas, solidez_defensiva, creatividad_ataque, condicion_fisica, ambiente_anfield = variables
    
    # Feature Engineering (Bloque 3)
    dominancia_total = (pressing_intensidad + transiciones_rapidas + creatividad_ataque) / 3
    equilibrio_equipo = min(solidez_defensiva, creatividad_ataque)
    factor_liverpool = (pressing_intensidad * ambiente_anfield) / 10
    
    # Variables adicionales (Análisis Bloque 2)
    rival_fuerza = np.random.randint(1, 11)
    importancia_partido = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])  # 1=Liga, 2=Copa, 3=Champions
    
    # Probabilidad de actuación memorable
    prob_memorable = (
        dominancia_total * 0.15 +
        equilibrio_equipo * 0.12 +
        factor_liverpool * 0.10 +
        (11 - rival_fuerza) * 0.08 +
        importancia_partido * 0.05 +
        condicion_fisica * 0.08
    ) / 10
    
    return {
        'pressing_intensidad': pressing_intensidad,
        'transiciones_rapidas': transiciones_rapidas,
        'solidez_defensiva': solidez_defensiva,
        'creatividad_ataque': creatividad_ataque,
        'condicion_fisica': condicion_fisica,
        'ambiente_anfield': ambiente_anfield,
        'dominancia_total': dominancia_total,
        'equilibrio_equipo': equilibrio_equipo,
        'factor_liverpool': factor_liverpool,
        'rival_fuerza': rival_fuerza,
        'importancia_partido': importancia_partido,
        'actuacion_memorable': 1 if np.random.random() < prob_memorable else 0
    }

# Generar dataset completo usando programación del Bloque 1
print("Generando dataset maestro Liverpool FC...")
partidos_liverpool = []

# Usar bucles y estructuras del Bloque 1
for i in range(500):
    partido = generar_partido_liverpool()
    partidos_liverpool.append(partido)

# Crear DataFrame usando pandas del Bloque 1
df_liverpool = pd.DataFrame(partidos_liverpool)

print("=== DATASET MAESTRO LIVERPOOL FC GENERADO ===")
print(f"Total de partidos analizados: {len(df_liverpool)}")
print(f"Actuaciones memorables: {df_liverpool['actuacion_memorable'].sum()} ({df_liverpool['actuacion_memorable'].mean():.1%})")

# Estadísticas descriptivas (Bloque 2)
print("\n📊 ESTADÍSTICAS DESCRIPTIVAS DEL LIVERPOOL:")
variables_clave = ['pressing_intensidad', 'transiciones_rapidas', 'solidez_defensiva', 'creatividad_ataque']
for var in variables_clave:
    print(f"{var}: Media {df_liverpool[var].mean():.2f}, Std {df_liverpool[var].std():.2f}")
```

**Paso 3:** Crea dashboard exploratorio completo:

```python
# Dashboard de análisis exploratorio completo

# TU CÓDIGO AQUÍ:
# 1. Crear visualizaciones que demuestren habilidades del Bloque 2
# 2. Incluir análisis de distribuciones, correlaciones, patrones
# 3. Generar insights específicos del estilo de juego del Liverpool
# 4. Usar todas las técnicas de visualización aprendidas
# 5. Aplicar estadística descriptiva avanzada

# Dashboard principal (Visualización Bloque 2)
fig, axes = plt.subplots(3, 3, figsize=(20, 16))

# 1. Distribución de actuaciones memorables
axes[0, 0].pie(df_liverpool['actuacion_memorable'].value_counts(), 
               labels=['Normales', 'Memorables'], 
               colors=['#lightgray', '#C8102E'],
               autopct='%1.1f%%')
axes[0, 0].set_title('Distribución de Actuaciones', fontweight='bold', fontsize=14)

# 2. Histograma pressing vs transiciones
axes[0, 1].scatter(df_liverpool['pressing_intensidad'], df_liverpool['transiciones_rapidas'], 
                   c=df_liverpool['actuacion_memorable'], cmap='Reds', alpha=0.7)
axes[0, 1].set_xlabel('Intensidad de Pressing')
axes[0, 1].set_ylabel('Rapidez de Transiciones')
axes[0, 1].set_title('Estilo Liverpool: Pressing vs Transiciones')

# 3. Boxplot por importancia de partido
importancia_labels = {1: 'Liga', 2: 'Copa', 3: 'Champions'}
df_liverpool['competicion'] = df_liverpool['importancia_partido'].map(importancia_labels)
sns.boxplot(data=df_liverpool, x='competicion', y='factor_liverpool', ax=axes[0, 2])
axes[0, 2].set_title('Factor Liverpool por Competición')

# 4. Correlaciones principales
variables_analisis = ['pressing_intensidad', 'transiciones_rapidas', 'solidez_defensiva', 
                     'creatividad_ataque', 'dominancia_total', 'factor_liverpool']
corr_matrix = df_liverpool[variables_analisis + ['actuacion_memorable']].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='Reds', ax=axes[1, 0])
axes[1, 0].set_title('Matriz de Correlaciones')

# 5. Distribución de dominancia total
axes[1, 1].hist(df_liverpool['dominancia_total'], bins=20, color='#C8102E', alpha=0.7, edgecolor='black')
axes[1, 1].axvline(df_liverpool['dominancia_total'].mean(), color='yellow', linestyle='--', linewidth=2)
axes[1, 1].set_xlabel('Dominancia Total')
axes[1, 1].set_ylabel('Frecuencia')
axes[1, 1].set_title(f'Distribución Dominancia (Media: {df_liverpool["dominancia_total"].mean():.2f})')

# 6. Análisis por fuerza del rival
axes[1, 2].plot(df_liverpool.groupby('rival_fuerza')['actuacion_memorable'].mean(), 
                marker='o', linewidth=3, markersize=8, color='#C8102E')
axes[1, 2].set_xlabel('Fuerza del Rival (1-10)')
axes[1, 2].set_ylabel('% Actuaciones Memorables')
axes[1, 2].set_title('Rendimiento vs Fuerza del Rival')
axes[1, 2].grid(True, alpha=0.3)

# 7. Equilibrio del equipo
equilibrio_bins = pd.cut(df_liverpool['equilibrio_equipo'], bins=4, labels=['Bajo', 'Medio', 'Alto', 'Excelente'])
equilibrio_counts = equilibrio_bins.value_counts()
axes[2, 0].bar(equilibrio_counts.index, equilibrio_counts.values, color=['lightcoral', 'orange', 'gold', '#C8102E'])
axes[2, 0].set_title('Distribución del Equilibrio del Equipo')
axes[2, 0].set_ylabel('Número de Partidos')

# 8. Condición física vs rendimiento
axes[2, 1].scatter(df_liverpool['condicion_fisica'], df_liverpool['dominancia_total'],
                   s=100, alpha=0.6, c=df_liverpool['actuacion_memorable'], cmap='RdYlBu')
axes[2, 1].set_xlabel('Condición Física')
axes[2, 1].set_ylabel('Dominancia Total')
axes[2, 1].set_title('Condición Física vs Dominancia')

# 9. Ambiente Anfield (factor casa)
ambiente_memorable = df_liverpool.groupby(pd.cut(df_liverpool['ambiente_anfield'], bins=5))['actuacion_memorable'].mean()
axes[2, 2].plot(range(len(ambiente_memorable)), ambiente_memorable.values, 
                marker='s', linewidth=3, markersize=10, color='#00B2A9')
axes[2, 2].set_xlabel('Nivel de Ambiente en Anfield')
axes[2, 2].set_ylabel('% Actuaciones Memorables')
axes[2, 2].set_title('Impacto del Ambiente de Anfield')
axes[2, 2].grid(True, alpha=0.3)

plt.suptitle('🔴 LIVERPOOL FC - DASHBOARD DE ANÁLISIS EXPLORATORIO COMPLETO', 
             fontsize=20, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()

# Insights clave del análisis exploratorio
print("=== INSIGHTS CLAVE DEL ANÁLISIS EXPLORATORIO ===")
print(f"1. Correlación pressing-memorables: {df_liverpool['pressing_intensidad'].corr(df_liverpool['actuacion_memorable']):.3f}")
print(f"2. Correlación factor Liverpool-memorables: {df_liverpool['factor_liverpool'].corr(df_liverpool['actuacion_memorable']):.3f}")
print(f"3. Media dominancia en actuaciones memorables: {df_liverpool[df_liverpool['actuacion_memorable']==1]['dominancia_total'].mean():.2f}")
print(f"4. Media dominancia en partidos normales: {df_liverpool[df_liverpool['actuacion_memorable']==0]['dominancia_total'].mean():.2f}")
print(f"5. Impacto ambiente Anfield: {df_liverpool['ambiente_anfield'].corr(df_liverpool['actuacion_memorable']):.3f}")
```

### Criterios de Evaluación
- **Dataset maestro completo e integrado** (15 puntos)
- **Dashboard exploratorio profesional** (10 puntos)

---

## Parte 2: Sistema de Machine Learning Avanzado (25 puntos)

### Objetivo
Desarrollar un sistema completo de machine learning que demuestre el dominio de técnicas del Bloque 3.

### Instrucciones Detalladas

**Paso 4:** Implementa sistema ML completo con feature engineering:

```python
# Sistema de Machine Learning avanzado Liverpool FC

# TU CÓDIGO AQUÍ:
# 1. Aplicar feature engineering avanzado (Semana 14)
# 2. Implementar múltiples algoritmos ML (Semana 12)
# 3. Evaluar con métricas avanzadas (Semana 13)
# 4. Crear pipeline optimizado
# 5. Generar predicciones para próxima temporada

# Feature Engineering avanzado (integrar Semana 14)
print("=== FEATURE ENGINEERING AVANZADO LIVERPOOL ===")

# Crear interacciones específicas del Liverpool
df_liverpool['pressing_x_transiciones'] = df_liverpool['pressing_intensidad'] * df_liverpool['transiciones_rapidas']
df_liverpool['defensa_x_ataque'] = df_liverpool['solidez_defensiva'] * df_liverpool['creatividad_ataque']
df_liverpool['anfield_x_condicion'] = df_liverpool['ambiente_anfield'] * df_liverpool['condicion_fisica']

# Ratios específicos del estilo Liverpool
df_liverpool['ratio_pressing_fisico'] = df_liverpool['pressing_intensidad'] / (df_liverpool['condicion_fisica'] + 1)
df_liverpool['ratio_dominancia_rival'] = df_liverpool['dominancia_total'] / (df_liverpool['rival_fuerza'] + 1)

# Variables categóricas del rendimiento
df_liverpool['categoria_pressing'] = pd.cut(df_liverpool['pressing_intensidad'], 
                                           bins=[0, 6, 8, 10], 
                                           labels=['Bajo', 'Alto', 'Muy_Alto'])

df_liverpool['categoria_equilibrio'] = pd.cut(df_liverpool['equilibrio_equipo'], 
                                             bins=[0, 6, 8, 10], 
                                             labels=['Desbalanceado', 'Equilibrado', 'Muy_Equilibrado'])

# One-hot encoding
df_ml = pd.get_dummies(df_liverpool, columns=['categoria_pressing', 'categoria_equilibrio'], prefix=['press', 'eq'])

print(f"Variables después de FE: {len(df_ml.columns) - 1}")

# Preparar datos para ML
features_ml = [col for col in df_ml.columns if col != 'actuacion_memorable' and df_ml[col].dtype != 'object']
X = df_ml[features_ml]
y = df_ml['actuacion_memorable']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Implementar múltiples algoritmos (integrar Semana 12)
modelos_liverpool = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Regresión Logística': LogisticRegression(random_state=42, max_iter=1000)
}

print("\n=== ENTRENAMIENTO DE MODELOS LIVERPOOL ===")
resultados_ml = {}

for nombre, modelo in modelos_liverpool.items():
    # Entrenar modelo
    modelo.fit(X_train, y_train)
    
    # Predicciones
    y_pred = modelo.predict(X_test)
    y_proba = modelo.predict_proba(X_test)[:, 1] if hasattr(modelo, 'predict_proba') else None
    
    # Métricas (integrar Semana 13)
    accuracy = accuracy_score(y_test, y_pred)
    
    resultados_ml[nombre] = {
        'modelo': modelo,
        'accuracy': accuracy,
        'y_pred': y_pred,
        'y_proba': y_proba
    }
    
    print(f"{nombre}: Accuracy {accuracy:.3f}")

# Selección del mejor modelo
mejor_modelo_nombre = max(resultados_ml.keys(), key=lambda x: resultados_ml[x]['accuracy'])
mejor_modelo = resultados_ml[mejor_modelo_nombre]['modelo']

print(f"\n🏆 MEJOR MODELO: {mejor_modelo_nombre}")
print(f"Accuracy: {resultados_ml[mejor_modelo_nombre]['accuracy']:.3f}")
```

**Paso 5:** Crea sistema de predicciones para próxima temporada:

```python
# Sistema de predicciones para próxima temporada

# TU CÓDIGO AQUÍ:
# 1. Generar escenarios para próxima temporada
# 2. Aplicar modelo entrenado a nuevos escenarios
# 3. Crear recomendaciones estratégicas
# 4. Visualizar predicciones
# 5. Generar alertas y oportunidades

print("=== PREDICCIONES TEMPORADA 2024-25 LIVERPOOL ===")

# Generar escenarios de la próxima temporada
escenarios_proxima = []

# Escenario 1: Partidos importantes Champions League
for i in range(10):
    escenario = {
        'pressing_intensidad': np.random.normal(9.0, 0.5),  # Máximo pressing en Champions
        'transiciones_rapidas': np.random.normal(8.5, 0.8),
        'solidez_defensiva': np.random.normal(8.0, 1.0),
        'creatividad_ataque': np.random.normal(8.8, 0.7),
        'condicion_fisica': np.random.normal(8.5, 0.5),
        'ambiente_anfield': np.random.normal(9.5, 0.3),  # Anfield en Champions
        'rival_fuerza': np.random.randint(8, 11),  # Rivales fuertes
        'importancia_partido': 3,  # Champions League
        'tipo_escenario': 'Champions League'
    }
    escenarios_proxima.append(escenario)

# Escenario 2: Partidos de liga contra equipos medios
for i in range(15):
    escenario = {
        'pressing_intensidad': np.random.normal(8.0, 1.0),
        'transiciones_rapidas': np.random.normal(7.5, 1.0),
        'solidez_defensiva': np.random.normal(7.5, 1.2),
        'creatividad_ataque': np.random.normal(8.0, 1.0),
        'condicion_fisica': np.random.normal(7.8, 1.0),
        'ambiente_anfield': np.random.normal(8.5, 1.0),
        'rival_fuerza': np.random.randint(4, 8),
        'importancia_partido': 1,  # Liga
        'tipo_escenario': 'Liga Regular'
    }
    escenarios_proxima.append(escenario)

# Crear DataFrame de escenarios
df_escenarios = pd.DataFrame(escenarios_proxima)

# Aplicar mismo feature engineering
df_escenarios['dominancia_total'] = (df_escenarios['pressing_intensidad'] + 
                                    df_escenarios['transiciones_rapidas'] + 
                                    df_escenarios['creatividad_ataque']) / 3
df_escenarios['equilibrio_equipo'] = np.minimum(df_escenarios['solidez_defensiva'], 
                                               df_escenarios['creatividad_ataque'])
df_escenarios['factor_liverpool'] = (df_escenarios['pressing_intensidad'] * 
                                   df_escenarios['ambiente_anfield']) / 10

# Interacciones
df_escenarios['pressing_x_transiciones'] = df_escenarios['pressing_intensidad'] * df_escenarios['transiciones_rapidas']
df_escenarios['defensa_x_ataque'] = df_escenarios['solidez_defensiva'] * df_escenarios['creatividad_ataque']
df_escenarios['anfield_x_condicion'] = df_escenarios['ambiente_anfield'] * df_escenarios['condicion_fisica']
df_escenarios['ratio_pressing_fisico'] = df_escenarios['pressing_intensidad'] / (df_escenarios['condicion_fisica'] + 1)
df_escenarios['ratio_dominancia_rival'] = df_escenarios['dominancia_total'] / (df_escenarios['rival_fuerza'] + 1)

# Variables categóricas
df_escenarios['categoria_pressing'] = pd.cut(df_escenarios['pressing_intensidad'], 
                                           bins=[0, 6, 8, 10], 
                                           labels=['Bajo', 'Alto', 'Muy_Alto'])
df_escenarios['categoria_equilibrio'] = pd.cut(df_escenarios['equilibrio_equipo'], 
                                             bins=[0, 6, 8, 10], 
                                             labels=['Desbalanceado', 'Equilibrado', 'Muy_Equilibrado'])

# One-hot encoding
df_escenarios_ml = pd.get_dummies(df_escenarios, columns=['categoria_pressing', 'categoria_equilibrio'], prefix=['press', 'eq'])

# Asegurar que tenga las mismas columnas que el entrenamiento
for col in features_ml:
    if col not in df_escenarios_ml.columns:
        df_escenarios_ml[col] = 0

X_escenarios = df_escenarios_ml[features_ml]

# Hacer predicciones
predicciones = mejor_modelo.predict(X_escenarios)
probabilidades = mejor_modelo.predict_proba(X_escenarios)[:, 1] if hasattr(mejor_modelo, 'predict_proba') else None

df_escenarios['prediccion_memorable'] = predicciones
df_escenarios['probabilidad_memorable'] = probabilidades

print(f"Predicciones para {len(df_escenarios)} escenarios generadas")

# Análisis de predicciones por tipo
print("\n📊 ANÁLISIS DE PREDICCIONES POR ESCENARIO:")
for tipo in df_escenarios['tipo_escenario'].unique():
    subset = df_escenarios[df_escenarios['tipo_escenario'] == tipo]
    prob_media = subset['probabilidad_memorable'].mean()
    actuaciones_predichas = subset['prediccion_memorable'].sum()
    
    print(f"{tipo}:")
    print(f"  Probabilidad media actuación memorable: {prob_media:.1%}")
    print(f"  Actuaciones memorables predichas: {actuaciones_predichas}/{len(subset)}")

# Visualización de predicciones
plt.figure(figsize=(15, 8))

# Subplot 1: Probabilidades por escenario
plt.subplot(2, 2, 1)
for tipo in df_escenarios['tipo_escenario'].unique():
    subset = df_escenarios[df_escenarios['tipo_escenario'] == tipo]
    plt.hist(subset['probabilidad_memorable'], alpha=0.6, label=tipo, bins=10)
plt.xlabel('Probabilidad Actuación Memorable')
plt.ylabel('Frecuencia')
plt.title('Distribución de Probabilidades por Escenario')
plt.legend()

# Subplot 2: Factores clave para Champions
plt.subplot(2, 2, 2)
champions_data = df_escenarios[df_escenarios['tipo_escenario'] == 'Champions League']
plt.scatter(champions_data['factor_liverpool'], champions_data['probabilidad_memorable'], 
           s=100, alpha=0.7, c='red')
plt.xlabel('Factor Liverpool')
plt.ylabel('Probabilidad Memorable')
plt.title('Predicciones Champions League')

# Subplot 3: Comparación por competición
plt.subplot(2, 2, 3)
tipos = df_escenarios['tipo_escenario'].unique()
probabilidades_tipo = [df_escenarios[df_escenarios['tipo_escenario']==tipo]['probabilidad_memorable'].mean() 
                      for tipo in tipos]
plt.bar(tipos, probabilidades_tipo, color=['red', 'blue'], alpha=0.7)
plt.ylabel('Probabilidad Media')
plt.title('Probabilidad por Competición')
plt.xticks(rotation=45)

# Subplot 4: Top factores predictivos
plt.subplot(2, 2, 4)
if hasattr(mejor_modelo, 'feature_importances_'):
    importancias = mejor_modelo.feature_importances_
    indices_top = np.argsort(importancias)[-8:]
    plt.barh(range(len(indices_top)), importancias[indices_top], color='green', alpha=0.7)
    plt.yticks(range(len(indices_top)), [features_ml[i][:15] + '...' if len(features_ml[i]) > 15 else features_ml[i] for i in indices_top])
    plt.xlabel('Importancia')
    plt.title('Top Factores Predictivos')

plt.suptitle('🔴 PREDICCIONES TEMPORADA 2024-25 LIVERPOOL FC', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Criterios de Evaluación
- **Sistema ML completo con feature engineering** (15 puntos)
- **Predicciones realistas para próxima temporada** (10 puntos)

---

## Parte 3: Recomendaciones Estratégicas Basadas en Datos (25 puntos)

### Objetivo
Generar recomendaciones estratégicas profesionales basadas en todos los análisis realizados.

### Instrucciones Detalladas

**Paso 6:** Crea sistema de recomendaciones estratégicas:

```python
# Sistema de recomendaciones estratégicas Liverpool FC

# TU CÓDIGO AQUÍ:
# 1. Analizar patrones de actuaciones memorables
# 2. Identificar factores de éxito específicos del Liverpool
# 3. Generar recomendaciones tácticas
# 4. Crear plan de optimización del rendimiento
# 5. Establecer métricas de seguimiento

print("=" * 70)
print("🔴 LIVERPOOL FC - RECOMENDACIONES ESTRATÉGICAS BASADAS EN DATOS")
print("Sistema de Inteligencia Futbolística Avanzada")
print("=" * 70)

# Análisis de patrones de éxito
actuaciones_memorables = df_liverpool[df_liverpool['actuacion_memorable'] == 1]
actuaciones_normales = df_liverpool[df_liverpool['actuacion_memorable'] == 0]

print("\n📊 ANÁLISIS DE PATRONES DE ÉXITO:")

# Comparación de medias en actuaciones memorables vs normales
variables_clave = ['pressing_intensidad', 'transiciones_rapidas', 'solidez_defensiva', 
                  'creatividad_ataque', 'condicion_fisica', 'ambiente_anfield', 'factor_liverpool']

diferencias_clave = {}
for var in variables_clave:
    media_memorable = actuaciones_memorables[var].mean()
    media_normal = actuaciones_normales[var].mean()
    diferencia = media_memorable - media_normal
    diferencias_clave[var] = diferencia
    
    print(f"{var}:")
    print(f"  Memorable: {media_memorable:.2f}")
    print(f"  Normal: {media_normal:.2f}")
    print(f"  Diferencia: {diferencia:+.2f}")

# Top 3 factores más diferenciantes
top_factores = sorted(diferencias_clave.items(), key=lambda x: abs(x[1]), reverse=True)[:3]

print(f"\n🎯 TOP 3 FACTORES MÁS DIFERENCIANTES:")
for i, (factor, diferencia) in enumerate(top_factores, 1):
    print(f"{i}. {factor}: {diferencia:+.2f}")

# Recomendaciones específicas por factor
print(f"\n⚽ RECOMENDACIONES TÁCTICAS ESPECÍFICAS:")

for factor, diferencia in top_factores:
    if factor == 'pressing_intensidad' and diferencia > 0:
        print(f"🔥 PRESSING: Intensificar presión alta, especialmente en primeros 30 minutos")
        print(f"   • Entrenar pressing coordinado en grupos de 3-4 jugadores")
        print(f"   • Aumentar {diferencia:.1f} puntos en intensidad para partidos clave")
    
    elif factor == 'transiciones_rapidas' and diferencia > 0:
        print(f"⚡ TRANSICIONES: Acelerar transición defensa-ataque")
        print(f"   • Entrenar pases largos precisos desde defensa")
        print(f"   • Mejorar {diferencia:.1f} puntos en velocidad de transición")
    
    elif factor == 'factor_liverpool' and diferencia > 0:
        print(f"🏟️ FACTOR ANFIELD: Maximizar ventaja de casa")
        print(f"   • Aprovechar apoyo de la hinchada en momentos clave")
        print(f"   • Intensificar rituales pre-partido en Anfield")

# Análisis por tipo de rival
print(f"\n🎭 ESTRATEGIAS POR FUERZA DEL RIVAL:")
for fuerza in [1, 5, 9]:
    subset_fuerza = df_liverpool[df_liverpool['rival_fuerza'] == fuerza]
    tasa_exito = subset_fuerza['actuacion_memorable'].mean()
    
    if fuerza <= 3:
        print(f"Rivales Débiles (1-3): Tasa éxito {tasa_exito:.1%}")
        print(f"  • Mantener concentración, evitar relajación")
        print(f"  • Rotar jugadores para mantener frescura")
    elif fuerza <= 6:
        print(f"Rivales Medios (4-6): Tasa éxito {tasa_exito:.1%}")
        print(f"  • Aplicar presión constante desde minuto 1")
        print(f"  • Usar ventaja física y técnica")
    else:
        print(f"Rivales Fuertes (7-10): Tasa éxito {tasa_exito:.1%}")
        print(f"  • Maximizar factor Anfield y ambiente")
        print(f"  • Perfeccionar transiciones rápidas")
```

**Paso 7:** Genera plan de implementación y monitoreo:

```python
# Plan de implementación y sistema de monitoreo

# TU CÓDIGO AQUÍ:
# 1. Crear plan de implementación por fases
# 2. Establecer KPIs y métricas de seguimiento
# 3. Definir alertas tempranas
# 4. Crear protocolo de actualización del modelo
# 5. Generar cronograma de revisiones

print(f"\n🚀 PLAN DE IMPLEMENTACIÓN TEMPORADA 2024-25:")

print(f"\nFASE 1 - PRETEMPORADA (Julio-Agosto):")
print(f"✅ Entrenamientos específicos de pressing coordinado")
print(f"✅ Desarrollo de transiciones rápidas desde defensa")
print(f"✅ Simulacros de ambiente Anfield para jugadores nuevos")
print(f"✅ Calibración inicial del sistema predictivo")

print(f"\nFASE 2 - INICIO TEMPORADA (Septiembre-Octubre):")
print(f"📊 Monitoreo semanal de variables clave")
print(f"🎯 Aplicación de recomendaciones en primeros 10 partidos")
print(f"📈 Evaluación de mejoras en factor Liverpool")
print(f"⚙️ Ajustes tácticos basados en feedback")

print(f"\nFASE 3 - TEMPORADA REGULAR (Noviembre-Abril):")
print(f"🔄 Actualización mensual del modelo predictivo")
print(f"📋 Reportes ejecutivos para cuerpo técnico")
print(f"🎪 Optimización específica para Champions League")
print(f"⚠️ Alertas de degradación del rendimiento")

print(f"\n📊 KPIs DE SEGUIMIENTO DEL SISTEMA:")

# Definir KPIs basados en el análisis
kpis_liverpool = {
    'Actuaciones Memorables': f'Target: >{df_liverpool["actuacion_memorable"].mean():.1%} por mes',
    'Factor Liverpool': f'Target: >{df_liverpool["factor_liverpool"].mean():.1f} en casa',
    'Pressing Intensidad': f'Target: >{df_liverpool["pressing_intensidad"].mean():.1f} vs rivales fuertes',
    'Precisión Modelo': f'Target: >90% accuracy en predicciones',
    'Dominancia Total': f'Target: >{df_liverpool["dominancia_total"].mean():.1f} promedio'
}

for kpi, target in kpis_liverpool.items():
    print(f"• {kpi}: {target}")

print(f"\n⚠️ SISTEMA DE ALERTAS TEMPRANAS:")
print(f"🔴 ALERTA CRÍTICA: Si accuracy del modelo < 85%")
print(f"🟡 ALERTA MEDIA: Si factor Liverpool < {df_liverpool['factor_liverpool'].mean():.1f} por 3 partidos")
print(f"🟢 ALERTA LEVE: Si pressing < {df_liverpool['pressing_intensidad'].mean():.1f} vs rivales top")

print(f"\n🔄 PROTOCOLO DE ACTUALIZACIÓN:")
print(f"• Reentrenamiento automático cada 10 partidos")
print(f"• Revisión de features cada mes")
print(f"• Validación de predicciones semanalmente")
print(f"• Calibración de umbrales trimestralmente")

print(f"\n📅 CRONOGRAMA DE REVISIONES:")
print(f"• Revisión Técnica: Cada lunes post-partido")
print(f"• Reporte Mensual: Primer viernes de cada mes")
print(f"• Evaluación Trimestral: Diciembre, Marzo, Junio")
print(f"• Revisión Anual: Julio (preparación nueva temporada)")

# Generar dashboard final del proyecto
plt.figure(figsize=(20, 12))

# 1. Resumen ejecutivo
plt.subplot(3, 4, 1)
plt.text(0.1, 0.8, '🔴 LIVERPOOL FC', fontsize=20, fontweight='bold', color='red')
plt.text(0.1, 0.6, 'SISTEMA INTEGRAL', fontsize=16, fontweight='bold')
plt.text(0.1, 0.4, f'Precisión: {resultados_ml[mejor_modelo_nombre]["accuracy"]:.1%}', fontsize=14)
plt.text(0.1, 0.2, f'Actuaciones: {df_liverpool["actuacion_memorable"].mean():.1%}', fontsize=14)
plt.axis('off')

# 2. Variables más importantes
plt.subplot(3, 4, 2)
if hasattr(mejor_modelo, 'feature_importances_'):
    top_5_features = np.argsort(mejor_modelo.feature_importances_)[-5:]
    feature_names = [features_ml[i][:12] for i in top_5_features]
    plt.barh(range(5), mejor_modelo.feature_importances_[top_5_features], color='red', alpha=0.7)
    plt.yticks(range(5), feature_names)
    plt.title('Top 5 Variables')

# 3. Predicciones Champions vs Liga
plt.subplot(3, 4, 3)
tipos_comp = df_escenarios['tipo_escenario'].unique()
prob_por_tipo = [df_escenarios[df_escenarios['tipo_escenario']==tipo]['probabilidad_memorable'].mean() 
                for tipo in tipos_comp]
colors = ['red', 'blue']
plt.bar(tipos_comp, prob_por_tipo, color=colors, alpha=0.7)
plt.title('Probabilidad por Competición')
plt.xticks(rotation=45)

# 4. Evolución factor Liverpool
plt.subplot(3, 4, 4)
factor_memorable = df_liverpool[df_liverpool['actuacion_memorable']==1]['factor_liverpool'].mean()
factor_normal = df_liverpool[df_liverpool['actuacion_memorable']==0]['factor_liverpool'].mean()
plt.bar(['Normal', 'Memorable'], [factor_normal, factor_memorable], color=['gray', 'red'], alpha=0.7)
plt.title('Factor Liverpool')
plt.ylabel('Valor Promedio')

# 5-8. Distribuciones de variables clave
variables_dashboard = ['pressing_intensidad', 'transiciones_rapidas', 'creatividad_ataque', 'ambiente_anfield']
for i, var in enumerate(variables_dashboard, 5):
    plt.subplot(3, 4, i)
    plt.hist(df_liverpool[var], bins=15, alpha=0.7, color='red', edgecolor='black')
    plt.title(f'{var.replace("_", " ").title()}')
    plt.axvline(df_liverpool[var].mean(), color='yellow', linestyle='--', linewidth=2)

# 9. Matriz de confusión del mejor modelo
plt.subplot(3, 4, 9)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, resultados_ml[mejor_modelo_nombre]['y_pred'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
           xticklabels=['Normal', 'Memorable'], yticklabels=['Normal', 'Memorable'])
plt.title(f'Matriz Confusión\n{mejor_modelo_nombre}')

# 10. Correlaciones principales
plt.subplot(3, 4, 10)
vars_corr = ['pressing_intensidad', 'factor_liverpool', 'dominancia_total', 'actuacion_memorable']
corr_subset = df_liverpool[vars_corr].corr()
sns.heatmap(corr_subset, annot=True, fmt='.2f', cmap='Reds')
plt.title('Correlaciones Clave')

# 11. Rendimiento por fuerza rival
plt.subplot(3, 4, 11)
rendimiento_rival = df_liverpool.groupby('rival_fuerza')['actuacion_memorable'].mean()
plt.plot(rendimiento_rival.index, rendimiento_rival.values, marker='o', linewidth=3, color='red')
plt.title('Rendimiento vs Fuerza Rival')
plt.xlabel('Fuerza Rival')
plt.ylabel('% Memorable')
plt.grid(True, alpha=0.3)

# 12. Resumen de recomendaciones
plt.subplot(3, 4, 12)
recomendaciones_text = "RECOMENDACIONES:\n\n• Intensificar pressing\n• Acelerar transiciones\n• Maximizar Anfield\n• Monitoreo continuo"
plt.text(0.05, 0.95, recomendaciones_text, fontsize=11, verticalalignment='top', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.7))
plt.axis('off')

plt.suptitle('🔴 LIVERPOOL FC - DASHBOARD PROYECTO FINAL INTEGRADOR', fontsize=24, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
```

### Criterios de Evaluación
- **Recomendaciones estratégicas fundamentadas** (15 puntos)
- **Plan de implementación detallado** (10 puntos)

---

## Parte 4: Presentación Ejecutiva y Reflexión (25 puntos)

### Objetivo
Crear una presentación ejecutiva profesional y reflexionar sobre el aprendizaje del curso completo.

### Instrucciones Detalladas

**Paso 8:** Genera presentación ejecutiva final:

```python
# Presentación ejecutiva final del proyecto

print("=" * 80)
print("🔴 LIVERPOOL FC - PRESENTACIÓN EJECUTIVA FINAL")
print("PROYECTO INTEGRADOR: DATA SCIENCE PARA EL FÚTBOL")
print("=" * 80)

print("\n👨‍💼 RESUMEN EJECUTIVO PARA LA DIRECTIVA:")
print(f"Este proyecto integra 15 semanas de aprendizaje en data science aplicado al fútbol,")
print(f"desarrollando un sistema completo de análisis predictivo para el Liverpool FC.")

print(f"\n📊 RESULTADOS CUANTITATIVOS PRINCIPALES:")
print(f"• Modelo predictivo entrenado con {len(df_liverpool)} partidos históricos")
print(f"• Precisión del sistema: {resultados_ml[mejor_modelo_nombre]['accuracy']:.1%}")
print(f"• {len(features_ml)} variables analizadas tras feature engineering")
print(f"• Predicciones generadas para {len(df_escenarios)} escenarios futuros")
print(f"• Sistema de monitoreo con {len(kpis_liverpool)} KPIs clave")

print(f"\n🎯 FACTORES CLAVE IDENTIFICADOS PARA EL ÉXITO:")
for i, (factor, diferencia) in enumerate(top_factores, 1):
    print(f"{i}. {factor.replace('_', ' ').title()}: Impacto +{diferencia:.2f}")

print(f"\n💰 VALOR COMERCIAL DEL PROYECTO:")
print(f"• Optimización del rendimiento en partidos clave (+15% predicción)")
print(f"• Reducción de riesgos en decisiones tácticas")
print(f"• Maximización del factor casa en Anfield")
print(f"• Sistema escalable para scouting y fichajes")

print(f"\n🚀 IMPLEMENTACIÓN INMEDIATA:")
print(f"• Sistema listo para uso en pretemporada 2024-25")
print(f"• Integración con datos reales del club")
print(f"• Entrenamiento del cuerpo técnico en uso del sistema")
print(f"• Monitoreo automático desde primer partido oficial")

print(f"\n📈 RETORNO DE INVERSIÓN ESPERADO:")
print(f"• Mejora 10-15% en preparación de partidos importantes")
print(f"• Reducción 20% en decisiones tácticas subóptimas")
print(f"• Aumento 5-10% en rendimiento en casa (Anfield)")
print(f"• ROI estimado: 300-500% en primera temporada")
```

**Paso 9:** Reflexión personal sobre el aprendizaje:

```python
# Reflexión personal sobre el curso completo

print(f"\n" + "="*60)
print("REFLEXIÓN PERSONAL: MI VIAJE EN DATA SCIENCE")
print("="*60)

print(f"\n🎓 HABILIDADES DESARROLLADAS EN EL CURSO:")

print(f"\nBLOQUE 1 - FUNDAMENTOS DE PROGRAMACIÓN:")
print(f"✅ Programación en Python desde cero")
print(f"✅ Estructuras de datos (listas, diccionarios)")
print(f"✅ Control de flujo (bucles, condicionales)")
print(f"✅ Funciones y modularización")
print(f"✅ Introducción a pandas y numpy")
print(f"✅ Visualización básica con matplotlib")

print(f"\nBLOQUE 2 - ANÁLISIS DE DATOS:")
print(f"✅ Exploración y limpieza de datos")
print(f"✅ Estadística descriptiva aplicada")
print(f"✅ Visualización avanzada con seaborn")
print(f"✅ Análisis de correlaciones y patrones")
print(f"✅ Interpretación de datos deportivos")

print(f"\nBLOQUE 3 - MACHINE LEARNING:")
print(f"✅ Introducción a algoritmos de ML")
print(f"✅ Modelos de clasificación y predicción")
print(f"✅ Evaluación de modelos con métricas avanzadas")
print(f"✅ Feature engineering y optimización")
print(f"✅ Pipelines de ML y sistemas completos")

print(f"\n💡 CONCEPTOS MÁS IMPORTANTES APRENDIDOS:")
print(f"1. Los datos cuentan historias, pero hay que saber interpretarlas")
print(f"2. La programación es una herramienta para resolver problemas reales")
print(f"3. El machine learning no es magia, es matemática aplicada")
print(f"4. La visualización es clave para comunicar insights")
print(f"5. El contexto deportivo hace el aprendizaje más interesante")

print(f"\n🏆 LOGROS PERSONALES MÁS SIGNIFICATIVOS:")
print(f"• Crear mi primer modelo predictivo funcional")
print(f"• Entender cómo se toman decisiones basadas en datos")
print(f"• Desarrollar un proyecto completo desde cero")
print(f"• Aplicar conceptos técnicos a mi pasión por el fútbol")
print(f"• Sentirme capaz de seguir aprendiendo data science")

print(f"\n🚀 APLICACIONES FUTURAS:")
print(f"• Análisis de datos en mi carrera profesional")
print(f"• Proyectos personales de análisis deportivo")
print(f"• Comprensión mejor de estadísticas en el deporte")
print(f"• Base sólida para cursos avanzados de data science")
print(f"• Pensamiento analítico en decisiones cotidianas")

print(f"\n🙏 AGRADECIMIENTOS:")
print(f"• Al curso por hacer accesible la data science")
print(f"• Al contexto futbolístico que mantuvo mi interés")
print(f"• A la metodología práctica que facilitó el aprendizaje")
print(f"• A los ejercicios progresivos que construyeron confianza")

print(f"\n📚 PRÓXIMOS PASOS EN MI APRENDIZAJE:")
print(f"1. Profundizar en machine learning avanzado")
print(f"2. Aprender más sobre análisis de datos deportivos")
print(f"3. Explorar visualización interactiva")
print(f"4. Desarrollar proyectos propios")
print(f"5. Considerar carrera en data science o analytics")

# Generar certificado simbólico del proyecto
print(f"\n" + "="*70)
print("🏆 CERTIFICADO DE FINALIZACIÓN - PROYECTO INTEGRADOR")
print("="*70)
print(f"Este proyecto demuestra competencia en:")
print(f"✓ Programación en Python")
print(f"✓ Análisis exploratorio de datos")
print(f"✓ Machine learning aplicado")
print(f"✓ Visualización de datos")
print(f"✓ Pensamiento analítico")
print(f"✓ Comunicación de resultados")
print(f"\nPROYECTO: Sistema de Análisis Predictivo Liverpool FC")
print(f"NIVEL: Integrador Avanzado")
print(f"FECHA: Semana 15 - Curso Data Science con Fútbol")
print("="*70)

print(f"\n🎉 ¡FELICITACIONES POR COMPLETAR EL CURSO!")
print(f"Has desarrollado habilidades valiosas que te acompañarán")
print(f"en tu futuro académico y profesional. ¡Sigue aprendiendo!")
```

### Criterios de Evaluación
- **Presentación ejecutiva profesional** (15 puntos)
- **Reflexión personal profunda y fundamentada** (10 puntos)

## Criterios de Evaluación General

### Integración de Conocimientos (40 puntos)
- Aplicación correcta de conceptos de los 3 bloques del curso
- Coherencia entre análisis exploratorio, ML y recomendaciones
- Demostración de progresión desde fundamentos hasta aplicación avanzada
- Uso apropiado de todas las herramientas aprendidas

### Calidad Técnica (30 puntos)
- Implementación correcta de sistemas de ML completos
- Feature engineering apropiado y justificado
- Evaluación rigurosa con múltiples métricas
- Código bien estructurado y documentado

### Aplicación Práctica (30 puntos)
- Recomendaciones estratégicas realistas y útiles
- Interpretación correcta de resultados en contexto futbolístico
- Plan de implementación detallado y factible
- Reflexión personal madura sobre el aprendizaje

## Instrucciones de Entrega

1. **Completa todas las 4 partes** del proyecto integrador
2. **Incluye código funcional** que demuestre todos los conceptos
3. **Verifica que todas las visualizaciones** se generen correctamente
4. **Guarda como:** `[matricula]-proyecto-final-liverpool.ipynb`
5. **Entrega antes del final de Semana 15**

## Recursos de Apoyo

- Todos los notebooks de las 15 semanas del curso
- Documentación completa de pandas, scikit-learn, matplotlib
- Ejemplos de proyectos integradores en data science

---

**¡Completa tu viaje en data science y demuestra todo lo que has aprendido con este proyecto final del Liverpool FC!** 🔴⚽📊🎉
    'posesion_local', 'tiros_local', 'tiros_puerta_local',
    'faltas_local', 'tarjetas_amarillas_local', 'tarjetas_rojas_local',
    'corners_local', 'fueras_juego_local',
    'racha_victorias_local_5', 'forma_reciente_local',
    'dias_descanso_local', 'historial_vs_rival',
    'importancia_partido', 'es_derby', 'clima'
]
```

**1.2 Análisis Exploratorio Completo**

- **Análisis temporal:** Tendencias por temporada, mes, jornada
- **Análisis de equipos:** Rendimiento en casa vs fuera, contra diferentes tipos de rivales
- **Análisis de contexto:** Impacto de variables contextuales en el rendimiento
- **Detección de patrones:** Identificación de insights no obvios

**1.3 Dashboard Ejecutivo Interactivo**

```python
# Crea visualizaciones que respondan preguntas clave:
# - ¿Cuáles son nuestras fortalezas y debilidades?
# - ¿Contra qué tipo de equipos tenemos mejor rendimiento?
# - ¿Cómo afectan los factores externos a nuestro juego?
# - ¿Qué patrones podemos explotar estratégicamente?
```

### Criterios de Evaluación Parte 1

- **Completitud de datos (25%):** Dataset robusto y realista
- **Profundidad de análisis (50%):** Insights valiosos y no obvios
- **Calidad de visualizaciones (25%):** Gráficos claros y profesionales

---

## Proyecto Parte 2: Sistema Predictivo Avanzado (2.5 horas)

### Contexto

Desarrolla el sistema de predicción más avanzado posible utilizando todas las técnicas aprendidas en el curso.

### Entregables Requeridos

**2.1 Múltiples Modelos Predictivos**

Implementa al menos 5 modelos diferentes:

- **Regresión Logística:** Baseline interpretable
- **Random Forest:** Modelo robusto principal
- **Gradient Boosting:** Modelo de alta precisión
- **SVM:** Modelo alternativo
- **Ensemble personalizado:** Combinación optimizada

**2.2 Feature Engineering Avanzado**

```python
class AdvancedFootballFeatures(BaseEstimator, TransformerMixin):
    """
    Feature engineering completo para predicción futbolística
    """
    def __init__(self):
        self.temporal_features = True
        self.contextual_features = True
        self.interaction_features = True
    
    def fit(self, X, y=None):
        # Aprende parámetros de los datos de entrenamiento
        return self
    
    def transform(self, X):
        # Aplica todas las transformaciones
        return X_transformed
```

Incluye al menos:

- 10 variables temporales (rachas, tendencias, forma)
- 8 variables contextuales (rivalidades, importancia, historial)
- 5 variables de interacción (combinaciones de variables existentes)
- Variables derivadas específicas de tu análisis exploratorio

**2.3 Pipeline de Producción**

```python
# Pipeline completo optimizado
pipeline_final = Pipeline([
    ('feature_engineering', AdvancedFootballFeatures()),
    ('imputation', SimpleImputer(strategy='median')),
    ('scaling', StandardScaler()),
    ('feature_selection', SelectKBest(k=20)),
    ('modelo', ensemble_optimizado)
])
```

**2.4 Validación Exhaustiva**

- Validación cruzada temporal (respetando orden cronológico)
- Validación por temporadas (entrenar en 2 temporadas, validar en 1)
- Análisis de estabilidad del modelo
- Intervalos de confianza para métricas principales

### Criterios de Evaluación Parte 2

- **Innovación técnica (30%):** Feature engineering creativo y efectivo
- **Rendimiento predictivo (40%):** Mejoras cuantificables significativas
- **Robustez metodológica (30%):** Validación apropiada y pipeline sólido

---

## Proyecto Parte 3: Aplicaciones Prácticas (1.5 horas)

### Contexto

Demuestra cómo tu sistema puede resolver problemas reales de un equipo de fútbol profesional.

### Entregables Requeridos

**3.1 Sistema de Recomendación de Estrategia**

```python
def recomendar_estrategia(equipo_local, equipo_visitante, contexto):
    """
    Recomienda estrategia basada en predicciones y análisis
    """
    # Análisis de probabilidades de victoria
    # Identificación de factores clave para este partido específico
    # Recomendaciones tácticas basadas en data
    return recomendaciones
```

**3.2 Análisis de Escenarios "What-If"**

- **Escenario 1:** ¿Cómo cambiarían las probabilidades con más días de descanso?
- **Escenario 2:** ¿Qué impacto tendría una racha de 3 victorias?
- **Escenario 3:** ¿Cómo afecta jugar en diferentes contextos?

**3.3 Sistema de Monitoreo de Rendimiento**

- Dashboard para seguimiento de predicciones vs resultados reales
- Identificación automática de cuándo reentrenar el modelo
- Alertas de degradación en precisión

**3.4 Reporte de Scouting Basado en Datos**

```python
def analizar_oponente(equipo_rival, ultimos_n_partidos=10):
    """
    Genera reporte completo de scouting de rival
    """
    # Análisis de fortalezas y debilidades
    # Patrones tácticos identificados
    # Recomendaciones específicas para enfrentar este rival
    return reporte_scouting
```

### Criterios de Evaluación Parte 3

- **Relevancia práctica (40%):** Aplicaciones útiles para equipos reales
- **Creatividad (30%):** Soluciones innovadoras a problemas deportivos
- **Implementación técnica (30%):** Código funcional y bien estructurado

---

## Proyecto Parte 4: Presentación Profesional (1 hora)

### Contexto

Como científico de datos senior, debes comunicar tus resultados a audiencias técnicas y no técnicas.

### Entregables Requeridos

**4.1 Reporte Ejecutivo (2 páginas máximo)**

- **Resumen ejecutivo:** Principales logros y capacidades del sistema
- **Métricas de rendimiento:** Mejoras cuantificadas vs métodos básicos
- **Aplicaciones prácticas:** Cómo el club puede usar el sistema
- **ROI estimado:** Valor económico potencial para el club

**4.2 Documentación Técnica**

- **Arquitectura del sistema:** Diagrama de componentes principales
- **Guía de uso:** Cómo operar el sistema día a día
- **Limitaciones conocidas:** Qué no puede hacer el sistema
- **Hoja de ruta:** Próximas mejoras sugeridas

**4.3 Presentación de 10 minutos**

Crea una presentación que cubra:

- Problema abordado y metodología
- Principales insights del análisis exploratorio
- Rendimiento del sistema predictivo
- Demostración de aplicaciones prácticas
- Conclusiones y siguientes pasos

### Criterios de Evaluación Parte 4

- **Claridad comunicativa (40%):** Explicaciones comprensibles para no técnicos
- **Organización profesional (30%):** Estructura lógica y presentación pulida
- **Completitud (30%):** Cobertura adecuada de todos los aspectos del proyecto

---

## Proyecto Parte 5: Reflexión y Autoevaluación (30 minutos)

### Contexto

Reflexiona sobre tu aprendizaje a lo largo de todo el curso y el desarrollo de este proyecto.

### Entregables Requeridos

**5.1 Ensayo de Reflexión (500-750 palabras)**

Aborda las siguientes preguntas:

- ¿Qué conceptos fueron más desafiantes y cómo los superaste?
- ¿Cómo cambió tu perspectiva sobre el análisis de datos durante el curso?
- ¿Qué aspectos del proyecto final te resultaron más satisfactorios?
- ¿Qué aplicaciones adicionales puedes imaginar para estas habilidades?

**5.2 Autoevaluación de Competencias**

Evalúa tu nivel (1-5) en cada área:

- **Programación en Python:** Estructuras de datos, funciones, librerías
- **Análisis exploratorio:** Pandas, visualización, detección de patrones
- **Machine Learning:** Modelos, evaluación, optimización
- **Feature Engineering:** Creación de variables, selección, pipelines
- **Comunicación:** Visualización, reportes, presentaciones

**5.3 Plan de Desarrollo Futuro**

- ¿Qué temas te gustaría profundizar?
- ¿Qué proyectos personales planeas desarrollar?
- ¿Cómo aplicarás estas habilidades en tu contexto personal/profesional?

### Criterios de Evaluación Parte 5

- **Profundidad de reflexión (50%):** Análisis introspectivo significativo
- **Honestidad en autoevaluación (25%):** Evaluación realista de competencias
- **Planificación futura (25%):** Planes concretos y realistas

---

## Criterios de Evaluación General del Proyecto

### Excelencia Técnica (40%)

- **Implementación correcta:** Todo el código funciona sin errores
- **Metodología apropiada:** Uso correcto de técnicas de data science
- **Innovación:** Enfoques creativos y mejoras significativas

### Aplicación Práctica (35%)

- **Relevancia deportiva:** Soluciones útiles para problemas reales
- **Insights valiosos:** Descubrimientos no obvios y accionables
- **Usabilidad:** Sistema que podría usarse en contexto profesional

### Comunicación Profesional (25%)

- **Claridad:** Explicaciones comprensibles para diferentes audiencias
- **Completitud:** Cobertura adecuada de todos los aspectos
- **Presentación:** Organización profesional y pulida

## Recursos Adicionales

### Datos Externos Opcionales

- **APIs de fútbol:** Para datos reales (API-Football, FootballData)
- **Datos climáticos:** Para variables contextuales adicionales
- **Datos de mercado:** Para análisis de valor de jugadores

### Herramientas Avanzadas Opcionales

```python
# Librerías adicionales que puedes explorar
import plotly.express as px  # Visualizaciones interactivas
import streamlit as st  # Aplicación web simple
import shap  # Explicabilidad de modelos
import optuna  # Optimización avanzada de hiperparámetros
```

## Entrega Final

### Componentes Requeridos

1. **Jupyter Notebook principal** (`apellido_nombre_proyecto_final.ipynb`)
2. **Pipeline guardado** (`modelo_final.pkl`)
3. **Reporte ejecutivo** (`reporte_ejecutivo.pdf`)
4. **Presentación** (`presentacion_final.pdf` o `.pptx`)
5. **Documentación técnica** (`documentacion_tecnica.md`)
6. **Ensayo de reflexión** (`reflexion_personal.pdf`)

### Formato de Entrega

- **Carpeta comprimida:** `apellido_nombre_proyecto_final.zip`
- **Fecha límite:** [Definir según cronograma]
- **Plataforma:** [Especificar LMS o sistema de entrega]
- **Presentación oral:** [Definir si aplica]

---

## ¡Felicitaciones por Completar el Curso!

Has recorrido un camino increíble desde los fundamentos de programación hasta el desarrollo de sistemas predictivos avanzados. Este proyecto final demuestra que ahora posees habilidades valiosas en data science aplicada al deporte.

**¿Qué sigue después?**

- Continúa practicando con proyectos personales
- Explora especializaciones (deep learning, análisis de video, etc.)
- Busca oportunidades para aplicar estas habilidades profesionalmente
- Comparte tu conocimiento con otros apasionados del deporte y los datos

**Tiempo total estimado:** 6-8 horas  
**Dificultad:** ⭐⭐⭐⭐⭐ (Proyecto Capstone)  
**Prerrequisitos:** Completar todo el curso (Bloques 1-3)  
**Nivel alcanzado:** ¡Data Scientist Junior en Deportes! 🏆
