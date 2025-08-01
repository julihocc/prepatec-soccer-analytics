# Ejercicio Semanal - Semana 14: Mejorando Mis Predicciones

**Curso:** Introducción a Data Science con Fútbol  
**Bloque:** 3 - Mi Primera Predicción con Datos de Fútbol  
**Semana:** 14 - Feature Engineering y Optimización  
**Tiempo estimado:** 4-5 horas  
**Tipo:** Individual  

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

1. **Crear** nuevas variables (features) más predictivas a partir de datos existentes
2. **Aplicar** técnicas de feature engineering específicas para datos deportivos
3. **Optimizar** modelos mediante selección automática de variables
4. **Implementar** pipelines de procesamiento de datos
5. **Mejorar** significativamente el rendimiento de modelos predictivos

## Contexto del Problema

Hasta ahora hemos usado variables básicas como goles, posesión, etc. Pero los analistas deportivos profesionales crean variables más sofisticadas: rachas de victorias, rendimiento contra equipos similares, fatiga acumulada, etc. El arte del feature engineering es transformar datos crudos en información más valiosa para la predicción.

**Pregunta central:** *¿Puedo crear variables más inteligentes que mejoren significativamente mis predicciones?*

---

## Ejercicio 1: Feature Engineering Básico - Variables Temporales (1.5 horas)

### Contexto

Los datos deportivos tienen una dimensión temporal crucial. El rendimiento reciente importa más que el rendimiento de hace 6 meses. Las rachas y tendencias son fundamentales.

### Tareas

**1.1 Configuración y datos históricos expandidos**

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="viridis")
```

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
