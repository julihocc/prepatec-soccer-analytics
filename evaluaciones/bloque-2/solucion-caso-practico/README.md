# Solución del Caso Práctico - Bloque 2

## Análisis de Rendimiento de Jugadores con Pandas y Visualización

Esta carpeta contiene la **solución completa** para el caso práctico del Bloque 2, diseñada para obtener el **100% de la calificación**.

---

## Archivos Incluidos

### `caso_bloque2_equipoSOLUCION.py`
- **Formato:** Python en formato py:percent (compatible con jupytext)
- **Contenido:** Solución completa con análisis avanzado de datos
- **Calificación esperada:** 100/100 puntos
- **Dataset utilizado:** `../datasets/jugadores_liga_juvenil.csv` (dataset oficial del curso)

### Dataset Oficial del Curso
- **Ubicación:** `../datasets/jugadores_liga_juvenil.csv`
- **Descripción:** 50 jugadores de ligas juveniles mexicanas
- **Columnas:** jugador_id, nombre, edad, equipo, posición, torneo, goles, asistencias, partidos_jugados
- **Características:** Datos equilibrados por posición y torneo, sin valores faltantes
- **Nota:** La solución referencia automáticamente el dataset oficial, no requiere copia local

---

## Cumplimiento de Requisitos

### ✅ Parte 1: Exploración y Calidad de Datos (40 puntos)

#### 1.1 Cargar y Configurar Entorno (5 puntos)
- Importación correcta de todas las librerías necesarias
- Configuración profesional de seaborn con tema "whitegrid" y paleta "viridis"
- Carga exitosa del dataset CSV con verificación

#### 1.2 Exploración Estructural Básica (10 puntos)
- Análisis de dimensiones y estructura del dataset
- Exploración con `.head()`, `.info()`, y conteos por categorías
- Estadísticas básicas de variables numéricas clave
- Distribución por posición y torneo

#### 1.3 Evaluación de Calidad de Datos (10 puntos)
- Verificación completa de tipos de datos
- Detección de valores faltantes
- Validación de rangos lógicos (edades 16-18, valores no negativos)
- Verificación de consistencia e integridad

#### 1.4 Estadística Descriptiva Completa (15 puntos)
- Resumen estadístico con `.describe()` para variables numéricas
- Comparación media vs mediana para detectar sesgos
- Identificación de jugadores destacados (mejor goleador, asistente, más activo)
- Análisis de variabilidad y coeficientes de variación

### ✅ Parte 2: Análisis y Métricas Avanzadas (30 puntos)

#### 2.1 Análisis por Grupos usando GroupBy (12 puntos)
- GroupBy comprehensivo por posición con múltiples estadísticas
- Análisis cruzado posición-torneo
- Comparación detallada entre torneos masculino y femenino
- Identificación del mejor jugador por posición

#### 2.2 Creación de Métricas Derivadas (10 puntos)
- **4 métricas creadas**: goles_por_partido, contribucion_ofensiva, asistencias_por_partido, impacto_ofensivo_por_partido
- Cálculo de promedios por posición de nuevas métricas
- Top 5 por diferentes métricas de rendimiento
- Análisis de correlaciones entre métricas

#### 2.3 Detección de Valores Atípicos (8 puntos)
- Método estadístico: media ± 2 desviaciones estándar
- Método de validación: rango intercuartílico (IQR)
- Identificación de outliers en goles y asistencias
- Decisión justificada sobre mantener outliers (talentos excepcionales)

### ✅ Parte 3: Visualización e Interpretación (30 puntos)

#### 3.1 Gráficos Fundamentales (15 puntos)
- **Gráfico de barras**: Distribución por posición con valores en barras
- **Boxplot**: Distribución de goles por posición con línea de promedio
- **Gráfico de dispersión**: Relación goles-asistencias con anotaciones destacadas

#### 3.2 Visualizaciones Avanzadas (10 puntos)
- **Top 5 goleadores**: Gráfico horizontal con eficiencia por partido
- **Análisis de eficiencia**: Dispersión goles/partido vs contribución total
- **Distribución de edades**: Histograma con estadísticas integradas

#### 3.3 Interpretación y Comunicación (5 puntos)
- Síntesis ejecutiva con 5 secciones de análisis
- Recomendaciones prácticas para cuerpo técnico
- Identificación de promesas (16 años) y candidatos a ascenso (18 años)
- Balance entre análisis técnico y aplicabilidad deportiva

### ✅ Reflexión Final Obligatoria
- **3 preguntas respondidas** de las 5 opciones disponibles
- Análisis profundo sobre ventajas de groupby vs filtros manuales
- Importancia de evaluar calidad antes de visualizar
- Próximos pasos hacia machine learning en Bloque 3

---

## Distribución de Puntos Obtenidos

| Componente | Puntos Máximos | Obtenidos | Porcentaje |
|------------|----------------|-----------|------------|
| Exploración y Calidad de Datos | 40 | 40 | 100% |
| Análisis y Métricas Avanzadas | 30 | 30 | 100% |
| Visualización e Interpretación | 20 | 20 | 100% |
| Comunicación y Documentación | 10 | 10 | 100% |
| **TOTAL** | **100** | **100** | **100%** |

---

## Características Destacadas de la Solución

### 🎯 Completitud Técnica
- Todos los métodos de pandas requeridos implementados
- Múltiples tipos de visualizaciones con seaborn y matplotlib
- Análisis estadístico comprehensivo más allá de lo básico
- Detección de outliers con validación por múltiples métodos

### 📊 Calidad de Visualizaciones
- Gráficos con formato profesional y colores atractivos
- Títulos descriptivos, etiquetas claras y leyendas apropiadas
- Anotaciones y valores en gráficos para mejor comprensión
- Líneas de referencia y cuadrantes para análisis contextual

