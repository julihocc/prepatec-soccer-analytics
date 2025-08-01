# Datasets del Curso - Evaluaciones

## Información General

Esta carpeta contiene todos los datasets utilizados en las evaluaciones del curso de Data Science aplicado al análisis de fútbol. Los datos están diseñados específicamente para el contexto educativo y progresivo del curso.

## Datasets Disponibles

### Datos Principales

1. **`futbol-basico.csv`** - Dataset principal para ejercicios básicos
   - **Registros:** 10 equipos con estadísticas básicas
   - **Columnas:** Equipo, Liga, Puntos, Goles_Favor, Goles_Contra
   - **Uso:** Ejercicios introductorios de Bloque 1
   - **Formato:** CSV con headers, encoding UTF-8

### Datos del Proyecto Integrador

2. **`equipos.csv`** - Equipos de la Liga Simulada (Será creado en el proyecto)
   - **Registros:** 15 equipos con información completa
   - **Columnas:** Nombre, Ciudad, Fundacion, Estadio, Capacidad, Liga, Presupuesto
   - **Uso:** Proyecto integrador del Bloque 1
   - **Características:** Datos realistas de equipos españoles

3. **`jugadores.csv`** - Jugadores del Sistema (Será creado en el proyecto)
   - **Registros:** 28 jugadores distribuidos entre equipos
   - **Columnas:** Nombre, Edad, Posicion, Equipo, Goles, Asistencias, Partidos, Valor_Mercado
   - **Uso:** Análisis de rendimiento individual
   - **Características:** Estadísticas equilibradas y realistas

4. **`partidos.csv`** - Resultados de Partidos (Será creado en el proyecto)
   - **Registros:** 20 partidos con resultados completos
   - **Columnas:** Fecha, Equipo_Local, Equipo_Visitante, Goles_Local, Goles_Visitante, Asistencia
   - **Uso:** Análisis de encuentros y tendencias
   - **Características:** Fechas y resultados coherentes

### Datos Complementarios

5. **`equipos-europa-2023-24.csv`** - Equipos Europeos Temporada 2023-24
   - **Registros:** 20 equipos de las principales ligas europeas
   - **Columnas:** Temporada, Equipo, Liga, Puntos, Goles_Favor, Goles_Contra, Victorias, Empates, Derrotas, Presupuesto
   - **Uso:** Ejercicios avanzados y comparaciones internacionales
   - **Características:** Datos reales aproximados de la temporada 2023-24

6. **`jugadores-estrellas-2024.csv`** - Jugadores Estrella del Fútbol Mundial
   - **Registros:** 25 jugadores de élite mundial
   - **Columnas:** Nombre, Edad, Posicion, Equipo, Liga, Goles, Asistencias, Partidos, Valor_Mercado, Salario_Anual
   - **Uso:** Análisis de mercado y comparaciones de élite
   - **Características:** Jugadores reconocidos mundialmente con valores aproximados

## Estructura de Datos

### Convenciones de Nombres

- **Equipos:** Nombres oficiales en español/inglés según liga
- **Posiciones:** Portero, Defensa, Centrocampista, Delantero
- **Ligas:** La Liga, Premier League, Bundesliga, Ligue 1, Serie A, MLS, Saudi Pro
- **Fechas:** Formato YYYY-MM-DD
- **Monedas:** Euros para valores europeos, dólares para MLS

### Tipos de Datos

```python
# Ejemplo de carga estándar
import pandas as pd

# Cargar con tipos apropiados
df = pd.read_csv('dataset.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'])  # Si hay fechas
df['Valor_Mercado'] = df['Valor_Mercado'].astype(float)  # Valores numéricos
```

## Uso en Ejercicios

### Bloque 1: Prerrequisitos de Programación

- **Semana 1-3:** `futbol-basico.csv` para operaciones básicas
- **Semana 4-5:** `equipos-europa-2023-24.csv` y `jugadores-estrellas-2024.csv` para pandas/numpy
- **Proyecto:** Crear datasets propios del proyecto integrador

### Bloque 2: Fundamentos de Data Science (Futuro)

- Datasets más complejos con datos temporales
- Múltiples temporadas y métricas avanzadas
- Datos de transferencias y mercado

### Bloque 3: Modelado Predictivo (Futuro)

- Datos históricos para predicciones
- Features engineered para machine learning
- Datasets de validación y testing

## Calidad de Datos

### Validaciones Implementadas

1. **Consistencia:** Equipos y jugadores coherentes entre datasets
2. **Realismo:** Valores aproximados a la realidad 2023-24
3. **Completitud:** Sin valores faltantes en campos críticos
4. **Variabilidad:** Suficiente diversidad para análisis estadístico

### Limitaciones Conocidas

- **Datos simulados:** No son estadísticas oficiales exactas
- **Simplificación:** Algunas métricas están simplificadas para nivel educativo
- **Temporalidad:** Basados en temporada 2023-24, pueden desactualizarse

## Actualización y Mantenimiento

### Programación de Actualizaciones

- **Anual:** Actualización de valores de mercado y salarios
- **Semestral:** Revisión de estadísticas de temporada
- **Por demanda:** Corrección de errores o inconsistencias reportadas

### Versionado

- **v1.0:** Datasets iniciales del Bloque 1
- **v1.1:** Adición de datasets complementarios europeos
- **v2.0:** Datasets del Bloque 2 (planificado)

## Soporte y Contacto

Para reportar errores en los datos o sugerir mejoras:

1. **Revisión técnica:** Verificar carga correcta con pandas
2. **Validación lógica:** Confirmar que los valores tienen sentido deportivo
3. **Reporte:** Documentar problema específico con ejemplos
4. **Propuesta:** Sugerir corrección o mejora

---

**Datasets diseñados específicamente para educación en Data Science deportivo - Nivel Preparatoria**
