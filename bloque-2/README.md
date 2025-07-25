# Bloque 2: Explorando Datos Deportivos con Python

## Objetivos del Bloque

Al finalizar este bloque, los estudiantes serán capaces de:

1. **Explorar y analizar** datos deportivos reales usando Python y pandas
2. **Aplicar estadística descriptiva** para descubrir patrones en datos de fútbol
3. **Crear visualizaciones efectivas** usando seaborn y matplotlib
4. **Interpretar resultados** y generar insights sobre rendimiento deportivo
5. **Desarrollar** un análisis completo de datos futbolísticos de manera profesional
6. **Comunicar hallazgos** de forma clara y visual
7. **Manejar datasets reales** con sus desafíos de limpieza y preparación

## Contenido por Semana

### Semana 1: Introducción y Exploración de Datos

- **Notebook:** `introduccion-exploracion.ipynb`
- **Teoría:** ¿Qué son los datos deportivos? Introducción a la ciencia de datos en el fútbol
- **Práctica:** Primeros pasos con pandas y seaborn en contexto deportivo
- **Ejercicios:** Exploración básica de datasets de fútbol, lectura de archivos CSV
- **Aplicación:** Análisis inicial de datos de partidos y estadísticas básicas

### Semana 2: Tipos de Datos en Fútbol

- **Notebook:** `tipos-datos-futbol.ipynb`
- **Teoría:** Clasificación de datos deportivos: numéricos, categóricos, temporales
- **Práctica:** Identificación y manejo de diferentes tipos de datos futbolísticos
- **Ejercicios:** Limpieza y preparación de datos de jugadores y equipos
- **Aplicación:** Análisis de datos de rendimiento y características de jugadores

### Semana 3: Estadística Descriptiva Aplicada

- **Notebook:** `estadistica-descriptiva.ipynb`
- **Teoría:** Medidas de tendencia central y dispersión en el contexto deportivo
- **Práctica:** Cálculo de estadísticas de goles, rendimiento y comparaciones
- **Ejercicios:** Análisis estadístico de temporadas y competiciones
- **Aplicación:** Evaluación del rendimiento de equipos y jugadores

### Semana 4: Visualización de Datos Deportivos

- **Notebook:** `visualizacion-datos.ipynb`
- **Teoría:** Principios de visualización efectiva para datos deportivos
- **Práctica:** Creación de gráficos comparativos y análisis visual
- **Ejercicios:** Gráficos de tendencias, comparaciones locales vs visitantes
- **Aplicación:** Dashboard básico de análisis futbolístico

### Semana 5: Análisis e Interpretación de Resultados

- **Notebook:** `analisis-interpretacion.ipynb`
- **Teoría:** Interpretación profesional de análisis descriptivos
- **Práctica:** Síntesis de hallazgos y generación de insights
- **Ejercicios:** Comunicación de resultados y recomendaciones
- **Aplicación:** Reporte final de análisis deportivo

## Materiales Incluidos

- **Notebooks interactivos:** Un notebook completo por semana con ejercicios integrados
- **Ejemplos deportivos reales:** Análisis de datos de FIFA, Champions League y ligas
- **Datasets deportivos:** Conjuntos de datos de jugadores, equipos y partidos
- **Código reutilizable:** Funciones y ejemplos para análisis deportivo
- **Proyecto integrado:** Evaluación progresiva con dataset FIFA 22

## Estructura de Carpetas

```
bloque-2/
├── semana-1/
│   └── introduccion-exploracion.ipynb
├── semana-2/
│   └── tipos-datos-futbol.ipynb
├── semana-3/
│   └── estadistica-descriptiva.ipynb
├── semana-4/
│   └── visualizacion-datos.ipynb
├── semana-5/
│   └── analisis-interpretacion.ipynb
├── evaluacion/
│   └── README.md (proyecto FIFA 22)
└── README.md
```

## Evaluación

La evaluación del Bloque 2 consiste en un **proyecto integrado** que se desarrolla progresivamente durante las 5 semanas del bloque:

### Proyecto: "Análisis Completo de Jugadores FIFA 22"

**Dataset:** [FIFA 22 Complete Player Dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

**Descripción:** Análisis profesional de más de 19,000 jugadores de FIFA 22, incluyendo estadísticas de rendimiento, datos económicos y atributos técnicos.

**Estructura del Proyecto:**

- **Semana 1:** Exploración inicial del dataset (20%)
- **Semana 2:** Análisis de tipos de datos y limpieza (20%)
- **Semana 3:** Estadísticas descriptivas por posición y liga (20%)
- **Semana 4:** Visualizaciones comparativas de rendimiento (20%)
- **Semana 5:** Interpretación de resultados y conclusiones (20%)

**Entrega Final:** Un notebook Jupyter consolidado que integre todos los análisis semanales, con conclusiones profesionales sobre el mercado de jugadores y recomendaciones estratégicas para equipos.

### Habilidades Evaluadas

✅ **Exploración de Datos:**
- Carga y comprensión de datasets complejos
- Identificación de variables clave
- Detección de patrones y anomalías

✅ **Análisis Estadístico:**
- Cálculo de estadísticas descriptivas
- Comparaciones entre grupos (posiciones, ligas)
- Interpretación de medidas de tendencia central y dispersión

✅ **Visualización:**
- Creación de gráficos efectivos con seaborn
- Personalización de visualizaciones
- Comunicación visual de hallazgos

✅ **Interpretación y Comunicación:**
- Generación de insights deportivos
- Redacción de conclusiones profesionales
- Formulación de recomendaciones basadas en datos

## Prerequisitos

**Conocimientos del Bloque 1:**
- Fundamentos de programación en Python
- Manejo básico de pandas y matplotlib
- Uso de Jupyter Notebook
- Estructuras de datos básicas (listas, diccionarios)

**Habilidades Requeridas:**
- Cálculos matemáticos básicos (promedios, porcentajes)
- Interpretación de gráficos simples
- Pensamiento analítico aplicado al deporte
- Curiosidad por descubrir patrones en datos deportivos

## Herramientas Principales

### Librerías de Python
```python
# Análisis de datos
import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Utilidades
import warnings
warnings.filterwarnings('ignore')
```

### Datasets Utilizados
- **FIFA 22 Player Dataset:** Análisis completo de jugadores
- **Champions League Data:** Datos históricos de partidos
- **League Statistics:** Comparaciones entre ligas europeas

## Transición al Bloque 3

Una vez completado exitosamente el Bloque 2, los estudiantes estarán preparados para:

- **Bloque 3:** Machine Learning aplicado al fútbol
- **Modelos predictivos:** Predicción de resultados y rendimiento
- **Análisis avanzado:** Clustering de jugadores y equipos
- **Optimización:** Estrategias basadas en datos para mejorar rendimiento

## Notas Importantes

💡 **Enfoque Práctico:** Este bloque se centra en aplicaciones reales con datos deportivos auténticos.

📊 **Visualización:** Se enfatiza la creación de gráficos claros y profesionales.

⚽ **Contexto Deportivo:** Todos los ejercicios están diseñados con ejemplos futbolísticos relevantes.

🎯 **Meta:** Al final del Bloque 2, deberías poder realizar un análisis completo de cualquier dataset deportivo y comunicar tus hallazgos de manera profesional.

---

**¡Descubre los secretos ocultos en los datos del fútbol!** 📈⚽

*Este bloque te convertirá en un analista de datos deportivos capaz de encontrar insights valiosos que pueden cambiar estrategias de equipos.*