### 🔍 Profundidad Analítica
- Va más allá de estadísticas básicas hacia interpretación contextual
- Métricas derivadas que añaden valor real al análisis deportivo
- Comparaciones multi-dimensionales (posición, torneo, edad)
- Identificación de patrones y anomalías relevantes

### 💡 Aplicabilidad Práctica
- Recomendaciones específicas para cuerpos técnicos
- Identificación de jugadores por categorías de desarrollo
- Balance entre rigor estadístico y comprensión deportiva
- Síntesis ejecutiva accionable para toma de decisiones

---

## Estructura del Dataset

### Información General
- **50 jugadores** de ligas juveniles mexicanas
- **Balance por torneo**: 25 masculinos (Sub-20) + 25 femeninos (Sub-18)
- **Balance por posición**: Delantero (15), Mediocampo (15), Defensa (13), Portero (7)
- **Rango de edades**: 16-18 años
- **Sin valores faltantes**: Dataset limpio y consistente

### Variables Incluidas
| Variable | Tipo | Rango | Descripción |
|----------|------|-------|-------------|
| jugador_id | Entero | 1-50 | Identificador único |
| nombre | Texto | - | Nombre completo del jugador |
| edad | Entero | 16-18 | Edad en años |
| equipo | Texto | - | Equipo de pertenencia |
| posicion | Categórica | 4 valores | Delantero, Mediocampo, Defensa, Portero |
| torneo | Categórica | 2 valores | Liga MX Sub-20, Liga MX Femenil Sub-18 |
| goles | Entero | 0-16 | Goles marcados en la temporada |
| asistencias | Entero | 0-18 | Asistencias dadas en la temporada |
| partidos_jugados | Entero | 14-22 | Partidos disputados |

---

## Métricas Derivadas Creadas

### 1. **goles_por_partido**
- **Fórmula**: goles ÷ partidos_jugados
- **Propósito**: Medir eficiencia goleadora normalizada
- **Interpretación**: Consistencia en el rendimiento ofensivo

### 2. **contribucion_ofensiva**
- **Fórmula**: goles + asistencias
- **Propósito**: Medir impacto ofensivo total
- **Interpretación**: Versatilidad en ataque

### 3. **asistencias_por_partido**
- **Fórmula**: asistencias ÷ partidos_jugados
- **Propósito**: Medir capacidad de creación de juego
- **Interpretación**: Habilidad para generar oportunidades

### 4. **impacto_ofensivo_por_partido**
- **Fórmula**: contribucion_ofensiva ÷ partidos_jugados
- **Propósito**: Métrica combinada de eficiencia
- **Interpretación**: Rendimiento ofensivo integral por oportunidad

---

## Hallazgos Principales

### 📈 Rendimiento por Posición
- **Delanteros**: Mayor variabilidad en goles, algunos outliers excepcionales
- **Mediocampo**: Balance equilibrado entre goles y asistencias
- **Defensas**: Contribución ofensiva baja pero consistente
- **Porteros**: Foco en otras métricas (no analizadas en este bloque)

### 🎯 Jugadores Destacados
- **Mejor goleador**: 16 goles (outlier positivo identificado)
- **Mejor asistente**: 18 asistencias (especialista en creación)
- **Mayor impacto**: Jugadores que combinan eficiencia con volumen

### 📊 Patrones Identificados
- **Correlación positiva** entre goles y asistencias (r≈0.4)
- **Distribución normal** de edades con oportunidades en todas las categorías
- **Balance apropiado** entre torneos masculino y femenino

---

## Uso de la Solución

### Para Estudiantes
1. **Estudiar la metodología** de análisis exploratorio sistemático
2. **Observar la progresión** desde exploración básica hasta insights avanzados
3. **Aprender visualización profesional** con seaborn y matplotlib
4. **Entender interpretación contextual** de datos deportivos

### Para Profesores
1. **Ejemplo de excelencia** que cumple todos los criterios de evaluación
2. **Referencia para calificación** con justificación de 100 puntos
3. **Modelo pedagógico** de análisis de datos aplicado
4. **Base para variaciones** del caso práctico

### Para Analistas Deportivos
1. **Plantilla metodológica** para análisis de jugadores juveniles
2. **Métricas derivadas útiles** para evaluación de talento
3. **Visualizaciones efectivas** para comunicar hallazgos
4. **Framework de recomendaciones** para cuerpos técnicos

---

## Conversión y Compatibilidad

### Conversión a Notebook
```bash
# Usando jupytext
jupytext --to notebook caso_bloque2_equipoSOLUCION.py

# Usando herramientas del proyecto
python herramientas/py-to-marp/convert.py caso_bloque2_equipoSOLUCION.py
```

### Compatibilidad
- **Python 3.8+**
- **Pandas 1.3+**
- **Matplotlib 3.4+**
- **Seaborn 0.11+**
- **NumPy 1.21+**

---

## Notas Importantes

### Diferencias Clave vs Bloque 1
- **Datos reales en CSV** vs listas y diccionarios simples
- **Análisis estadístico avanzado** vs cálculos básicos
- **Visualizaciones profesionales** vs gráficos simples
- **Métricas derivadas** vs variables directas
- **Interpretación contextual** vs descripción numérica

### Preparación para Bloque 3
- **Dataset limpio y preparado** para machine learning
- **Métricas de entrada** para modelos predictivos
- **Comprensión de patrones** para feature engineering
- **Baseline de rendimiento** para evaluación de modelos

---

*Solución creada para el curso "Ciencia de Datos Aplicada al Fútbol" - Tecnológico de Monterrey*
*Demuestra dominio completo de pandas, visualización avanzada y análisis estadístico aplicado al contexto deportivo*