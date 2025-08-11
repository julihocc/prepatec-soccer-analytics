# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 14: ¿Cómo mejorar y optimizar tus modelos de predicción en fútbol?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué crear nuevas variables puede mejorar tus predicciones? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado si hay información oculta en los datos que podrías aprovechar?
#
# ---
#
# ### Teoría: Feature engineering básico
#
# - Crear nuevas variables a partir de las existentes
# - Ejemplo: promedio de goles por partido, diferencia de goles
# - Mejora la capacidad del modelo para encontrar patrones
#
# ---
#
# ### Analogía deportiva
#
# Crear una nueva variable es como descubrir una jugada sorpresa que cambia el partido.
#
# ---
#
# ## Práctica: Creando variables nuevas

# %%
import pandas as pd
datos = pd.DataFrame({
    'goles': [2, 1, 3, 0, 2],
    'partidos': [5, 5, 5, 5, 5]
})
datos['promedio_goles'] = datos['goles'] / datos['partidos']
print(datos)

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué otras variables podrías crear a partir de los datos disponibles?
#
# ---
#
# ### Actividad práctica
#
# Crea al menos dos variables nuevas usando datos de tu equipo favorito.
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Feature engineering: crear variables útiles
# - Ejemplos prácticos en fútbol
# - Impacto en la calidad del modelo
#
# ---
#
# # SESIÓN 2: ¿Cómo ajustar y optimizar un modelo básico? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Un modelo siempre funciona igual con cualquier configuración?
#
# ---
#
# ### Teoría: Ajuste de parámetros básicos
#
# - Cambiar parámetros puede mejorar el desempeño
# - Ejemplo: número de árboles en un Random Forest
# - Probar diferentes configuraciones y comparar resultados
#
# ---
#
# ### Analogía deportiva
#
# Ajustar un modelo es como cambiar la alineación o táctica según el rival.
#
# ---
#
# ## Práctica: Ajustando parámetros

# %%
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=100, n_features=4, random_state=42)
modelo = RandomForestClassifier(n_estimators=10, random_state=42)
modelo.fit(X, y)
print("Precisión con 10 árboles:", modelo.score(X, y))

modelo2 = RandomForestClassifier(n_estimators=50, random_state=42)
modelo2.fit(X, y)
print("Precisión con 50 árboles:", modelo2.score(X, y))

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué parámetro crees que tendría mayor impacto en el resultado?
#
# ---
#
# ### Actividad práctica
#
# Ajusta un parámetro de un modelo simulado y observa el cambio en precisión.
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Ajuste de parámetros: optimización básica
# - Comparación de resultados
# - Importancia de experimentar
#
# ---
#
# # SESIÓN 3: ¿Cómo integrar mejoras y preparar un modelo para el reto final? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo combinarías todo lo aprendido para enfrentar un reto real?
#
# ---
#
# ### Teoría: Integración y validación final
#
# - Combinar nuevas variables y parámetros óptimos
# - Validar el modelo con datos no vistos
# - Preparación para el proyecto final
#
# ---
#
# ### Práctica: Mini-proyecto de integración

# %%
# Simula la integración de mejoras
print("Modelo final: incluye nuevas variables y parámetros ajustados.")
print("Validación con datos nuevos: precisión = 0.88")

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué pasos seguirías para asegurar que tu modelo es confiable antes de presentarlo?
#
# ---
#
# ### Actividad práctica
#
# Prepara un mini-proyecto integrando feature engineering y optimización con tus propios datos.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Integración de mejoras: variables y parámetros
# - Validación final antes del reto
# - Preparación para el proyecto integrador
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué variable nueva fue la más útil?
# - ¿Qué parámetro tuvo mayor impacto?
# - ¿Qué aprendiste sobre la integración de mejoras?
#
# ---
#
# # Próxima semana
#
# - Proyecto final integrador
# - Presentación de resultados
# - Reflexión sobre el aprendizaje
#
# **¿Listo para aplicar todo lo aprendido en un reto real?**
