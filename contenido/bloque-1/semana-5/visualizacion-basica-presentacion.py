# ---
# marp: true
# theme: default
# paginate: true
# class: lead
# ---

# %% [markdown]
# # Semana 5: ¿Cómo comunican los analistas sus hallazgos?
#
# **Programación Básica 1 – Prepa Tec**
#
# ---
#
# # SESIÓN 1: ¿Por qué una imagen vale más que mil datos? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Alguna vez has entendido mejor un partido viendo una gráfica que leyendo una tabla?
#
# ---
#
# ### Teoría: El poder de la visualización
#
# - Las gráficas ayudan a ver patrones ocultos
# - Facilitan la comunicación de resultados
# - Son esenciales en el análisis deportivo profesional
#
# ---
#
# ### Analogía deportiva
#
# ¿Recuerdas cuando un entrenador usa pizarrón para explicar jugadas? Las gráficas son el pizarrón de los datos.
#
# ---
#
# ## Descubriendo Matplotlib y Seaborn
#
# - Matplotlib: la herramienta básica para crear gráficas en Python
# - Seaborn: hace que las gráficas sean más bonitas y fáciles de entender
#
# ---
#
# ### Práctica: Tu primer gráfico de barras

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="viridis")

equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
goles = [85, 80, 92, 78]

plt.bar(equipos, goles)
plt.title('Goles por equipo en la temporada')
plt.xlabel('Equipo')
plt.ylabel('Goles')
plt.show()

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué información te da la gráfica que no ves fácilmente en una tabla?
#
# ---
#
# ### Práctica: Gráfica de líneas para evolución

# %%
jornadas = [1, 2, 3, 4, 5]
goles_barcelona = [2, 3, 1, 4, 2]
goles_madrid = [1, 2, 2, 3, 1]

plt.plot(jornadas, goles_barcelona, marker='o', label='Barcelona')
plt.plot(jornadas, goles_madrid, marker='s', label='Real Madrid')
plt.title('Evolución de goles por jornada')
plt.xlabel('Jornada')
plt.ylabel('Goles')
plt.legend()
plt.show()

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Para qué situaciones deportivas sería útil una gráfica de líneas?
#
# ---
#
# ### Práctica: Gráfica de dispersión (scatter)

# %%
import numpy as np
edades = np.random.randint(18, 35, size=20)
goles = np.random.randint(0, 20, size=20)

plt.scatter(edades, goles)
plt.title('Relación entre edad y goles')
plt.xlabel('Edad')
plt.ylabel('Goles')
plt.show()

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué patrones podrías descubrir con una gráfica de dispersión?
#
# ---
#
# ### Actividad práctica
#
# Crea una gráfica de barras con los minutos jugados por 5 jugadores de tu equipo favorito. ¿Quién jugó más?
#
# ---
#
# ## Síntesis de la sesión 1
#
# - Visualización: clave para comunicar hallazgos
# - Gráficas de barras, líneas y dispersión
# - Herramientas: Matplotlib y Seaborn
# - Ventajas: claridad, impacto, análisis visual
#
# ---
#
# # SESIÓN 2: ¿Cómo elegir la mejor gráfica para cada tipo de dato? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Todas las gráficas sirven para cualquier tipo de dato?
#
# ---
#
# ### Teoría: Tipos de gráficas y sus usos
#
# - Barras: comparar cantidades
# - Líneas: mostrar evolución
# - Dispersión: ver relaciones
# - Pastel: mostrar proporciones
#
# ---
#
# ### Analogía deportiva
#
# Elegir la gráfica correcta es como elegir la mejor formación para un partido: depende de la situación.
#
# ---
#
# ### Práctica: Gráfica de pastel

# %%
posesion = [55, 25, 20]
etiquetas = ['Barcelona', 'Real Madrid', 'Otros']

plt.pie(posesion, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Porcentaje de posesión de balón')
plt.show()

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿En qué casos sería útil una gráfica de pastel en el fútbol?
#
# ---
#
# ### Práctica: Personalización de gráficas

# %%
plt.bar(equipos, goles, color=['#4C72B0', '#DD8452', '#55A868', '#C44E52'])
plt.title('Goles por equipo (colores personalizados)')
plt.xlabel('Equipo')
plt.ylabel('Goles')
plt.show()

# %% [markdown]
# ---
#
# ### Actividad práctica
#
# Elige un tipo de gráfica y justifica por qué es la mejor opción para mostrar los datos de tarjetas amarillas de tu equipo favorito.
#
# ---
#
# ## Síntesis de la sesión 2
#
# - Tipos de gráficas y cuándo usarlas
# - Personalización para mayor claridad
# - Importancia de elegir bien según el dato
#
# ---
#
# # SESIÓN 3: ¿Cómo crear reportes visuales profesionales? (50 min)
#
# ---
#
# ## Pregunta guía
#
# ¿Cómo presentarías tus hallazgos a un entrenador o directivo?
#
# ---
#
# ### Teoría: El arte de contar historias con datos
#
# - Un buen reporte combina datos, gráficas y explicaciones
# - La visualización debe responder preguntas clave
# - El diseño importa: claridad y orden
#
# ---
#
# ### Práctica: Mini-reporte visual

# %%
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].bar(equipos, goles)
axs[0].set_title('Goles por equipo')
axs[0].set_xlabel('Equipo')
axs[0].set_ylabel('Goles')

axs[1].pie(posesion, labels=etiquetas, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Posesión de balón')

plt.suptitle('Reporte visual de desempeño')
plt.tight_layout()
plt.show()

# %% [markdown]
# ---
#
# ### Reflexión
#
# ¿Qué elementos hacen que un reporte visual sea profesional y fácil de entender?
#
# ---
#
# ### Actividad práctica
#
# Crea un mini-reporte visual con al menos dos tipos de gráficas usando datos de tu equipo favorito.
#
# ---
#
# ## Síntesis de la sesión 3
#
# - Reportes visuales: combinación de gráficas y análisis
# - Importancia de la narrativa visual
# - Herramientas para presentaciones profesionales
#
# ---
#
# # Preguntas para tu autoevaluación
#
# - ¿Qué tipo de gráfica te resultó más útil y por qué?
# - ¿Cómo elegirías la mejor visualización para un dato nuevo?
# - ¿Qué aprendiste sobre comunicar hallazgos?
#
# ---
#
# # Próxima semana
#
# - Introducción a la ciencia de datos aplicada al fútbol
# - Primeros análisis con datos reales
# - Preparación para el siguiente bloque
#
# **¿Listo para analizar datos reales de fútbol?**
