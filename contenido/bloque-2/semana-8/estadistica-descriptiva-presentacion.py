# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 8: ¿Cómo se resumen y entienden los datos en el fútbol?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué es útil la estadística descriptiva en el fútbol? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado cómo los analistas resumen el rendimiento de un equipo en una sola cifra?
#
# ---
#
# ### Teoría: Estadística descriptiva básica
#
# - Promedio (media): el valor típico
# - Mediana: el valor central
# - Moda: el valor más frecuente
# - Rango: diferencia entre el mayor y el menor
#
# ---
#
# ### Analogía deportiva
#
# El promedio de goles es como el promedio de calificaciones: te da una idea general, pero no cuenta toda la historia.
#
# ---
#
# ## Práctica: Calculando estadísticas básicas

# %%
import pandas as pd
import numpy as np

goles = [2, 1, 3, 0, 2, 4, 1, 3, 2, 1]
print("Promedio:", np.mean(goles))
print("Mediana:", np.median(goles))
print("Moda:", pd.Series(goles).mode()[0])
print("Rango:", np.max(goles) - np.min(goles))

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué información aporta cada estadístico? ¿En qué casos sería engañoso usar solo el promedio?
#
# ---
#
# ### Práctica: Estadística en DataFrames

# %%
datos = pd.DataFrame({
    'equipo': ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich'],
    'goles': [85, 80, 92, 78],
    'partidos': [38, 38, 38, 38]
})
print(datos['goles'].mean())
print(datos['goles'].median())
print(datos['goles'].max())

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Calcula el promedio, mediana y rango de goles de tu equipo favorito en los últimos 5 partidos.
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Estadística descriptiva: media, mediana, moda, rango
# - Aplicación en fútbol: resumen de rendimiento
# - Importancia de interpretar correctamente los resultados
#
# ---
#
# # SESIÓN 2: ¿Cómo detectar tendencias y patrones en los datos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Puedes identificar si un equipo está mejorando o empeorando solo con los datos?
#
# ---
#
# ### Teoría: Tendencias y variabilidad
#
# - Tendencia: aumento o disminución a lo largo del tiempo
# - Desviación estándar: qué tan dispersos están los datos
#
# ---
#
# ### Analogía deportiva
#
# Detectar una racha ganadora es como ver si tus calificaciones suben o bajan a lo largo del semestre.
#
# ---
#
# ### Práctica: Analizando tendencias

# %%
jornadas = [1, 2, 3, 4, 5]
goles = [2, 3, 1, 4, 2]
print("Promedio de goles:", np.mean(goles))
print("Desviación estándar:", np.std(goles))
print("¿Tendencia positiva?", goles[-1] > goles[0])

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿En qué casos una tendencia puede ser engañosa? ¿Qué otros factores deberías considerar?
#
# ---
#
# ### Práctica: Variabilidad en DataFrames

# %%
print(datos['goles'].std())

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Analiza la tendencia de goles de tu equipo en los últimos 5 partidos. ¿Va en ascenso o descenso?
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Tendencias y variabilidad: claves para entender el rendimiento
# - Desviación estándar como medida de dispersión
# - Importancia de analizar más allá del promedio
#
# ---
#
# # SESIÓN 3: ¿Cómo comunicar hallazgos estadísticos de manera clara? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo explicarías a un entrenador si el equipo está mejorando o no?
#
# ---
#
# ### Teoría: Comunicación de resultados
#
# - Usar cifras clave y comparaciones
# - Explicar el significado, no solo el número
#
# ---
#
# ### Práctica: Mini-reporte estadístico

# %%
print("En los últimos 5 partidos, el promedio de goles fue de 2.4, con una tendencia positiva.")
print("La desviación estándar indica que el rendimiento es consistente.")

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué hace que una explicación estadística sea clara y útil?
#
# ---
#
# ### Actividad práctica
#
# Redacta un breve reporte sobre el rendimiento de tu equipo usando al menos dos estadísticas descriptivas.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Comunicación clara de hallazgos
# - Importancia de contextualizar los números
# - Preparación para visualización avanzada
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué estadístico te resultó más útil y por qué?
# - ¿Cómo detectarías una tendencia engañosa?
# - ¿Qué aprendiste sobre comunicar resultados?
#
# ---
#
# # Próxima semana
#
# - Visualización avanzada de datos
# - Integración de estadística y gráficos
# - Preparación para análisis más complejos
#
# **¿Listo para visualizar y comunicar datos como un profesional?**
