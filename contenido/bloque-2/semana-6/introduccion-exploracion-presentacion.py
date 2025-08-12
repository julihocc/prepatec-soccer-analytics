# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 6: ¿Cómo empieza el análisis de datos en el fútbol real?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué es importante explorar los datos antes de analizarlos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado cómo un club de fútbol decide qué datos analizar primero?
#
# ---
#
# ### Teoría: El primer contacto con los datos
#
# - Antes de cualquier análisis, hay que conocer los datos
# - La exploración permite detectar errores, patrones y oportunidades
# - Es el paso inicial de todo proyecto de ciencia de datos
#
# ---
#
# ### Analogía deportiva
#
# Explorar datos es como un entrenador que observa a sus jugadores en el primer entrenamiento: busca fortalezas, debilidades y sorpresas.
#
# ---
#
# ## Práctica: Cargando y observando un dataset real

# %%
import pandas as pd
import numpy as np

# Simulamos un dataset de partidos
partidos = pd.DataFrame({
    'equipo_local': ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich', 'Barcelona'],
    'equipo_visitante': ['Bayern Munich', 'Manchester City', 'Barcelona', 'Real Madrid', 'Manchester City'],
    'goles_local': [2, 1, 3, 0, 2],
    'goles_visitante': [1, 2, 1, 2, 3],
    'temporada': ['2023-24']*5
})
print(partidos)

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué información puedes obtener solo con ver la tabla? ¿Qué preguntas surgen?
#
# ---
#
# ### Práctica: Métodos básicos de exploración

# %%
print(partidos.head())  # Primeras filas
print(partidos.info())  # Tipos de datos y nulos
print(partidos.describe())  # Estadísticas básicas

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué diferencias hay entre ver la tabla completa y usar estos métodos?
#
# ---
#
# ### Actividad práctica
#
# Carga un DataFrame con datos de 5 partidos de tu equipo favorito. ¿Qué patrones o curiosidades encuentras?
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Exploración: primer paso crítico en ciencia de datos
# - Métodos: head, info, describe
# - Importancia de conocer los datos antes de analizar
#
# ---
#
# # SESIÓN 2: ¿Cómo identificar patrones y errores en los datos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Alguna vez has encontrado datos que no tienen sentido en una tabla deportiva?
#
# ---
#
# ### Teoría: Detección de valores atípicos y errores
#
# - Los datos pueden tener errores de captura o valores extremos
# - Identificar estos casos es clave para un análisis confiable
#
# ---
#
# ### Analogía deportiva
#
# Detectar errores en los datos es como revisar si todos los jugadores están en la alineación correcta antes de un partido.
#
# ---
#
# ### Práctica: Búsqueda de valores extraños

# %%
# Agregamos un error intencional
datos = partidos.copy()
datos.loc[2, 'goles_local'] = 99  # Error evidente
print(datos)

# Detectar valores fuera de rango
print(datos[datos['goles_local'] > 10])

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué harías si encuentras un dato imposible? ¿Cómo lo corregirías?
#
# ---
#
# ### Práctica: Limpieza básica de datos

# %%
# Corregimos el error
datos.loc[datos['goles_local'] > 10, 'goles_local'] = datos['goles_local'].median()
print(datos)

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Introduce un error en tu propio DataFrame y corrígelo usando una técnica similar.
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Importancia de detectar y corregir errores
# - Métodos para identificar valores atípicos
# - Limpieza básica para análisis confiable
#
# ---
#
# # SESIÓN 3: ¿Cómo documentar y comunicar lo que descubriste? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo explicarías tus hallazgos a un entrenador o compañero?
#
# ---
#
# ### Teoría: Documentar y compartir descubrimientos
#
# - Escribir conclusiones claras es parte del trabajo profesional
# - La comunicación efectiva es tan importante como el análisis
#
# ---
#
# ### Práctica: Síntesis y reporte básico

# %%
# Ejemplo de síntesis
print("En los 5 partidos analizados, el equipo local ganó el 60% de las veces.")
print("El promedio de goles por partido fue:", datos[['goles_local', 'goles_visitante']].mean().mean())

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué hace que una conclusión sea clara y útil para otros?
#
# ---
#
# ### Actividad práctica
#
# Redacta una conclusión breve sobre los datos de tus partidos. ¿Qué recomendarías analizar a continuación?
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Documentar hallazgos: parte esencial del análisis
# - Importancia de la comunicación clara
# - Preparación para análisis más avanzados
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué fue lo más fácil y lo más difícil de explorar datos?
# - ¿Cómo detectarías errores en un dataset más grande?
# - ¿Qué aprendiste sobre la importancia de la limpieza de datos?
#
# ---
#
# # Próxima semana
#
# - Tipos de datos futbolísticos
# - Análisis más profundo de variables
# - Preparación para estadística descriptiva
#
# **¿Listo para profundizar en los datos del fútbol?**
