# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 7: ¿Qué tipos de datos existen en el fútbol y cómo se analizan?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué es importante distinguir tipos de datos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado por qué no puedes sumar nombres de jugadores, pero sí goles?
#
# ---
#
# ### Teoría: Tipos de datos en ciencia de datos
#
# - Números (cuantitativos): goles, minutos jugados, edad
# - Texto (cualitativos): nombre, posición, nacionalidad
# - Fechas: día del partido, nacimiento
#
# ---
#
# ### Analogía deportiva
#
# En una alineación, ¿qué diferencia hay entre el número de camiseta y el nombre del jugador?
#
# ---
#
# ## Práctica: Identificando tipos de datos en un DataFrame

# %%
import pandas as pd
jugadores = pd.DataFrame({
    'nombre': ['Messi', 'Cristiano', 'Mbappé', 'Haaland'],
    'edad': [36, 39, 25, 24],
    'goles': [30, 28, 22, 25],
    'posicion': ['Delantero', 'Delantero', 'Delantero', 'Delantero'],
    'fecha_nacimiento': ['1987-06-24', '1985-02-05', '1998-12-20', '2000-07-21']
})
print(jugadores.dtypes)

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué operaciones puedes hacer con cada tipo de dato? ¿Qué limitaciones encuentras?
#
# ---
#
# ### Práctica: Conversión de tipos de datos

# %%
jugadores['fecha_nacimiento'] = pd.to_datetime(jugadores['fecha_nacimiento'])
print(jugadores.dtypes)

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Crea un DataFrame con 3 variables numéricas, 2 de texto y 1 de fecha para tu equipo favorito. Identifica los tipos de datos.
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Tipos de datos: numéricos, texto, fechas
# - Importancia de distinguirlos para análisis correcto
# - Conversión de tipos en pandas
#
# ---
#
# # SESIÓN 2: ¿Cómo analizar variables categóricas y numéricas? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Se analizan igual los goles que las posiciones de los jugadores?
#
# ---
#
# ### Teoría: Análisis según el tipo de variable
#
# - Numéricas: promedios, sumas, máximos
# - Categóricas: conteos, agrupaciones
#
# ---
#
# ### Analogía deportiva
#
# Analizar posiciones es como contar cuántos defensas y delanteros hay en la cancha, no sumar sus nombres.
#
# ---
#
# ### Práctica: Agrupando y contando categorías

# %%
conteo_posiciones = jugadores['posicion'].value_counts()
print(conteo_posiciones)

# %% [markdown]
# ---
#
# ### Práctica: Estadísticas de variables numéricas

# %%
print(jugadores['goles'].mean())
print(jugadores['edad'].max())

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Agrupa a los jugadores de tu DataFrame por posición y cuenta cuántos hay en cada una. Calcula el promedio de goles por posición.
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Análisis de variables numéricas y categóricas
# - Agrupaciones y conteos
# - Estadísticas básicas según el tipo de dato
#
# ---
#
# # SESIÓN 3: ¿Cómo preparar los datos para análisis más avanzados? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Qué pasos previos necesitas antes de hacer análisis estadístico o modelos?
#
# ---
#
# ### Teoría: Preparación y limpieza de datos
#
# - Revisar tipos de datos
# - Eliminar duplicados
# - Completar o eliminar valores faltantes
#
# ---
#
# ### Práctica: Limpieza básica

# %%
# Eliminar duplicados
jugadores = jugadores.drop_duplicates()
# Rellenar valores faltantes (si hubiera)
jugadores = jugadores.fillna(0)
print(jugadores)

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Por qué es importante limpiar y preparar los datos antes de analizarlos?
#
# ---
#
# ### Actividad práctica
#
# Busca o simula un error en tu DataFrame (valor faltante o duplicado) y corrígelo.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Preparación y limpieza: paso previo esencial
# - Métodos: drop_duplicates, fillna
# - Importancia de la calidad de los datos
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué tipo de dato te resultó más fácil de analizar?
# - ¿Por qué es importante distinguir variables categóricas y numéricas?
# - ¿Qué aprendiste sobre la limpieza de datos?
#
# ---
#
# # Próxima semana
#
# - Estadística descriptiva aplicada al fútbol
# - Análisis de tendencias y patrones
# - Preparación para visualización avanzada
#
# **¿Listo para analizar tendencias en el fútbol?**
