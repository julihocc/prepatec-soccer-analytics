# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 11: ¿Cómo predecir el futuro en el fútbol usando datos?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué los equipos quieren predecir resultados? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado cómo los clubes intentan anticipar el marcador de un partido?
#
# ---
#
# ### Teoría: Introducción al modelado predictivo
#
# - Predecir = anticipar resultados usando datos del pasado
# - Modelos: herramientas matemáticas que "aprenden" patrones
# - Aplicaciones: pronóstico de partidos, fichajes, rendimiento
#
# ---
#
# ### Analogía deportiva
#
# Un modelo es como un entrenador: aprende de partidos anteriores para planear el siguiente.
#
# ---
#
# ## Práctica: Primeros pasos en predicción

# %%
# Simulación sencilla: ¿gana local o visitante?
import random
resultados = []
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
for i in range(5):
    local = random.choice(equipos)
    visitante = random.choice([e for e in equipos if e != local])
    resultado = random.choice(['Local', 'Empate', 'Visitante'])
    resultados.append({'Local': local, 'Visitante': visitante, 'Predicción': resultado})
for partido in resultados:
    print(partido)

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿En qué se parece y en qué se diferencia esta simulación de una predicción real?
#
# ---
#
# ### Práctica: ¿Qué variables influyen en el resultado?

# %%
# ¿Qué datos crees que afectan el marcador?
variables = ['Goles previos', 'Localía', 'Lesiones', 'Racha', 'Posición en tabla']
print("Variables posibles:", variables)

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Haz una lista de variables que tú considerarías para predecir el resultado de un partido.
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Modelado predictivo: anticipar usando datos
# - Modelos = entrenadores matemáticos
# - Variables relevantes para la predicción
#
# ---
#
# # SESIÓN 2: ¿Cómo funciona un modelo predictivo básico? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Puede una fórmula sencilla predecir el resultado de un partido?
#
# ---
#
# ### Teoría: Regresión lineal simple
#
# - Relaciona dos variables: por ejemplo, goles previos y probabilidad de ganar
# - El modelo "aprende" una línea que mejor se ajusta a los datos
#
# ---
#
# ### Analogía deportiva
#
# Entrenar un modelo es como practicar tiros libres: mientras más practicas, mejor predices el resultado.
#
# ---
#
# ## Práctica: Regresión lineal con datos simulados

# %%
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos simulados: goles previos y puntos obtenidos
goles_previos = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
puntos = np.array([1, 3, 3, 6, 7])

modelo = LinearRegression()
modelo.fit(goles_previos, puntos)

print("Coeficiente (pendiente):", modelo.coef_[0])
print("Intersección:", modelo.intercept_)
print("Predicción para 6 goles previos:", modelo.predict([[6]])[0])

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Crees que una sola variable es suficiente para predecir el resultado? ¿Por qué sí o por qué no?
#
# ---
#
# ### Actividad práctica
#
# Simula una regresión lineal con datos de tu equipo favorito (goles previos vs puntos).
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Regresión lineal: modelo predictivo básico
# - Entrenamiento = aprender de datos
# - Limitaciones de modelos simples
#
# ---
#
# # SESIÓN 3: ¿Cuáles son los retos y límites de predecir en fútbol? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Se puede predecir todo en el fútbol solo con datos?
#
# ---
#
# ### Teoría: Incertidumbre y factores no medibles
#
# - El fútbol tiene azar, lesiones, clima, decisiones arbitrales
# - Los modelos ayudan, pero no garantizan el futuro
#
# ---
#
# ### Analogía deportiva
#
# Un modelo que "memoriza" todos los partidos pasados (overfitting) es como un jugador que solo sabe una jugada: falla cuando cambia la situación.
#
# ---
#
# ## Práctica: Explorando el overfitting

# %%
# Simulación: modelo que memoriza
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])  # Relación no lineal
modelo = LinearRegression()
modelo.fit(x.reshape(-1, 1), y)
print("Predicción para 6:", modelo.predict([[6]])[0])

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué riesgos hay si un modelo solo "memoriza" los datos? ¿Cómo evitarlo?
#
# ---
#
# ### Actividad práctica
#
# Piensa en un ejemplo donde un modelo podría fallar por no considerar factores externos.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Retos del modelado: azar, factores externos
# - Overfitting: memorizar vs aprender patrones
# - Importancia de la interpretación humana
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué variable te parece más importante para predecir?
# - ¿Por qué no todo es predecible en el fútbol?
# - ¿Qué aprendiste sobre los límites de los modelos?
#
# ---
#
# # Próxima semana
#
# - Modelos de clasificación y comparación
# - Predicción de resultados (ganar, empatar, perder)
# - Profundización en Machine Learning
#
# **¿Listo para llevar tus predicciones al siguiente nivel?**
