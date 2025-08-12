# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 13: ¿Cómo saber si tu modelo de predicción es realmente bueno?
#
# **Ciencia de Datos aplicada al Fútbol – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué no basta con tener un modelo, sino que hay que evaluarlo? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Te has preguntado cómo los analistas deciden si un modelo es útil o no?
#
# ---
#
# ### Teoría: Evaluación de modelos
#
# - Precisión: porcentaje de aciertos
# - Matriz de confusión: aciertos y errores por clase
# - Importancia de analizar errores y aciertos
#
# ---
#
# ### Analogía deportiva
#
# Evaluar un modelo es como revisar el porcentaje de penales anotados vs fallados: mide el desempeño real.
#
# ---
#
# ## Práctica: Precisión y matriz de confusión

# %%
from sklearn.metrics import accuracy_score, confusion_matrix

# Supón que tienes predicciones y resultados reales
reales = [1, 0, 1, 1, 0]
predichos = [1, 0, 0, 1, 1]

print("Precisión:", accuracy_score(reales, predichos))
print("Matriz de confusión:\n", confusion_matrix(reales, predichos))

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué significa tener alta precisión pero muchos errores en una clase específica?
#
# ---
#
# ### Actividad práctica
#
# Calcula la precisión y la matriz de confusión para un modelo simulado con tus propios datos.
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Precisión y matriz de confusión: evaluación básica
# - Importancia de analizar errores y aciertos
#
# ---
#
# # SESIÓN 2: ¿Cómo comparar diferentes modelos de predicción? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Siempre el modelo con mayor precisión es el mejor?
#
# ---
#
# ### Teoría: Comparación de modelos
#
# - Precisión no lo es todo: importancia de otros factores
# - Simplicidad, interpretabilidad, velocidad
# - Elegir el modelo adecuado para el problema
#
# ---
#
# ### Analogía deportiva
#
# Elegir un modelo es como elegir un portero: no solo importa cuántos goles ataja, sino cómo se adapta al equipo.
#
# ---
#
# ## Práctica: Comparando modelos

# %%
# Supón que tienes dos modelos con diferentes precisiones
precision_modelo1 = 0.85
precision_modelo2 = 0.80
print("Modelo 1: Precisión =", precision_modelo1)
print("Modelo 2: Precisión =", precision_modelo2)
print("¿Cuál elegirías y por qué?")

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿En qué casos preferirías un modelo menos preciso pero más simple o rápido?
#
# ---
#
# ### Actividad práctica
#
# Compara dos modelos (simulados o reales) y justifica tu elección más allá de la precisión.
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Comparación de modelos: precisión y otros factores
# - Importancia de la interpretación y el contexto
#
# ---
#
# # SESIÓN 3: ¿Cómo mejorar la calidad de tus modelos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Qué puedes hacer si tu modelo no es suficientemente bueno?
#
# ---
#
# ### Teoría: Mejoras simples en modelos
#
# - Agregar variables relevantes
# - Ajustar parámetros básicos
# - Validar con nuevos datos
#
# ---
#
# ### Analogía deportiva
#
# Mejorar un modelo es como entrenar más: pruebas nuevas tácticas y analizas resultados.
#
# ---
#
# ## Práctica: Mejorando un modelo

# %%
# Supón que agregas una variable nueva
print("Antes: precisión = 0.80")
print("Después de agregar variable: precisión = 0.85")

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué variable agregarías para mejorar la predicción en fútbol?
#
# ---
#
# ### Actividad práctica
#
# Propón una mejora para un modelo simulado y evalúa el cambio en precisión.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Mejoras simples: nuevas variables, ajustes básicos
# - Validación con datos nuevos
# - Importancia de la experimentación
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Por qué no basta con la precisión para elegir un modelo?
# - ¿Qué aprendiste sobre comparar y mejorar modelos?
# - ¿Qué variable agregarías para mejorar la predicción?
#
# ---
#
# # Próxima semana
#
# - Feature engineering básico
# - Optimización de modelos
# - Preparación para el proyecto final
#
# **¿Listo para optimizar y aplicar tus modelos en un reto real?**
